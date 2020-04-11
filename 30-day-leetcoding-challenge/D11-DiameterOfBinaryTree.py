# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        
        def findDepth(node):
            if not node:
                return 0
            
            lft = findDepth(node.left)
            rgt = findDepth(node.right)
            
            # max path
            self.ans = max(self.ans, lft+rgt)
            print(self.ans)
            # max depth
            return max(lft, rgt) + 1
        
        findDepth(root)
        return self.ans
            