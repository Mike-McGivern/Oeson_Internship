import sys
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = sys.maxsize
        min2 = sys.maxsize

        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        
        return False
