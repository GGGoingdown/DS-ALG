# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head_node = None
        tail_node = None
        current_node1 = list1
        current_node2 = list2
        
        while current_node1 and current_node2 :
            print(f"l1 = {current_node1.val}, l2 = {current_node2.val}")
            if current_node1.val < current_node2.val:
                val = current_node1.val
                current_node1 = current_node1.next
            else:
                val = current_node2.val
                current_node2 = current_node2.next
                
            if head_node:
                new_node = ListNode(val)
                tail_node.next = new_node
                tail_node = new_node
            else:
                head_node = ListNode(val)
                tail_node = head_node
                
        while current_node1:
            val = current_node1.val
            print(f"Node1 {val}")
            new_node = ListNode(val)
            tail_node.next = new_node
            tail_node = new_node
            
        while current_node2:
            val = current_node2.val
            new_node = ListNode(val)
            tail_node.next = new_node
            tail_node = new_node
            
        return head_node



def main():
    list1 = ListNode(1, ListNode(2, ListNode(4)))
    list2 = ListNode(1, ListNode(3, ListNode(4)))

    solution = Solution()
    sort_list = solution.mergeTwoLists(list1, list2)
    current_node = sort_list
    while current_node:
        print(current_node.val)
        current_node = current_node.next

main()

    
    