class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n

        longest_cnt = 0
        seen = {s[0]:0}
        
        i = 0
        for j in range(1, n):
            if s[j] not in seen:
                seen[s[j]] = j
                longest_cnt = max(longest_cnt, j - i + 1)
                continue
        
            i = max(i, seen[s[j]]+1)
            seen[s[j]] = j
            longest_cnt = max(longest_cnt, j - i + 1)
        
        return longest_cnt

