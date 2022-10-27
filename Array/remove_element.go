/*
LeetCode: https://leetcode.com/problems/remove-element/
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

*/
package main

import "fmt"

func RemoveElement(nums []int, val int) int {
	slow, fast := len(nums)-1, len(nums)-1
	for fast >= 0 {
		if nums[fast] == val{
			nums[slow], nums[fast] = nums[fast], nums[slow]
			slow--
		}
		fast--
	}
	return slow + 1
}

func main() {
	nums := []int{0,1,2,2,3,0,4,2}
	val := 2
	result := RemoveElement(nums, val)
	fmt.Printf("Result: %v", result)
}
