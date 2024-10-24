# Definition for a binary tree node.
from itertools import filterfalse


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree(object):

    def __init__(self, root= None):
        self.root = root

    def insert(self, value):
        new = TreeNode(value)
        if self.root is None:
            self.root = TreeNode(value)
        else:
            play = True

            current = self.root
            while play:
                if self.root.val < value:
                    if current.left is None:
                        current.left =new
                        play = False
                    else:
                        current = current.left
                elif self.root.val > value:
                    if current.right is None:
                        current.right = new
                        play = False
                    else:
                        current = current.right

    def lookup(self, value):
        current = self.root
        if current is None:
            return None

        play = True
        while play:
            if current.val == value:
                return current
            elif current.val < value:
                current = current.right
            elif current.val > value:
                current = current.left


    def print_tree(self, node):
        if node is not None:
            self.print_tree(node.left)
            print(node.val)
            self.print_tree(node.right)


    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """
        results = []
        def inorder(root, path, results):
            if root.left is None and root.right is None:
                results.append(root.val)
                return

            if root.left:
                return inorder(root.left, path + "->" + str(root.left.val), results)

            if root.right:
                return inorder(root.right, path + "->" + str(root.right.val), results)

        return inorder(root, str(root.val), results)






new = BinaryTree()
new.insert(1)
new.insert(2)
new.insert(3)
new.print_tree(new.root)




