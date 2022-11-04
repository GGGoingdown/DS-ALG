""" 
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        val_list: list[int] = []
        cur = head
        while cur:
            val_list.append(cur.val)
            cur = cur.next

        dummy = ListNode()
        tail = dummy
        target_idx = len(val_list) - n

        for idx, val in enumerate(val_list):
            if idx == target_idx:
                continue

            node = ListNode(val=val)
            tail.next = node
            tail = tail.next

        return dummy.next


def showLinkList(head: Optional[ListNode]):
    if not head:
        return

    cur = head
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == "__main__":
    h1 = ListNode(
        val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4)))
    )
    solution = Solution()
    result = solution.removeNthFromEnd(h1, 1)
    showLinkList(result)
