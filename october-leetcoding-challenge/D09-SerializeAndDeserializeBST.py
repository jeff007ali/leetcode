# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        stack = []
        
        while root or stack:
            if root:
                res.append(str(root.val))
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        
        return ",".join(res)
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        
        data = list(map(int, data.split(",")))
        stack = []
        root = node = TreeNode(data[0])
        
        for n in data[1:]:
            if n < node.val:
                node.left = TreeNode(n)
                stack.append(node)
                node = node.left
            else:
                while stack and stack[-1].val < n:
                    node = stack.pop()
                    
                node.right = TreeNode(n)
                node = node .right
                
        return root
                
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans