from typing import Dict

from design_patterns.all_o_one.node import Node


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.previous = self.head
        self.key_map: Dict[str, Node] = dict()

    def inc(self, key: str) -> None:
        if key in self.key_map:
            node = self.key_map[key]
            freq = node.freq
            node.keys.remove(key)

            next_node = node.next
            if next_node == self.tail or next_node.freq != freq + 1:
                # Create a new node if next node does not exist or freq is not freq + 1
                new_node = Node(freq + 1)
                new_node.keys.add(key)
                new_node.previous = node
                new_node.next = next_node
                node.next = new_node
                next_node.prev = new_node
                self.key_map[key] = new_node
            else:
                # Increment the existing next node
                next_node.keys.add(key)
                self.key_map[key] = next_node

            # remove the current node if it has no keys left
            if not node.keys:
                self.remove_node(node)
        else:
            # key does not exist
            first_node = self.head.next
            if first_node == self.tail or first_node.freq > 1:
                # create a new node
                new_node = Node(1)
                new_node.keys.add(key)
                new_node.previous = self.head
                new_node.next = first_node
                self.head.next = new_node
                first_node.prev = new_node
                self.key_map[key] = new_node
            else:
                first_node.keys.add(key)
                self.key_map[key] = first_node

    def dec(self, key: str) -> None:
        if key not in self.key_map:
            return

        node = self.key_map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            # remove the key from the map if freq is 1, since decreasing it will result in 0
            del self.key_map[key]
        else:
            prev_node = node.previous
            if prev_node == self.head or prev_node.freq != freq - 1:
                # create a new node if the previous node does not exist or freq is not freq - 1
                new_node = Node(freq - 1)
                new_node.keys.add(key)
                new_node.previous = prev_node
                new_node.next = node
                prev_node.next = new_node
                node.previous = new_node
                self.key_map[key] = new_node
            else:
                prev_node.keys.add(key)
                self.key_map[key] = prev_node

        if not node.keys:
            self.remove_node(node)

    def get_max_key(self) -> str:
        if self.tail.previous == self.head:
            # No keys exist
            return ""
        # Return one of the keys from the tail's previous node
        return next(iter(self.tail.previous.keys))

    def get_min_key(self) -> str:
        if self.head.next == self.tail:
            # No keys exist
            return ""
        return next(iter(self.head.next.keys))

    @staticmethod
    def remove_node(node: Node):
        prev_node = node.previous
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
