class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        count = 0
        res = 0

        for i in range(1, length):
            if nums[i] == 1:
                dp[i] = dp[i - 1] + 1
            else:
                if nums[i - 1] == 0:
                    count = 0
                else:
                    dp[i] = dp[i - 1] - count
                    count = dp[i]
            
            res = max(res, dp[i])
        
        return res - 1 if res == length else res
