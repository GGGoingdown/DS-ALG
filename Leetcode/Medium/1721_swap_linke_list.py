from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        return_list_node = []
        current_node = head
        # Traversal
        while current_node is not None:
            return_list_node.append(current_node)
            current_node = current_node.next
            
        if return_list_node: # If not empty list, swap it
            return_list_node[k-1].val, return_list_node[-k].val = return_list_node[-k].val, return_list_node[k-1].val
            return return_list_node[0] 
        else:
            return None

        # Time complexity -> O(n)
        # Space complexity -> O(n)