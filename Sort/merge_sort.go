package main

import "fmt"

func MergeSort(s []int) []int {
	if len(s) > 1 {
		mid := len(s) / 2
		left_s := MergeSort(s[:mid])
		right_s := MergeSort(s[mid:])
		// MergeSort(left_s)
		// MergeSort(right_s)

		// result := []int{}
		head_l, head_r, cur_idx := 0, 0, 0
		fmt.Printf("Left: %v\tRight: %v\n", left_s, right_s)
		for head_l < len(left_s) && head_r < len(right_s) {
			if left_s[head_l] <= right_s[head_r] {
				fmt.Printf("L: %v - R: %v\n", left_s[head_l], right_s[head_r])
				// result = append(result, left_s[head_l])
				s[cur_idx] = left_s[head_l]
				head_l++
			} else {
				// result = append(result, right_s[head_r])
				s[cur_idx] = right_s[head_r]
				head_r++
			}
			cur_idx++
		}
		// fmt.Println(result)

		for head_l < len(left_s) {
			//result = append(result, left_s[head_l])
			s[cur_idx] = left_s[head_l]
			head_l++
			cur_idx++
		}

		for head_r < len(right_s) {
			// result = append(result, right_s[head_r])
			s[cur_idx] = right_s[head_r]
			head_r++
			cur_idx++
		}
		// fmt.Println(result)

		return s

	} else {
		return s
	}

}

func main() {
	ar1 := []int{3, 5, 1, 7, 1, 8, 10, 2}
	fmt.Println("Before sorting", ar1)
	ar1 = MergeSort(ar1)
	fmt.Println("After sorting", ar1)

}
