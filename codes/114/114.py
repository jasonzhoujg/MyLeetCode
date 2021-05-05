# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def flatten2(node):
            if node:
                flatten2(node.left)
                cur_right = node.right
                node.right = node.left
                node.left = None
                while node.right:node = node.right
                node.right = cur_right
                flatten2(node.right)
                
            
                
        flatten2(root)
        
