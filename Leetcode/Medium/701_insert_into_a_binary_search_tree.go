package main

import (
	"fmt"
	"log"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func InorderTree(tree *TreeNode) {
	if tree == nil {
		return
	}

	InorderTree(tree.Left)
	fmt.Printf("%d,", tree.Val)
	InorderTree(tree.Right)
}

func IsValidBST(tree *TreeNode) bool {
	if tree == nil {
		return true
	}

	return checkBST(tree, math.Inf(-1), math.Inf(1))

}

func InsertBST(tree *TreeNode, val int) *TreeNode {
	if tree == nil {
		return &TreeNode{Val: val}
	}

	if val < tree.Val {
		tree.Left = InsertBST(tree.Left, val)
	} else {
		tree.Right = InsertBST(tree.Right, val)
	}

	return tree

}

func FindMinNode(tree *TreeNode) *TreeNode {
	cur := tree
	for cur.Left != nil {
		cur = cur.Left
	}
	return cur
}

func RemoveBST(tree *TreeNode, val int) *TreeNode {
	if tree == nil {
		return nil
	}

	if val < tree.Val {
		tree.Left = RemoveBST(tree.Left, val)
	} else if val > tree.Val {
		tree.Right = RemoveBST(tree.Right, val)
	} else {
		if tree.Left == nil {
			return tree.Right
		} else if tree.Right == nil {
			return tree.Left
		} else {
			minNode := FindMinNode(tree.Right)
			tree.Val = minNode.Val
			tree.Right = RemoveBST(tree.Right, minNode.Val)
		}

	}

	return tree

}

func checkBST(tree *TreeNode, min, max float64) bool {
	if tree == nil {
		return true
	}

	//fmt.Printf("Value: %v. Range [%v_%v]\n", tree.Val, min, max)
	if float64(tree.Val) < min || float64(tree.Val) > max {
		return false
	}
	left_result := checkBST(tree.Left, min, float64(tree.Val))
	if !left_result {
		return false
	}
	right_result := checkBST(tree.Right, float64(tree.Val), max)
	if !right_result {
		return false
	}

	return true

}

func main() {
	tree1 := &TreeNode{
		Val: 40,
		Left: &TreeNode{
			Val:   20,
			Left:  &TreeNode{Val: 10},
			Right: &TreeNode{Val: 30, Left: &TreeNode{Val: 21}},
		},
		Right: &TreeNode{
			Val: 60,
			Left: &TreeNode{
				Val: 50,
			},
			Right: &TreeNode{
				Val: 70,
			},
		},
	}
	isValid1 := IsValidBST(tree1)
	if !isValid1 {
		log.Fatalln("Is not valid BST")
	}

	InorderTree(tree1)
	fmt.Printf("\n")
	tree1 = InsertBST(tree1, 25)
	isValid2 := IsValidBST(tree1)
	if !isValid2 {
		log.Fatalln("Is not valid BST")
	}
	InorderTree(tree1)
	fmt.Printf("\n")
	tree1 = RemoveBST(tree1, 40)
	isValid3 := IsValidBST(tree1)
	if !isValid3 {
		log.Fatalln("Is not valid BST")
	}
	InorderTree(tree1)
	fmt.Printf("\n")
}
