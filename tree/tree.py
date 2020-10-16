# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = ri# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Source: 102 Level order


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levelOrder = {}

        def helper(root, level):
            # Technique: BFS
            if root == None:
                return
            else:
                levelOrder[level] = levelOrder.get(level, []) + [root.val]
                helper(root.left, level + 1)
                helper(root.right, level + 1)

        helper(root, 0)
        return levelOrder.values()


# Source: 104 Max depth
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Technique: BFS
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
