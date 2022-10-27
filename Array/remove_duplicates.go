/*
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
*/

package main

import (
	"log"
)

func removeDuplicates(nums []int)int{
	slow, fast := 0, 0
	for fast < len(nums){
		if nums[slow] != nums[fast]{
			nums[slow+1] = nums[fast]
			slow++
		}
		fast++
	}
	return slow + 1
}

func main() {
	nums := []int{1,1,2}
	result := removeDuplicates(nums)
	log.Println("Result:", result)
}
