class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums = sorted(nums)

        for i in range(n-2):
            # 最小的都沒辦法小於零了 整個數組一定沒有可以達成的
            if nums[i] + nums[i+1] + nums[i+2] > 0:
                break
            # 使用最大的兩個也無法 讓這個值 變成零 可以跳過
            if nums[i] + nums[n-2] + nums[n-1] < 0:
                continue
            # 如果大於idx>0 前一個的數值 跟 目前的一樣 代表求出的數組會一樣 因此跳過
            if i > 0 and nums[i-1] == nums[i]:
                continue
            # 使用i的下一個數字當two pointer 的左邊 最後一個數字當坐右邊
            l, r = i+1, n-1
            while l < r:
                three_sum = nums[i]+nums[l]+nums[r]
                if three_sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    # 排除左邊往右一格也是同樣值 造成重複的問題
                    while l+1<r and nums[l+1] == nums[l]:
                        l += 1
                    # 排除右邊往左一格也是同樣值 造成重複的問題
                    while l<r-1 and nums[r-1] == nums[r]:
                        r -= 1
                    # 左右各網內一格 找下個值
                    l += 1
                    r -= 1
                else:
                    # 
                    if three_sum > 0:
                        r -= 1
                    else:
                        l += 1
            
        return result