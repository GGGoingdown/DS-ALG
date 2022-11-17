package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type MySlice struct {
	dataslice []int
	datamap   map[int]int
	length    int
}

func NewMySlice(s []int) *MySlice {
	my_s := new(MySlice)
	my_s.datamap = make(map[int]int)

	for idx, val := range s {

		my_s.dataslice = append(my_s.dataslice, val)
		my_s.datamap[val] = idx
		my_s.length++
	}

	return my_s
}

func (mySlice *MySlice) Index(val int) int {
	result, exist := mySlice.datamap[val]
	if !exist {
		panic("value not found")
	}
	return result
}

func (mySLice *MySlice) Value(idx int) int {
	if idx >= mySLice.length {
		panic("out of index")
	}
	return mySLice.dataslice[idx]
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

	if mid+1 >= len(preoder) {
		return root
	}

	root.Left = BuildTree(preoder[1:mid+1], inorder[:mid])
	root.Right = BuildTree(preoder[mid+1:], inorder[mid+1:])

	return root

}

func newArray() *[]int {
	a := &[]int{1, 2, 3}
	fmt.Printf("In func %p\n", &a)
	return a
}

func Preorder(root *TreeNode) {
	if root == nil {
		return
	}
	fmt.Println(root.Val)
	Preorder(root.Left)
	Preorder(root.Right)
}

// func main() {
// 	s := []int{2, 3, 5, 7, 11, 13}
// 	printSlice(s)

// 	// Slice the slice to give it zero length.
// 	s = s[:0]
// 	printSlice(s)

// 	// Extend its length.
// 	s = s[:4]
// 	printSlice(s)

// 	// Drop its first two values.
// 	s = s[2:]
// 	printSlice(s)
// }

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func main() {
	//	preorder := []int{3, 9, 20, 15, 7}
	// inorder := []int{9, 3, 15, 20, 7}

	// inorder := []int{9, 3, 15, 20, 7}
	// tree := BuildTree(preorder, inorder)
	// Preorder(tree)
	// a := newArray()
	// fmt.Printf("Out of func %p", &a)

	// fmt.Println(preorder[5:])

	// s := []int{2, 3, 5, 7, 11, 13}
	// printSlice(s)

	// // Slice the slice to give it zero length.
	// s = s[:0]
	// printSlice(s)

	// // Extend its length.
	// s = s[:4]
	// printSlice(s)

	// // Drop its first two values.
	// s = s[2:]
	// printSlice(s)

	a := make([]int, 3, 5)
	b := make([]int, 1, 2)
	copy_len := copy(b, a)
	fmt.Println(copy_len)
	printSlice(b)
	// a = append(a, []int{2:5}...)
	// printSlice(a)
}
