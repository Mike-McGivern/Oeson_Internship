class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        for _ in range(len(candies)):
            if candies[_] > greatest:
                greatest = candies[_]
        toReturn = []
        for _ in range(len(candies)):
            if (candies[_] + extraCandies) >= greatest:
                toReturn.append(True)
            else:
                toReturn.append(False)
        return toReturn
