package main

import "fmt"

func isAnagram(s, t string) bool {
	s_rune := []rune(s)
	t_rune := []rune(t)
	if len(s_rune) != len(t_rune) {
		return false
	}

	contains := make(map[rune]int)
	for _, v := range s_rune {
		// fmt.Printf("%v - %T\n", v, v)
		count, exist := contains[v]
		if exist {
			contains[v] = count + 1
		} else {
			contains[v] = 1
		}
	}
	fmt.Println(contains)

	for _, v := range t_rune {
		count, exist := contains[v]
		if !exist || count <= 0 { 
			return false
		}
		contains[v] = count - 1
	}

	return true

}

func main() {
	s := "anagram"
	t := "nagaram"
	result := isAnagram(s, t)
	fmt.Println(result)

}
