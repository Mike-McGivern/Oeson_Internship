class Solution:
    def isVowel(self, c: str) -> bool:
        return (c == 'a' or c == 'A' or c == 'e' or c == 'E' or c == 'i' or c == 'I' or c == 'o' or c == 'O' or c == 'u' or c == 'U')
    def reverseVowels(self, s: str) -> str:
        j = 0
        charList = list(s)
        vowel = ""
        for i in range(len(charList)):
            if self.isVowel(charList[i]):
                j += 1
                vowel += charList[i]
        for i in range(len(charList)):
            if self.isVowel(charList[i]):
                charList[i] = vowel[j-1:j]
                j -= 1
        return ''.join(charList)
