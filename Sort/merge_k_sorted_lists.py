""" 
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

"""

from re import L
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) <= 0:
            return None

        merge_lists: list[Optional[ListNode]] = lists

        while len(merge_lists) > 1:
            tmp_lists = []
            for i in range(0, len(merge_lists), 2):
                l1 = merge_lists[i]
                l2 = merge_lists[i + 1] if (i + 1) < len(merge_lists) else None
                mergeListNode = self._mergeTwoSortedListNode(l1, l2)
                tmp_lists.append(mergeListNode)
            merge_lists = tmp_lists

        return merge_lists[0]

    def _mergeTwoSortedListNode(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return None

        cur1 = l1
        cur2 = l2
        dummy = ListNode()
        tail = dummy

        while cur1 and cur2:
            tmp = 0
            if cur1.val < cur2.val:
                tmp = cur1.val
                cur1 = cur1.next
            else:
                tmp = cur2.val
                cur2 = cur2.next

            node = ListNode(val=tmp)
            tail.next = node
            tail = tail.next

        while cur1:
            node = ListNode(val=cur1.val)
            tail.next = node
            tail = tail.next
            cur1 = cur1.next

        while cur2:
            node = ListNode(val=cur2.val)
            tail.next = node
            tail = tail.next
            cur2 = cur2.next

        return dummy.next


def iterateListNode(node: ListNode):
    cur = node
    while cur:
        print(cur.val)
        cur = cur.next


if __name__ == "__main__":
    l1 = ListNode(val=1, next=ListNode(val=4, next=ListNode(val=5)))
    l2 = ListNode(val=1, next=ListNode(val=3, next=ListNode(val=4)))
    l3 = ListNode(val=2, next=ListNode(val=6))
    l: list[Optional[ListNode]] = [l1, l2, l3]
    solution = Solution()
    result = solution.mergeKLists(l)

    if result:
        iterateListNode(result)
