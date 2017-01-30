from BST import BST


class AVL(BST):
    """Implements an AVL Tree"""
    def __init__(self, root_value):
        super(AVL, self).__init__(root_value)

    @staticmethod
    def _height_diff_children(node):
        get_height_node = lambda node: -1 if node is None else node.height
        return abs(get_height_node(node.left) - get_height_node(node.right))

    @staticmethod
    def _roatate_right(node):
        """Rotates the given node to left
          Example:
          ---------
          Rotate A to the Right
             A.                  B.
            / \   ------->      / \
           B   C               D  A
          / \                    / \
         D  E                   E   C
        """
        pass

    def _rotate_left(self):
        pass

    def insert(self, value, **kwargs):
        """Insert in to AVL Tree"""
        # First do a BST insertion
        inserted_node = super(AVL, self).insert(value)
        print(inserted_node)

        # Find violations as a result of the insert
        if inserted_node.parent is None:
            return

        curr_node = inserted_node.parent

        while curr_node:
            if AVL._height_diff_children(curr_node) <= 1:
                curr_node = curr_node.parent
            else:
                # Case 1: If the violated nodes
                #            Left Child is Left heavy: (or)
                #                   Rotate the violated Node Right
                #            Right Child is Right heavy:
                #                   Rotate the Violated Node Left
                print("Violation")
                break


    #def __str__(self):
    #    super(AVL, self).__str__()

if __name__ == '__main__':
    tree = AVL(1)
    tree.insert(2)
    tree.insert(3)
    print(tree)