# Maximum_Product_Subarray

## 解題思路：

1. DP 解法
    因為是乘積所以會有負負得正 正負得負的結果，所以需要存兩個列表 一個存最大 另一個存最小
    因此每次紀錄都必須比較以下三個值該放在最大還是最小
        `上一個最大值` * `當下的值` , `上一個最小值` * `當下的值`, `當下的值`
    最後從最大值列表找出最大值輸出
    > Time Complexity : O(n)
    > Space Complexity : O(n)
2. 優化 DP 解法
    因為DP解法會儲存 每次的最大最小 但其實每次都只有用到上一個 因此可以簡化成只用一個變數 不需要一個列表
    > Time Complexity : O(n)
    > Space Complexity : O(1)


[leetcode link](https://leetcode.com/problems/maximum-product-subarray/description/)