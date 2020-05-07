# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        def recurr(node, parent, level, val):
            if node:
                if node.val == val:
                    return parent, level
                
                return recurr(node.left, node, level + 1, val) or recurr(node.right, node, level + 1, val)
            
        parentX, levelX, parentY, levelY = recurr(root, None, 0, x) + recurr(root, None, 0, y)
        
        if parentX != parentY and levelX == levelY:
            return True
        else:
            return False
        