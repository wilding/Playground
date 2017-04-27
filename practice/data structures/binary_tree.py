class Node(object):
    """docstring for Node class"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    """docstring for BinaryTree class"""
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        output = ""
        traversal = self.preorder_print(self.root, [])
        for value in traversal:
            output += str(value) + "-"
        output = output[:-1]
        return output

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            traversal.append(start.value)
            if start.left:
                traversal = self.preorder_print(start.left, traversal)
            if start.right:
                traversal = self.preorder_print(start.right, traversal)
        return traversal


class BST(object):
    """docstring for BST class"""
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """inserts a new value into the BST
        at the appropriate position"""
        self.bst_insert(self.root, new_val)
        pass

    def search(self, find_val):
        """Return True if the given value is in
        the BST, False otherwise"""
        return self.bst_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        output = ""
        traversal = self.inorder_print(self.root, [])
        for value in traversal:
            output += str(value) + "-"
        output = output[:-1]
        return output

    def bst_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution
        with logarithmic efficiency"""
        if start:
            if find_val == start.value:
                return True
            elif find_val < start.value:
                return self.bst_search(start.left, find_val)
            elif find_val > start.value:
                return self.bst_search(start.right, find_val)
        return False

    def bst_insert(self, start, new_val):
        """Helper method - use this to create a
        recursive insert solution"""
        if start:
            if new_val < start.value:
                if start.left:
                    self.bst_insert(start.left, new_val)
                else:
                    start.left = Node(new_val)
            if new_val > start.value:
                if start.right:
                    self.bst_insert(start.right, new_val)
                else:
                    start.right = Node(new_val)
        pass

    def inorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        if start:
            if start.left:
                traversal = self.inorder_print(start.left, traversal)
            traversal.append(start.value)
            if start.right:
                traversal = self.inorder_print(start.right, traversal)
        return traversal
