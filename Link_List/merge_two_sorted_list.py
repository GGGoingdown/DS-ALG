""" 
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        tail: Optional[ListNode] = None
        cur_l1: Optional[ListNode] = list1
        cur_l2: Optional[ListNode] = list2

        # Compare with list1 and list2
        while cur_l1 and cur_l2:
            if cur_l1.val < cur_l2.val:
                append_node = ListNode(val=cur_l1.val)
                cur_l1 = cur_l1.next
            else:
                append_node = ListNode(val=cur_l2.val)
                cur_l2 = cur_l2.next

            if head and tail:
                tail.next = append_node
                tail = append_node
            else:
                head = append_node
                tail = append_node

        # Remaining list1
        while cur_l1:
            append_node = ListNode(val=cur_l1.val)
            if head and tail:
                tail.next = append_node
                tail = append_node
            else:
                head = append_node
                tail = append_node

            cur_l1 = cur_l1.next

        # Remaining list2
        while cur_l2:
            append_node = ListNode(val=cur_l2.val)
            if head and tail:
                tail.next = append_node
                tail = append_node
            else:
                head = append_node
                tail = append_node

            cur_l2 = cur_l2.next

        return head


def showLinkList(head: Optional[ListNode]) -> None:
    cur = head
    while cur:
        print(f"Val: {cur.val}")
        cur = cur.next


if __name__ == "__main__":
    l1 = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))
    l2 = ListNode(
        val=0, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4)))
    )

    solution = Solution()
    result = solution.mergeTwoLists(l1, None)
    showLinkList(result)
