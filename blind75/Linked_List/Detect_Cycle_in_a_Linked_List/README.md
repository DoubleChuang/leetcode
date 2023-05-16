# Detect_Cycle_in_a_Linked_List


## 解題思路：

1. set解法
    使用set紀錄是否有重複的node出現
    > Time Complexity : O(n)
    > Space Complexity : O(n)
2. Floyds解法
    透過兩個pointer 分別為快慢pointer 一個pointer一次走兩步 一個一次走一步 只要在快pointer走完前遇到慢的pointer代表有cycle
    Ref: https://leetcode.com/problems/linked-list-cycle/solutions/3460021/beats-92-12-20-145-top-interview-question/

[leetcode link](https://leetcode.com/problems/reverse-linked-list/description/)