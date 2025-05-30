class Solution:
    def reverseWords(self, s: str) -> str:
        sb = list(s[::-1])
        self.reverse_words(sb, len(sb))
        return self.cleanSpaces(sb, len(sb))

    def reverse_words(self, sb: list, n: int):
        i = 0
        j = 0
        
        while i < n:
            while i < j or (i < n and sb[i] == ' '):
                i += 1
            while j < i or (j < n and sb[j] != ' '):
                j += 1
            self.reverse(sb, i, j - 1)
    
    def cleanSpaces(self, sb: list, n: int) -> str:
        i = 0
        j = 0
        
        while j < n:
            while j < n and sb[j] == ' ':
                j += 1
            while j < n and sb[j] != ' ':
                sb[i] = sb[j]
                i += 1
                j += 1
            while j < n and sb[j] == ' ':
                j += 1
            if j < n:
                sb[i] = ' '
                i += 1
        
        return ''.join(sb[:i])

    def reverse(self, sb: list, l: int, r: int):
        while l < r:
            sb[l], sb[r] = sb[r], sb[l]
            l += 1
            r -= 1
    
