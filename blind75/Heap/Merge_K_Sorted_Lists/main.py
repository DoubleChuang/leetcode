# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            
            if list1.val < list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2
        
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        
        # 講列表分兩半
        mid = len(lists) // 2
        # 左半部分遞迴處理
        left = self.mergeKLists(lists[:mid])
        # 右半部分遞迴處理
        right = self.mergeKLists(lists[mid:])
        # 將兩部分合併
        return mergeTwoLists(left, right)