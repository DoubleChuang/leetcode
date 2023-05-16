from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        dp_max = nums[0]
        dp_min = nums[0]

        max_v = nums[0]
        min_v = nums[0]

        for i in range(1, n):
            a, b, c = dp_min*nums[i], dp_max*nums[i], nums[i]
            dp_max = max(a, b, c)
            dp_min = min(a, b, c)
            
            max_v = max(dp_max, max_v)
            min_v = min(dp_min, min_v)
        
        return max_v
    
nums = [-4 ,-3, -2]
ans = Solution().maxProduct(nums)
print(ans)