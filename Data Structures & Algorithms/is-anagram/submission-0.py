class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetterDict = {}
        tLetterDict = {}
        for letter in s:
            sLetterDict[letter] = sLetterDict.get(letter, 0) + 1
        
        for letter in t:
            tLetterDict[letter] = tLetterDict.get(letter, 0) + 1
        
        if sLetterDict == tLetterDict:
            return True
        else:
            return False