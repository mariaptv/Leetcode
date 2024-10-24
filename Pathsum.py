#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
#A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False
        if root.val == targetSum and not root.left and not root.right:
            return True
        targetSum -= root.val

        return self.hasPathSum(self, root.left, targetSum) or self.hasPathSum(self, root.right,targetSum)
