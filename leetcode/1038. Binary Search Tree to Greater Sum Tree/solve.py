# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, node: TreeNode):
        if not node:
            return
        if node.right:
            self.solve(node.right)
        self.total += node.val
        node.val = self.total
        
        if node.left:
            self.solve(node.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.total = 0
        self.solve(root)
        
        return root
