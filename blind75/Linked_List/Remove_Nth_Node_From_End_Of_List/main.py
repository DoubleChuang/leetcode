# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def get_nth_from_end(head: Optional[ListNode], n: int)-> Optional[ListNode]:
            # 找出總長度
            node_cnt = 0
            p = head
            while p:
                p = p.next
                node_cnt += 1
            # 算出要刪除的idx
            remove_idx = node_cnt - n
            p = head
            for i in range(remove_idx):
                p = p.next
            
            return p
        
        dummy = ListNode()
        dummy.next = head
        node = get_nth_from_end(dummy, n+1)
        node.next = node.next.next
        
        return dummy.next
        

