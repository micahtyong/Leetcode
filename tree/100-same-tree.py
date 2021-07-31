# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q
        
    def isSameTreeVerbose(self, p, q): # fast!!
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_none, q_none = p == None, q == None
        if p_none and q_none: 
            return True
        if (p_none and not q_none) or (q_none and not p_none) or (not p.val == q.val):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)