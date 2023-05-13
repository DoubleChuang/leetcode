# Maximum_Subarray

## 解題思路：

1. 使用兩個for loop暴力可以解 但是資料太多O(n^2)會出現time exceed limit
2. O(n)解法
    與前面的sum相加 並與最大值比對 如果大於 則改變最大值
    判斷加完是否為正的 如果為正則繼續用這個值 如果不是則歸零
    最後回傳最大值


[leetcode link](https://leetcode.com/problems/maximum-subarray/description/)