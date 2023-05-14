from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return min(nums)

        def is_sorted(nums):
            print(len(nums))
            return nums[0] < nums[-1]

        if is_sorted(nums):
            return nums[0]
        
        mid = n//2
        return min(self.findMin(nums[0:mid]), self.findMin(nums[mid:]))

ans = Solution().findMin([ 2, 3,1])
print(f'ans: {ans}')