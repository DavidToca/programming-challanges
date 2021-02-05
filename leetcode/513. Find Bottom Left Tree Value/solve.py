# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    response = -1
    deep = -1
    
    def find_lefmost(self, root: TreeNode, deep) -> int:
        if root == None:
            return
        if deep > self.deep:
            self.deep = deep
            self.response = root.val


        self.find_lefmost(root.left, deep+1)
        self.find_lefmost(root.right, deep+1)
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.find_lefmost(root, 0)
        return self.response
        
        
        