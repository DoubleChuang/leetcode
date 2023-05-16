from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        min_v = nums[0]

        s = 0
        e = n-1
        
        while s != e:
            mid = (s+e)//2
            min_v = min(min_v, nums[e])
            if nums[mid] > nums[s]:
                s = mid
            else:
                e = mid
                
        return min_v

ans = Solution().findMin([ 2, 3,1])
print(f'ans: {ans}')