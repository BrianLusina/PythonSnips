from queue import Queue


class BinaryTreeNode(object):
    """
    Binary tree node class which will implement Binary tree
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert_node(self, value):
        """
        Inserts a node using a Binary Search approach, where every value insert will be inserted to either the left or right based on whether
        the value is greater than the root node. if the value is greater than the root node, then the value will be inserted to the right. If 
        the value is less than the root node, then the insertion will be to the left of the root Node. This will apply for subsequent children of the
        root node and will be recursive.
        Assumption made here is that value insertions are int type
        :param: value, value to insert
        """
        # if the value being inserted is less than the current value and the left node exists
        if value < self.value and self.left:
            self.left.insert_node(value)

        elif value <= self.value:
            self.left = BinaryTreeNode(value)

        elif value > self.value and self.right:
            self.right.insert_node(value)

        else:
            self.right_child = BinaryTreeNode(value)

    def search_node(self, value):
        """
        Searches for the given value in a binary search tree. If the value exists in the tree, then True is returned, else false
        :param value the value to search for
        :rtype: bool
        """
        # check if the value is less than the root node and recursively check on the left of the tree
        if value < self.value and self.left:
            return self.left.search_node(value)
        # check if the current value is greater than the root node and that the right node exist, then proceed to the right
        # to perform the search
        if value > self.value and self.right:
            return self.right.search_node(value)
        # if the root node is equal to the value, then return True if they are equal
        return value == self.value
    
    def delete_node(self, value, parent):
        """
        Deletes a node from the tree if present and return result of deletion, True if the delete was successful and False if the deletion was
        unsuccessful, 
        :param value Value we want to delete from the tree
        :param parent
        :rtype: bool True if the deletion was a success, false otherwise
        """
        # recursively check that the value is less than the current node value and that there is a left 
        if value < self.value and self.left:
            return self.delete_node(value, self)

        if value < self.value:
            return False

        # recursively check that the value is greater than the current node value and that there is a right
        if value > self.value and self.right:
            return self.delete_node(value, self)

        if value > self.value:
            return False
    
        else:
            if self.left is None and self.right is None and self == parent.left:
                parent.left = None
                self.clear_node()
            
            elif self.left is None and self.right is None and self == parent.right:
                parent.right = None
                self.clear_node()
            
            elif self.left and self.right is None and self == parent.left:
                parent.left = self.left
                self.clear_node()
         
            elif self.left and self.right is None and self == parent.right:
                parent.right = self.left
                self.clear_node()
        
            elif self.right and self.left is None and self == parent.left:
                parent.left = self.right
                self.clear_node()
    
            elif self.right and self.left is None and self == parent.right:
                parent.right = self.right
                self.clear_node()
            
            else:
                self.value = self.right.find_minimum_value()
                self.right.delete_node(self.value, self)

        return True
    
    def clear_node(self):
        """
        Clears the node and sets the values to None
        """
        self.value = None
        self.left = None
        self.right = None
    
    def find_minimum_value(self):
        """
        Find the minimum value by going way down to the left, if we can not find anymore nodes, we have reached the end
        """
        if self.left:
            return self.left.find_minimum_value()
        else:
            return self.value



    def insert_left(self, value):
        """
        Inserts a new value(node) to the left of the current node and return the newly created node
        :param value the value to insert into the new node
        :rtype: BinaryTreeNode
        """
        if self.left is None:
            self.left = BinaryTreeNode(value)
        else:
            # create a new node
            new_node = BinaryTreeNode(value)
            # set the current left child node to become the left of the new node
            new_node.left = self.left
            # set the new left node of the current node to be the newly created node
            self.left = new_node
        return self.left

    def insert_right(self, value):
        """
        Inserts a value to the right of the current node. This will check if the current node has a right child already
        and insert this node as the new right node of the current node and move the previous node (if not None) to become the
        new right node of the newly created node.
        This will then return the newly inserted node value
        :param value value used to create a new node
        :rtype: BinaryTreeNode
        """
        if self.right is None:
            self.right = BinaryTreeNode(value)
        else:
            new_node = BinaryTreeNode(value)
            new_node.right = self.right
            self.right = new_node
        return self.right

    def pre_order(self):
        """
        Type of Depth First Traversal (DFS) for binary trees which will start at root node and proceed to the left value and print it until
        it reaches the leaf(node with no more children) and then backtrack to the node and check if the current node has a right child and print
        it. This will continue until all nodes have been tracked and printed.
        """
        print("Value: {}".format(self.value))

        if self.left:
            self.left.pre_order()

        if self.right:
            self.right.pre_order()

    def in_order(self):
        """
        Another type of Depth First Search (DFS) that traverses the tree from the left to middle to right of the tree. This type of search will
        begin at the left node and check if that node has a left child and continually check until that left node is a leaf(has no children)
        and will then print its value and "bubble up" back to the current node and execute that (in this case print it) and then print the right
        node. The same procedure is executed for the right side of the tree.
        """
        if self.left:
            self.left.in_order()

        print("Value: {}".format(self.value))

        if self.right:
            self.right.in_order()

    def post_order(self):
        """
        Post order is a another kind of Depth First Search (DFS) algorithm that will search the tree from the left first, then the right first before
        then proceeding to the middle last, in this case, the root node
        """
        if self.left:
            self.left.post_order()

        if self.right:
            self.right.post_order()

        print("Value: {}".format(self.value))

    def breadth_first_search(self):
        """
        Performs a breadth first search through a Binary Tree
        This will traverse the tree level by level and depth by depth. Using a Queue to put elements into the queue
        """
        queue = Queue()

        # start off by adding the root node
        queue.put(self)

        # while the queue is not empty, we want to traverse the tree and add elements to the queue,
        while not queue.empty():
            current_node = queue.get()
            print("value: {}".format(self.value))

            if current_node.left:
                queue.put(current_node.left)

            if current_node.right:
                queue.put(current_node.right)






