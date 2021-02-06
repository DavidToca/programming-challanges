# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    current_level = 0
    response = []

    def solve(self, node, level):
        if self.current_level == level:
            self.response.append(node.val)
            self.current_level = level + 1
        if node.right:
            self.solve(node.right, level+1)

        if node.left:
            self.solve(node.left, level+1)

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.response = []
        self.current_level=0
        self.solve(root, 0)

        return self.response