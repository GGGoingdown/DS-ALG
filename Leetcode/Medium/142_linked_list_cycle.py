# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        fast, slow = head, head
        count = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            count += 1

            if fast is slow:
                break

        if fast is None or count == 0:
            return None

        s1 = head
        while s1 and slow:
            if s1 is slow:
                return s1

            s1 = s1.next
            slow = slow.next

        return None


if __name__ == "__main__":
    head = ListNode(x=3)
    l2 = ListNode(x=2)
    l3 = ListNode(x=0)
    l4 = ListNode(x=4)
    head.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l2

    solution = Solution()
    result = solution.detectCycle(head)
    if result:
        print(result.val)
    else:
        print("None")
