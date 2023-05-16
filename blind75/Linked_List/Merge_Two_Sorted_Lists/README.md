# Merge_Two_Sorted_Lists


## 解題思路：

1. Two pointer解法
    先創建一個head node 接下來使用兩個pointer分別指向兩個list 並依照大小 將小的先方到head node下一個並移動pointer直到有一個列表沒有值
    最後在看有沒有list還沒跑完直接接在尾端 並回傳head node
    > Time Complexity : O(n)
    > Space Complexity : O(1)

[leetcode link](https://leetcode.com/problems/merge-two-sorted-lists/description/)