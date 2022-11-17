package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func BuildTree(preoder, inorder []int) *TreeNode {
	if len(preoder) <= 0 || len(inorder) <= 0 {
		return nil
	}

	root := &TreeNode{Val: preoder[0]}
	mid := 0
	for idx, val := range inorder {
		if val == preoder[0] {
			mid = idx
			break
		}
	}

	root.Left = BuildTree(preoder[1:mid+1], inorder[:mid])
	root.Right = BuildTree(preoder[mid+1:], inorder[mid+1:])

	return root

}

func Preorder(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Println(root.Val)
	Preorder(root.Left)
	Preorder(root.Right)
}

func main() {
	// preorder := []int{3, 9, 20, 15, 7}
	// inorder := []int{9, 3, 15, 20, 7}

	// result := BuildTree(preorder, inorder)
	// Preorder(result)

	// Note : 切Slice的一些注意事項
	// a := []int{1, 2, 3} // len(a)==3 cap(a)==3
	// fmt.Println(a[3:]) // 如果起始位置為len + 1 則result -> []
	// fmt.Println(a[3:4]) // slice bounds out of range [:4] with capacity 3
}
