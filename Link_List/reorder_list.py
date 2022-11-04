""" 
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ...
        if not head:
            return

        link_array: list[int] = []
        cur = head
        while cur:
            link_array.append(cur.val)
            cur = cur.next

        front_pointer = 0
        back_pointer = len(link_array) - 1
        dummy = head
        counter = 0
        while front_pointer <= back_pointer:
            if counter % 2 == 0:
                dummy.val = link_array[front_pointer]
                front_pointer += 1
            else:
                dummy.val = link_array[back_pointer]
                back_pointer -= 1

            dummy = dummy.next
            counter += 1


def showLinkList(head: Optional[ListNode]):
    if not head:
        return

    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


def changeValue(head: ListNode):
    cur = head
    while cur:
        cur.val = cur.val + 10
        cur = cur.next


if __name__ == "__main__":
    h1 = ListNode(
        val=1,
        next=ListNode(
            val=2,next=ListNode(val=3,)
        ),
    )
    solution = Solution()
    solution.reorderList(h1)
    showLinkList(h1)
