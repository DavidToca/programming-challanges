# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        queue = deque()
        response = []
        pre_root = TreeNode(left=root)
        queue.append(pre_root)
        voyage_index = 0
        while queue:
            current_node = queue.pop()
            voyage_sub_len = 0
            if current_node.left:
                voyage_sub_len += 1
                queue.append(current_node.left)
            if current_node.right:
                voyage_sub_len += 1
                queue.append(current_node.right)

            if current_node.left:
                if (
                    current_node.left.val
                    not in voyage[voyage_index : voyage_index + voyage_sub_len]
                ):
                    return [-1]
            if current_node.right:
                if (
                    current_node.right.val
                    not in voyage[voyage_index : voyage_index + voyage_sub_len]
                ):
                    return [-1]

            if current_node.right and current_node.left:
                if current_node.left.val != voyage[voyage_index]:
                    response.append(current_node.val)
                    current_node.left, current_node.right = (
                        current_node.right,
                        current_node.left,
                    )
                voyage_index += 2
            elif current_node.right:
                if current_node.right.val != voyage[voyage_index]:
                    response.append(current_node.val)
                    current_node.left, current_node.right = (
                        current_node.right,
                        current_node.left,
                    )
                voyage_index += 1
            elif current_node.left:
                if current_node.left.val != voyage[voyage_index]:
                    response.append(current_node.val)
                    current_node.left, current_node.right = (
                        current_node.right,
                        current_node.left,
                    )
                voyage_index += 1

        return response
