class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        zero_cnt = 0
        total = 1
        
        for num in nums:
            if num == 0: 
                zero_cnt += 1
                continue
            total *= num
        
        if zero_cnt > 1:
            return [0] * n
        
        if zero_cnt == 1:
            for num in nums:
                if num == 0:
                    output.append(total)
                else:
                    output.append(0)
        else:
            for num in nums:
                output.append(int(total/num))
                
        return output