# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 如果有其中一個list跑完直接回傳 另一個list
        if not list1:
            return list2
        if not list2:
            return list1
        
        # 如果list1的數值比list2的數值小 則代表要取用當下list1當作node 而他的下一個就是遞迴 自己的下一個與list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
        