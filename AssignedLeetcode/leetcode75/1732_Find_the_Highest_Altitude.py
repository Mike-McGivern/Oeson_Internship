class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        accum = 0
        maximum = 0
        for i in range(len(gain)):
            accum += gain[i]
            if accum > maximum:
                maximum = accum
        return maximum
