# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

        
class QueueItem:
    def __init__(self, node, level):
        self.node = node
        self.level = level

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = []
        response = []   
        queue.append(QueueItem(root, 0))

        while(queue):
            current_item = queue.pop(0)
            
            level = current_item.level
            node = current_item.node

            if(len(response) == level):
                response.append([current_item.node.val])
            else:
                response[level].append(node.val)
            
            if node.left:
                queue.append(QueueItem(node.left, level+1))
            if node.right:
                queue.append(QueueItem(node.right, level+1))
        
        response = map(lambda x: sum(x)/len(x), response)
        
        return response
