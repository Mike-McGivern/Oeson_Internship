from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        else:
            count = Counter(v for v in nums if v < k)
            res = sum(min(count[v], count[k - v]) for v in count)

            return res // 2                    
