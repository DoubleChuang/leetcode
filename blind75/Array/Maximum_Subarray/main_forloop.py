class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_v = -10e4
        for i in range(0, n):
            for j in range(i+1, n+1):
                total = sum(nums[i:j])
                if total > max_v: max_v = total
        
        return max_v