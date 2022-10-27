/*
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
*/

package main

import (
	"errors"
	"fmt"
	"log"
)

func twoSum(nums []int, target int) ([]int, error) {
	cacheVal := make(map[int]int)
	for i, num := range nums {
		findNum := target - num
		v, exist := cacheVal[findNum]
		if exist {
			return []int{i, v}, nil
		}
		cacheVal[num] = i
	}
	return nil, errors.New("not found compared target")
}

func main() {
	nums := []int{2, 7, 11, 15}
	target := 17
	index, err := twoSum(nums, target)
	if err != nil{
		log.Fatalln(err)
	}
	fmt.Println(index)
}
