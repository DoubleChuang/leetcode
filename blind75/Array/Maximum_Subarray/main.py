class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = -10e4
        # 判斷加完是否為正的 如果為正則繼續用這個值
        # 如果不是則歸零
        temp_sum=0
        for num in nums:
            temp_sum += num
            if max_sum < temp_sum:
                max_sum = temp_sum
            
            if temp_sum < 0:
                temp_sum = 0
            
        return max_sum