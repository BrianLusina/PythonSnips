from .node import BTreeNode, T


class BTree:
    def __init__(self, degree: int):
        self.root = BTreeNode(leaf=True)
        self.degree = degree

    def insert(self, key: T):
        """
        Insert a key or value into the tree
        Args:
            key (T): Key to insert
        """
        root = self.root
        if len(root.keys) == (2 * self.degree) - 1:
            b_node = BTreeNode()
            self.root = b_node
            b_node.children.append(root)
            self.__split_child(b_node, 0)
            self.__insert_non_full(b_node, key)
        else:
            self.__insert_non_full(root, key)

    # Delete a node
    def delete(self, key: T) -> BTreeNode:
        """
        Delete a node from the tree based on the key and return it
        @param key: key to delete.
        @return: BTreeNode
        """

        def delete_helper(node: BTreeNode, k: T):
            t = self.degree
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1
            if node.leaf:
                if i < len(node.keys) and node.keys[i][0] == key[0]:
                    node.keys.pop(i)
                    return
                return

            if i < len(node.keys) and node.keys[i][0] == k[0]:
                return self.delete_internal_node(node, k, i)
            elif len(node.children[i].keys) >= t:
                delete_helper(node.children[i], k)
            else:
                if i != 0 and i + 2 < len(node.children):
                    if len(node.children[i - 1].keys) >= t:
                        self.delete_sibling(node, i, i - 1)
                    elif len(node.children[i + 1].keys) >= t:
                        self.delete_sibling(node, i, i + 1)
                    else:
                        self.delete_merge(node, i, i + 1)
                elif i == 0:
                    if len(x.child[i + 1].keys) >= t:
                        self.delete_sibling(node, i, i + 1)
                    else:
                        self.delete_merge(node, i, i + 1)
                elif i + 1 == len(node.children):
                    if len(node.children[i - 1].keys) >= t:
                        self.delete_sibling(node, i, i - 1)
                    else:
                        self.delete_merge(node, i, i - 1)
                self.delete(node.children[i], k)

        return delete_helper(node=self.root, k=key)

    # Delete internal node
    def delete_internal_node(self, x, k, i):
        t = self.degree
        if x.leaf:
            if x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
            return

        if len(x.child[i].keys) >= t:
            x.keys[i] = self.delete_predecessor(x.child[i])
            return
        elif len(x.child[i + 1].keys) >= t:
            x.keys[i] = self.delete_successor(x.child[i + 1])
            return
        else:
            self.delete_merge(x, i, i + 1)
            self.delete_internal_node(x.child[i], k, self.degree - 1)

    # Delete the predecessor
    def delete_predecessor(self, x):
        if x.leaf:
            return x.pop()
        n = len(x.keys) - 1
        if len(x.child[n].keys) >= self.degree:
            self.delete_sibling(x, n + 1, n)
        else:
            self.delete_merge(x, n, n + 1)
        self.delete_predecessor(x.child[n])

    # Delete the successor
    def delete_successor(self, x):
        if x.leaf:
            return x.keys.pop(0)
        if len(x.child[1].keys) >= self.degree:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        self.delete_successor(x.child[0])

    # Delete resolution
    def delete_merge(self, x, i, j):
        cnode = x.child[i]

        if j > i:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.child) > 0:
                    cnode.child.append(rsnode.child[k])
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child.pop())
            new = cnode
            x.keys.pop(i)
            x.child.pop(j)
        else:
            lsnode = x.child[j]
            lsnode.keys.append(x.keys[j])
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.child) > 0:
                    lsnode.child.append(cnode.child[i])
            if len(lsnode.child) > 0:
                lsnode.child.append(cnode.child.pop())
            new = lsnode
            x.keys.pop(j)
            x.child.pop(i)

        if x == self.root and len(x.keys) == 0:
            self.root = new

    # Delete the sibling
    def delete_sibling(self, x, i, j):
        cnode = x.child[i]
        if i < j:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            x.keys[i] = rsnode.keys[0]
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child[0])
                rsnode.child.pop(0)
            rsnode.keys.pop(0)
        else:
            lsnode = x.child[j]
            cnode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.child) > 0:
                cnode.child.insert(0, lsnode.child.pop())

    def __split_child(self, btree_node: BTreeNode, index: int):
        degree = self.degree

        child_at_index = btree_node.children[index]
        leaf_node = BTreeNode(leaf=child_at_index.leaf)

        btree_node.children.insert(index + 1, leaf_node)
        btree_node.add_key_at(key=child_at_index.keys[degree - 1], index=index)

        leaf_node.keys = child_at_index.keys[degree : (2 * degree) - 1]
        child_at_index.keys = child_at_index.keys[0 : degree - 1]

        if not child_at_index.leaf:
            leaf_node.children = child_at_index[degree : 2 * degree]
            child_at_index.children = child_at_index.children[0 : degree - 1]

    def __insert_non_full(self, btree_node: BTreeNode, k: T):
        i = len(btree_node.keys) - 1

        if btree_node.leaf:
            btree_node.keys.append((None, None))
            while i >= 0 and k < btree_node.keys[i][0]:
                btree_node.keys[i + 1] = btree_node.keys[i]
                i -= 1
            btree_node.keys[i + 1] = k
        else:
            while i >= 0 and k < btree_node.keys[i][0]:
                i -= 1
            i += 1

            if len(btree_node.children[i].keys) == (2 * self.degree) - 1:
                self.__split_child(btree_node, i)
                if k > btree_node.keys[i][0]:
                    i += 1

            self.__insert_non_full(btree_node.children[i], k)
