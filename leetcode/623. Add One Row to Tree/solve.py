# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        
        d -=2

        queue = []

        queue.append( (root, 0))

        while(queue):
            node, level = queue.pop(0)
            if level == d:
                newleft = TreeNode(v)
                newright = TreeNode(v)
                if node.left:
                    newleft.left = node.left
                if node.right:
                    newright.right = node.right
                node.left = newleft
                node.right = newright
            elif level+1 <=d:
                if node.left:
                    queue.append((node.left, level+1))
                if node.right:
                    queue.append((node.right, level+1))

        return root
