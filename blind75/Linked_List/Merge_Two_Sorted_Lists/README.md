# Merge_Two_Sorted_Lists


## 解題思路：

1. Two pointer解法
    先創建一個head node 接下來使用兩個pointer分別指向兩個list 並依照大小 將小的先方到head node下一個並移動pointer直到有一個列表沒有值
    最後在看有沒有list還沒跑完直接接在尾端 並回傳head node
    > Time Complexity : O(n)
    > Space Complexity : O(1)
2. Recursive解法
   1. 如果有其中一個list跑完直接回傳 另一個list
   2. 如果list1的數值比list2的數值小 則代表要取用當下list1當作node 而他的下一個就是遞迴 自己的下一個與list2
   3. 反之 則代表要取用當下list2當作node 而他的下一個就是遞迴 自己的下一個與list2
    > Time Complexity : O(n)
    > Space Complexity : O(1)
Ref: https://www.youtube.com/watch?v=qckKEYP9bBA&ab_channel=HuaHua
    

[leetcode link](https://leetcode.com/problems/merge-two-sorted-lists/description/)