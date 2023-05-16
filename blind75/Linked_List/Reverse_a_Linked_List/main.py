# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        prev_node = None
        
        while curr_node is not None:
                tmp = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = tmp
        
        return prev_node