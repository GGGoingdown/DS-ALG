# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast  = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False


if __name__ == "__main__":
    pos = ListNode(val=1)
    root = ListNode(val=0, next=pos)
    pos.next = ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4)))
    solution = Solution()
    result = solution.hasCycle(root)
    print(result)
