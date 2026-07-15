from typing import List
from heapq import heapify, heappop, heappush
from datastructures.trees.heaps.binary.min_heap import MinHeap, HeapNode


def connect_sticks(sticks: List[int]) -> int:
    """
    Calculates the minimum cost to connect all sticks.

    The function takes a list of integers, representing the length of each stick.
    It returns an integer representing the minimum cost to connect all sticks.

    The cost to connect two sticks is the sum of their lengths.

    For example, given the list [3, 4, 5], the minimum cost to connect all sticks is 12 (3 + 4 + 5).

    The time complexity of this function is O(nlogn), where n is the number of sticks.
    The space complexity of this function is O(1), because the heap is built in place from the input list
    """
    if len(sticks) <= 1:
        return 0

    # Create a min heap from the list of sticks
    heapify(sticks)

    # Initialize the total cost to zero
    total_cost = 0

    # While there are more than one sticks left
    while len(sticks) > 1:
        # Extract the two smallest sticks from the heap
        first = heappop(sticks)
        second = heappop(sticks)
        # Calculate the cost to connect the two sticks
        cost = first + second
        # Add the cost to the total cost
        total_cost += cost
        # Push the connected stick back into the heap
        heappush(sticks, cost)

    # Return the total cost
    return total_cost


def connect_sticks_2(sticks: List[int]) -> int:
    """
    Calculates the minimum cost to connect all sticks.

    The function takes a list of integers, representing the length of each stick.
    It returns an integer representing the minimum cost to connect all sticks.

    The cost to connect two sticks is the sum of their lengths.

    For example, given the list [3, 4, 5], the minimum cost to connect all sticks is 12 (3 + 4 + 5).

    The time complexity of this function is O(nlogn), where n is the number of sticks.
    The space complexity of this function is O(1), because the heap is built in place from the input list
    """
    if len(sticks) <= 1:
        return 0

    nodes: List[HeapNode] = []
    for stick in sticks:
        node = HeapNode(stick)
        nodes.append(node)

    # Create a min heap from the list of sticks
    min_heap = MinHeap(nodes)

    # Initialize the total cost to zero
    total_cost = 0

    # While there are more than one sticks left
    while len(min_heap) > 1:
        # Extract the two smallest sticks from the heap
        first = min_heap.remove_min()
        second = min_heap.remove_min()
        # Calculate the cost to connect the two sticks
        cost = first.data + second.data
        # Add the cost to the total cost
        total_cost += cost
        # Push the connected stick back into the heap
        min_heap.insert(cost)

    # Return the total cost
    return total_cost
