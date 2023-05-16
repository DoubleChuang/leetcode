# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        # 建立一個頭來重新連接這兩個list
        head = ListNode()
        curr_node = head
        # 建立兩個pointer紀錄 兩個list分別跑到哪個node
        p1 = list1
        p2 = list2

        # 持續找到兩個list其中有一個沒有node了
        while p1 is not None and p2 is not None:
            # 先接上比較小的node
            if p1.val < p2.val:
                curr_node.next = p1
                p1 = p1.next
            else :
                curr_node.next = p2
                p2 = p2.next

            curr_node = curr_node.next
        
        # 如果有其中一個list有剩餘的node 直接接在最後面
        if p1:
            curr_node.next = p1
        if p2:
            curr_node.next = p2
        
        return head.next