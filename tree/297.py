# Source: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        print("Tree looks like", root)
        code = []
        self.helper(root, code)
        return str(code)
        
    def helper(self, root, code): 
        if (root == None): 
            code.append(None)
        else:   
            code.append(root.val)
            self.helper(root.left, code)
            self.helper(root.right, code)

    def deserialize(self, data) -> TreeNode:
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        code = data.replace(']', '').replace('[', '').replace(' ', '').split(',')
        tree = self.d_helper(code)
        return tree
        
    def d_helper(self, code):
        if (len(code) == 0): # empty
            return 
        
        elem = code.pop(0)
        if (elem == 'None'):
            return None
        else:
            node = TreeNode(elem)
            node.left = self.d_helper(code)
            node.right = self.d_helper(code)
            return node
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))