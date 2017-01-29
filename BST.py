""" Binary Search Tree Implementation """


class Node(object):
    """Node of a Binary Tree"""

    def __init__(self, value, left, right):
        super(Node, self).__init__()
        self.value = value
        self.left = left
        self.right = right
        self.parent = None
        self.height = 0

    def __str__(self):
        return str(self.value)


class BST(object):
    """ Class that defines the Binary Search Tree"""

    def __init__(self, root_value):
        super(BST, self).__init__()
        self.root = Node(root_value, None, None)
        self.height = self.root.height

    def insert(self, value):
        """Insert values in to the binary tree"""
        curr_node = self.root
        prev_node = None

        while curr_node:
            if curr_node.value > value:
                prev_node = curr_node
                curr_node = curr_node.left
            elif curr_node.value <= value:
                prev_node = curr_node
                curr_node = curr_node.right

        if prev_node.value > value:
            prev_node.left = Node(value, None, None)
            prev_node.left.parent = prev_node
            BST._update_height(prev_node.left)
            return prev_node.left
        elif prev_node.value <= value:
            prev_node.right = Node(value, None, None)
            prev_node.right.parent = prev_node
            BST._update_height(prev_node.right)
            return prev_node.right

    def find_min(self):
        """Find the Node with minimum value and return it
           @:return Node with minimum value"""
        curr_node = self.root
        while curr_node.left:
            curr_node = curr_node.left

        return curr_node

    def find_max(self):
        """Find the node with maximum value
        @:return node with maximum value"""
        curr_node = self.root
        while curr_node.right:
            curr_node = curr_node.right

        return curr_node

    @staticmethod
    def _update_height(leaf_node):
        """After each insertion this function is called to update the height of each node in the tree"""
        node = leaf_node
        get_height_node = lambda node: -1 if node is None else node.height
        while node:
            node.height = max(get_height_node(node.left), get_height_node(node.right)) + 1
            node = node.parent

    @staticmethod
    def _in_order(node):
        """ Private Static Method that traverses the tree in In-oder"""
        if node:
            BST._in_order(node.left)
        else:
            return
        print(node.value, 'height= ' + str(node.height))
        if node:
            BST._in_order(node.right)
        else:
            return

    def in_order(self):
        """ In-order traversal left,root,right"""
        BST._in_order(self.root)

    def search(self, key):
        """Search the binary tree for a Key
        @:return Node if key in tree, else none
        @:key The value to be searched for in the tree """
        curr = self.root
        while curr:
            if curr.value > key:
                curr = curr.left
            elif curr.value == key:
                return curr
            else:
                curr = curr.right

    @staticmethod
    def _predecessor(node):
        """Returns the predecessor for a given node"""
        left_tree = node.left
        while left_tree.right:
            left_tree = left_tree.right

        return left_tree

    def _delete(self, node_to_del):
        """Implementation of deleting a node of Binary tree """
        left_child = False
        root_node = False

        if node_to_del.parent is None:
            root_node = True
        elif node_to_del == node_to_del.parent.left:
            left_child = True

        if node_to_del.left and node_to_del.right:
            """ Case 1: node_to_del has both left and right child
                Find the predecessor of the node.
                Swap the predecessor value with the node we delete  .
                delete the predecessor.
                Note: Deleting predecessor will always be a Case 2 or Case 3
            """
            predecessor = BST._predecessor(node_to_del)
            node_to_del.value, predecessor.value = predecessor.value, node_to_del.value
            self._delete(predecessor)

        elif node_to_del.left or node_to_del.right:
            # Case 2: node_to_del has either a left child or right child
            if root_node:
                self.root = node_to_del.left or node_to_del.right
            elif left_child:
                node_to_del.parent.left = node_to_del.left or node_to_del.right
            else:
                node_to_del.parent.right = node_to_del.left or node_to_del.right
            node_to_del.left = None
            node_to_del.right = None
            BST._update_height(node_to_del.parent)
        else:
            # Case 3: node_to_del has no children
            if left_child:
                node_to_del.parent.left = None
            else:
                node_to_del.parent.right = None
            BST._update_height(node_to_del.parent)

    def delete(self, key):
        """Delete the node with a given key"""
        node_to_del = self.search(key)
        self._delete(node_to_del)

        if node_to_del is None:
            print("No Node with key: " + str(key))
            return

    def __str__(self):
        """Gives an ASCII diagram of the Tree, This function taken from
        https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/
        6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/bst.py"""

        if self.root is None:
            return '<empty tree>'

        def recurse(node):
            if node is None:
                return [], 0, 0
            label = str(node.value)
            left_lines, left_pos, left_width = recurse(node.left)
            right_lines, right_pos, right_width = recurse(node.right)
            middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
            pos = left_pos + middle // 2
            width = left_pos + middle + right_width - right_pos
            while len(left_lines) < len(right_lines):
                left_lines.append(' ' * left_width)
            while len(right_lines) < len(left_lines):
                right_lines.append(' ' * right_width)
            if (middle - len(label)) % 2 == 1 and node.parent is not None and \
                    node is node.parent.left and len(label) < middle:
                label += '.'
            label = label.center(middle, '.')
            if label[0] == '.':
                label = ' ' + label[1:]
            if label[-1] == '.':
                label = label[:-1] + ' '
            lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                     ' ' * left_pos + '/' + ' ' * (middle - 2) +
                     '\\' + ' ' * (right_width - right_pos)] + \
                    [left_line + ' ' * (width - left_width - right_width) +
                     right_line
                     for left_line, right_line in zip(left_lines, right_lines)]
            return lines, pos, width

        return '\n'.join(recurse(self.root)[0])

if __name__ == '__main__':
    # tree = BST(20)
    # tree.insert(10)
    # tree.insert(40)
    # tree.insert(18)
    # tree.insert(999)
    # tree.insert(45)
    # tree.insert(15)
    # tree.insert(5)
    # tree.insert(6)
    # tree.insert(4)

    tree = BST(10)
    tree.insert(9)
    tree.insert(8)
    tree.insert(7)
    tree.insert(6)
    tree.insert(5)
    tree.insert(4)
    tree.insert(3)
    tree.insert(2)
    tree.insert(1)

    print(tree, end="\n\n")
    tree.in_order()

    print(tree.search(100))
    print(tree.find_min())
    print(tree.find_max())

    tree.delete(1)
    print(tree, end="\n\n")
    tree.in_order()
