from typing import List, Optional
from datastructures.stacks import Stack
from datastructures.trees.nary.node import NAryNode


def count_number_of_underpaid_managers(root: Optional[NAryNode]) -> int:
    if not root:
        return 0

    def traverse_direct_and_indirect_nodes(current: NAryNode) -> List[int]:
        """Perform a preorder traversal of the node's children from left to right in a sequence
        Args:
            current(Node): current node to traverse
        Returns:
            list: list of child and grand child nodes
        """

        # use to maintain the list of nodes to traverse, resulting in an O(n) operation where n is the number of nodes
        nodes_to_traverse = Stack()

        # add the current node to traverse
        nodes_to_traverse.push(current)

        # keep track of the node children data, that is, our visited nodes
        visited_nodes_data = []

        while not nodes_to_traverse.is_empty():
            # flag denotes whether all the child nodes have been visited
            flag = False

            parent = nodes_to_traverse.peek()

            # if top of the stack is a leaf node, that is, has no children, then remove it from the stack
            if len(parent.children) == 0:
                nodes_to_traverse.pop()

            # a)As soon as an unvisited child is
            # found(left to right sequence),
            # Push it to Stack and Store it in
            # Auxiliary List(Marked Visited)
            # Start Again from Case-1, to explore
            # this newly visited child
            for child_node in parent.children:
                if child_node not in visited_nodes_data:
                    flag = True
                    nodes_to_traverse.push(child_node)
                    visited_nodes_data.append(child_node.data)
                    break
                    # b)If all Child nodes from left to right
                    # of a Parent have been visited
                    # then remove the parent from the stack.

            if not flag:
                if not nodes_to_traverse.is_empty():
                    nodes_to_traverse.pop()

        return visited_nodes_data

    stack = Stack()
    stack.push(root)
    manager_count = 0

    while not stack.is_empty():
        node = stack.pop()

        direct_and_indirect_salaries = traverse_direct_and_indirect_nodes(node)

        if direct_and_indirect_salaries:
            total_child_salaries = sum(direct_and_indirect_salaries)
            average_salaries = total_child_salaries / len(direct_and_indirect_salaries)

            if node.data < average_salaries:
                manager_count += 1

        for child in node.children:
            stack.push(child)

    return manager_count
