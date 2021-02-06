/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func solution(node *TreeNode, level int, response []int) []int {
	if len(response) == level {
		response = append(response, node.Val)
	}
	if node.Right != nil {
		response = solution(node.Right, level+1, response)
	}
	if node.Left != nil {
		response = solution(node.Left, level+1, response)
	}
	return response

}

func rightSideView(root *TreeNode) []int {
	response := make([]int, 0)
    if root == nil {
		return response
	}
	response = solution(root, 0, response)

	return response
}