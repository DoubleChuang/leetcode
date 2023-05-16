class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        max_v = 0
        # two pointer尋找
        while l < r:
            # 計算當前水量
            h = min(height[l], height[r])
            w = r - l
            max_v = max(w*h, max_v)
            
            # 保留數值比較大的一邊
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_v