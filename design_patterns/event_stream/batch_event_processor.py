from typing import Set, List, Dict
from threading import Lock
from concurrent.futures import ThreadPoolExecutor, as_completed
import heapq
from datastructures.bloom_filter import BloomFilter
from design_patterns.event_stream.prioritized_event import PrioritizedEvent
from design_patterns.event_stream.event_priority_mapper import EventPriorityMapper
from design_patterns.circuit_breaker import CircuitBreaker
from design_patterns.event_stream.message_state_manager import MessageStateManager
from design_patterns.event_stream.event import Event


class BatchEventProcessor:
    """
    High-performance batch event processor with:
    - Priority-based processing
    - Deduplication
    - Concurrent processing
    - Circuit breaker protection
    """

    def __init__(
        self,
        state_manager: MessageStateManager,
        max_workers: int = 10,
        batch_size: int = 100,
    ):
        self.state_manager = state_manager
        self.max_workers = max_workers
        self.batch_size = batch_size

        # Event deduplication
        self.seen_events = BloomFilter(size=100000)
        self.confirmed_events: Set[str] = set()  # For exact dedup
        self.dedup_lock = Lock()

        # Priority queue for event ordering
        self.event_queue: List[PrioritizedEvent] = []
        self.queue_lock = Lock()

        # Circuit breaker for fault tolerance
        self.circuit_breaker = CircuitBreaker()

        # Metrics
        self.metrics = {
            "processed": 0,
            "skipped_duplicates": 0,
            "failed": 0,
            "total_batches": 0,
        }

    @staticmethod
    def _event_fingerprint(event: Event) -> str:
        """Generate unique fingerprint for event deduplication"""
        return (
            f"{event.event_type.value}:{event.message_id}:{event.timestamp.isoformat()}"
        )

    def is_duplicate(self, event: Event) -> bool:
        """Check if event is a duplicate using bloom filter plus set"""
        fingerprint = self._event_fingerprint(event)

        with self.dedup_lock:
            # Check the exact set first for confirmed duplicates
            if fingerprint in self.confirmed_events:
                return True

            # Not a duplicate - add to both structures
            self.seen_events.add(fingerprint)
            self.confirmed_events.add(fingerprint)
            return False

    def enqueue_event(self, event: Event):
        """Add event to priority queue"""
        if self.is_duplicate(event):
            self.metrics["skipped_duplicates"] += 1
            return

        priority = EventPriorityMapper.get_priority(event.event_type)
        prioritized = PrioritizedEvent(priority, event.timestamp, event)

        with self.queue_lock:
            heapq.heappush(self.event_queue, prioritized)

    def enqueue_events(self, events: List[Event]):
        """Bulk enqueue events"""
        for event in events:
            self.enqueue_event(event)

    def _process_single_event(self, event: Event) -> bool:
        """Process a single event with the circuit breaker"""
        try:
            return self.circuit_breaker.call(self.state_manager.process_event, event)
        except Exception as e:
            self.metrics["failed"] += 1
            print(f"Error processing event {event.event_type.value}: {e}")
            return False

    def process_batch(self, batch_size: int = None) -> Dict[str, int]:
        """
        Process a batch of events from the queue.
        Returns metrics for the batch.
        """
        batch_size = batch_size or self.batch_size
        batch_metrics = {"processed": 0, "failed": 0}

        # Extract batch from queue
        batch = []
        with self.queue_lock:
            while len(batch) < batch_size and self.event_queue:
                prioritized = heapq.heappop(self.event_queue)
                batch.append(prioritized.event)

        if not batch:
            return batch_metrics

        self.metrics["total_batches"] += 1

        # Process batch concurrently
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._process_single_event, event): event
                for event in batch
            }

            for future in as_completed(futures):
                try:
                    success = future.result()
                    if success:
                        batch_metrics["processed"] += 1
                        self.metrics["processed"] += 1
                    else:
                        batch_metrics["failed"] += 1
                except Exception as e:
                    batch_metrics["failed"] += 1
                    print(f"Batch processing error: {e}")

        return batch_metrics

    def process_all(self) -> Dict[str, int]:
        """Process all events in the queue"""
        total_metrics = {"processed": 0, "failed": 0, "batches": 0}

        while True:
            with self.queue_lock:
                if not self.event_queue:
                    break

            batch_metrics = self.process_batch()
            total_metrics["processed"] += batch_metrics["processed"]
            total_metrics["failed"] += batch_metrics["failed"]
            total_metrics["batches"] += 1

        return total_metrics

    def get_metrics(self) -> Dict[str, int]:
        """Get processing metrics"""
        return {
            **self.metrics,
            "queue_size": len(self.event_queue),
            "dedup_set_size": len(self.confirmed_events),
        }

    def get_queue_size(self) -> int:
        """Get current queue size"""
        with self.queue_lock:
            return len(self.event_queue)
