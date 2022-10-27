/*
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
---
Example :

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
*/
package main

import (
	"errors"
	"fmt"
	"log"
)

const MaxInt = int(^uint(0) >> 1)

type Node struct {
	val     int
	min_val int
}

type Stack struct {
	array   []Node
	min_val int
}

func (s *Stack) Push(val int) {
	local_min := s.min_val
	if val < local_min {
		local_min = val
		s.min_val = val
	}
	node := Node{val, local_min}
	s.array = append(s.array, node)
}

func (s *Stack) Pop() error {
	if len(s.array) <= 0 {
		return errors.New("empty stack")
	}
	s.array = s.array[:len(s.array)-1]
	return nil
}

func (s *Stack) GetMin() (int, error) {
	if len(s.array) == 0 {
		return -1, errors.New("empty stack")
	}
	node := s.array[len(s.array)-1]
	return node.min_val, nil
}

func showMin(s Stack){
	v1, err := s.GetMin()
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Printf("Min value: %v\n", v1)
}

func main() {
	s := Stack{min_val: MaxInt}
	s.Push(0)
	s.Push(-2)
	s.Push(-4)
	fmt.Printf("Cap=%v,Len=%v\n",cap(s.array), len(s.array))
	showMin(s)
	s.Pop()
	fmt.Printf("Cap=%v,Len=%v\n",cap(s.array), len(s.array))
	showMin(s)
	s.Pop()
	showMin(s)
	fmt.Printf("Cap=%v,Len=%v\n",cap(s.array), len(s.array))
	s.Pop()
	showMin(s)
	fmt.Printf("Cap=%v,Len=%v\n",cap(s.array), len(s.array))
	err := s.Pop()
	if err != nil{
		fmt.Println(err)
	}
	fmt.Printf("Cap=%v,Len=%v\n",cap(s.array), len(s.array))
}
