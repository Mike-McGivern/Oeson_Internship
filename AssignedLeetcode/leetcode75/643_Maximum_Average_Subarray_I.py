from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = sum(nums[:k])
        
        currSum = maxSum

        for i in range(k, len(nums)):
            currSum = currSum + nums[i] - nums[i - k]
            maxSum = max(maxSum, currSum)
        
        return maxSum / k
