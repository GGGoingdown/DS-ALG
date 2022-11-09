package main

import (
	"fmt"
	"log"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}

	switch {
	case val < root.Val:
		return searchBST(root.Left, val)
	case val > root.Val:
		return searchBST(root.Right, val)
	case val == root.Val:
		return root
	default:
		return nil
	}
}

func ShowTree(tree *TreeNode) {
	if tree == nil {
		return
	}
	fmt.Println(tree.Val)
	ShowTree(tree.Left)
	ShowTree(tree.Right)
}

func main() {
	root := &TreeNode{
		Val: 4,
		Left: &TreeNode{
			Val: 2,
			Left: &TreeNode{
				Val: 1,
			},
			Right: &TreeNode{
				Val: 3,
			},
		},
		Right: &TreeNode{
			Val: 7,
		},
	}
	// ShowTree(root)
	tree := searchBST(root, 2)
	if tree == nil {
		log.Fatalln("Empty tree")
	}
	ShowTree(tree)
}
