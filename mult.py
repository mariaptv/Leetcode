# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: Optional[TreeNode]
        :type low: int
        :type high: int
        :rtype: int
        """
        sum = 0

        def order(root, low, high):

            if root.val < low and root.val > high:
                self.sum += root.val

            if root.left is not None:
                order(root.left, low, high)

            if root.right is not None:
                order(root.left, low, high)

            return

        order(root, low, high)

        return sum