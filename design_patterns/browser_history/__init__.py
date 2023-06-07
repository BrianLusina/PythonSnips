from datastructures.linked_lists.doubly_linked_list import DoubleNode


class BrowserHistory:
    """
    Implementation of a Browser history using DoublyLinkedList. This does not actually use the list, but it uses nodes
    with 2 pointers which build up to the LinkedList.

    The assumption made here is that if the same URL is visited, it creates a history item. In the real world, this is
    not the case
    """

    def __init__(self, homepage: str):
        self.current_node = DoubleNode(homepage)

    def visit(self, url: str) -> None:
        """
        Visits url from the current page. It clears up all the forward history.
        @param url: URL to visit
        """
        node = DoubleNode(url)
        current = self.current_node

        # check if there is a node after current node
        if not current.next:
            node.previous = current
            self.current_node = node
            current.next = node
            return
        else:
            # if there is, we clear all forward history
            current.next = node
            node.next = None
            node.previous = self.current_node
            self.current_node = node

    def back(self, steps: int) -> str:
        """
        Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x
        steps. Return the current url after moving back in history at most steps
        @param steps: Number of steps to move back
        @return: Current url after moving back in history
        """
        current = self.current_node
        for _ in range(steps):
            if current.previous:
                current = current.previous
        self.current_node = current
        return current.data

    def forward(self, steps: int) -> str:
        """
        Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward
        only x steps. Return the current url after forwarding in history at most steps.
        @param steps: Number of steps to move forward
        @return: current url after moving forward in history
        """
        current = self.current_node
        for _ in range(steps):
            if current.next:
                current = current.next
        self.current_node = current
        return current.data
