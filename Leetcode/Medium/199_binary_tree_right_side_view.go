package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type node struct {
	*TreeNode
	level int
}

func RightSideView(root *TreeNode) []int {
	if root == nil {
		return nil
	}

	result := make([]int, 0)
	queue := []node{{root, 0}}
	level := 0

	for len(queue) > 0 {
		head := queue[0]
		queue = queue[1:]
		if head.level == level {
			result = append(result, head.Val)
			level++
		}
		if head.Right != nil {
			queue = append(queue, node{head.Right, head.level + 1})
		}
		if head.Left != nil {
			queue = append(queue, node{head.Left, head.level + 1})
		}
	}

	return result
}

func main() {
	root := &TreeNode{Val: 2, Left: &TreeNode{Val: 1}}
	result := RightSideView(root)
	fmt.Println(result)
}
