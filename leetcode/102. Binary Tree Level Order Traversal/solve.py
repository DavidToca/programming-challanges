# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class QueueElement:
    node = None
    level = None

    def __init__(self, node, level):
        self.node = node
        self.level = level

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = []
        queue.append(QueueElement(root, 0))

        response = []
        while(queue):
            current_item = queue.pop(0)
            if len(response) == current_item.level:
                response.append([])    
            response[current_item.level].append(current_item.node.val)
            if current_item.node.left:
                queue.append(QueueElement(current_item.node.left, current_item.level+1))
            if current_item.node.right:
                queue.append(QueueElement(current_item.node.right, current_item.level+1))

        return response
        