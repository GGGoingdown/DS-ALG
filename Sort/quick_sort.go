package main

import (
	"fmt"
)

func quickSortHelper(ary []int, left, right int) {
	if left > right {
		return
	}
	pivot := ary[left]
	pos := right
	for i := right; i > left; i-- {
		if ary[i] > pivot {
			ary[i], ary[pos] = ary[pos], ary[i]
			pos--
		}
	}
	ary[left], ary[pos] = ary[pos], ary[left]
	quickSortHelper(ary, left, pos-1)
	quickSortHelper(ary, pos+1, right)
}

func QuickSort(ary []int) {
	if len(ary) == 1 {
		return
	}
	quickSortHelper(ary, 0, len(ary)-1)
}

func main() {
	ary := []int{10, 1, 7}
	fmt.Println("Before sorting", ary)
	QuickSort(ary)
	fmt.Println("After sorting", ary)
}
