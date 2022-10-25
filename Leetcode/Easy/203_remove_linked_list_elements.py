
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = None
        new_tail = None
        current_node = head 

        while current_node:
            if current_node.val != val:
                if new_head is None:
                    new_head = ListNode(current_node.val)
                    new_tail = new_head
                else:
                    new_node = ListNode(current_node.val)
                    new_tail.next = new_node
                    new_tail = new_node

            current_node = current_node.next

        return new_head




def main():
    nodes = ListNode(1, ListNode(2, ListNode(3)))

    solution = Solution()
    new_nodes = solution.removeElements(nodes, 5)
    current_node = new_nodes

    while current_node:
        print(current_node.val)
        current_node = current_node.next


main()
