class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c = 0
        for i in range(len(t)):
            if c == len(s):
                break
            if t[i] == s[c]:
                c += 1
            
        if c == len(s):
            return True
        else:
            return False
