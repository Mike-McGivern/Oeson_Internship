class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        toReturn = ''
        count = 0
        while count < len(word1) or count < len(word2):
            if count < len(word1):
                toReturn += word1[count:count + 1]
            if count < len(word2):
                toReturn += word2[count:count + 1]
            count += 1
        return toReturn
