# Maximum_Subarray

## 解題思路：

1. 使用兩個for loop暴力解 但是資料太多O(n^2)會出現time exceed limit
    > Time Complexity : O(n^2)
    > Space Complexity : O(1)
2. O(n)解法
    與前面的sum相加 並與最大值比對 如果大於 則改變最大值
    判斷加完是否為正的 如果為正則繼續用這個值 如果不是則歸零
    最後回傳最大值
    > Time Complexity : O(n)
    > Space Complexity : O(1)

3. DP 解法
    紀錄上一次最大值到`dp`中 如 `dp[0]` 代表第0格的最大值 `dp[1]` 代表第1格的最大值 
    而第0格沒有選擇一定是自己
    之後的格就是判斷 `dp[0]` + `目前格得值` 與 `目前格得值`哪個比較大
    比較大的放入dp
    最後再找出dp最大值返回就可
    > Time Complexity : O(n)
    > Space Complexity : O(1)


[leetcode link](https://leetcode.com/problems/maximum-subarray/description/)