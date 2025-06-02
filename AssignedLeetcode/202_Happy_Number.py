class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))

        return n == 1  



#def recIsHappy(self, n: int) -> bool:
  #  n = list(str(n))
  #  toReturn = 0
  #  for digit in range(len(n)):
 #       toReturn = toReturn + int(n[digit]) ** 2
#    if toReturn == 1:
#        return True
#    else:
#        return Solution.isHappy(self, toReturn)
#def isHappy(self, n: int) -> bool:
#    sys.setrecursionlimit(1000)
#    try:
 #       return Solution.recIsHappy(self, n)
 #   except RecursionError:
  #      return False
