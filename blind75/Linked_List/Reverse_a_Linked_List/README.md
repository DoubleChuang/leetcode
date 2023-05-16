# Reverse_a_Linked_List


## 解題思路：

1. Two pointer解法
    使用兩個pointer紀錄先前node與當前node 並依造 以下四步驟
    1. 將當前next改成先前node
    2. 將紀錄先前node的pointer記錄當前node
    3. 將紀錄當前node的pointer紀錄下一個node
    4. 並找到node為None時 代表結束
    > Time Complexity : O(n)
    > Space Complexity : O(1)

[leetcode link](https://leetcode.com/problems/reverse-linked-list/description/)