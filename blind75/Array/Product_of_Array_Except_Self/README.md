# Product_of_Array_Except_Self


## 解題思路：

1. 使用兩個for loop暴力可以解 但是資料太多O(n^2)會出現time exceed limit
2. O(n)解法
    將輸入資料分成三種
        1. 資料裡超過一個零 就是全部回零
        2. 資料裡只有一個零 就是零個那格填入相乘的值
        3. 資料裡都沒有零 就是用全部的乘積除以當下的值


[leetcode link](https://leetcode.com/problems/product-of-array-except-self/description/)