# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    # Fastest
    def isValidBST(self, root, floor = float('-inf'), ceil = float('inf')):
        if not root: return True
        return root.val > floor and root.val < ceil and self.isValidBST(root.left, floor, min(ceil, root.val)) and self.isValidBST(root.right, max(floor, root.val), ceil)
    
    # Slow (helpers)
    def lessThanNode(self, root, val):
        if not root: return True
        return root.val < val and self.lessThanNode(root.left, val) and self.lessThanNode(root.right, val)
    
    def greaterThanNode(self, root, val):
        if not root: return True
        return root.val > val and self.greaterThanNode(root.left, val) and self.greaterThanNode(root.right, val)
        
    def isValidBSTSlow(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        return self.lessThanNode(root.left, root.val) and self.greaterThanNode(root.right, root.val) and self.isValidBST(root.left) and self.isValidBST(root.right)
        