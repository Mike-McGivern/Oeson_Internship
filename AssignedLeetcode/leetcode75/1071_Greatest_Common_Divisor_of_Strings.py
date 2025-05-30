class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        if not str1.startswith(str2):
            return ""
        if str2 == "":
            return str1
        modify = self.mod(str1, str2)
        return self.gcdOfStrings(str2, modify)
    
    def mod(self, s1: str, s2: str) -> str:
        while s1.startswith(s2):
            s1 = s1[len(s2):]
        return s1
