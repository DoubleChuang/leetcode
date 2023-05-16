from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_sorted(nums, s, e):
            return nums[s] < nums[e]

        def search_idx(nums: List[int], s: int, e: int, target:int) -> int:
            print(s,e)
            if len(nums[s:e+1]) < 2:
                if target == nums[s]: return s
                return -1
            mid = (s+e)//2
            
            if is_sorted(nums, s, e):
                if nums[s] > target:
                    return -1
                
                if nums[mid] == target: return mid
                elif nums[mid] > target:
                    return search_idx(nums, s, mid, target)
                else:
                    return search_idx(nums, mid+1, e, target)
            
            if nums[mid] == target: return mid
            return max(search_idx(nums, s, mid, target), search_idx(nums, mid+1, e, target))

        n = len(nums)
        return search_idx(nums, 0, n-1, target)

ans = Solution().search([1,3], 3)
print(ans)