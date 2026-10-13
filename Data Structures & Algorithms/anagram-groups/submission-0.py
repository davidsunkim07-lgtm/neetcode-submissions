class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDictionary = {}

        for string in strs:
            charCount = [0] * 26
            for char in string:
                charCount[ord(char) - ord('a')] += 1
            charCount = tuple(charCount)
            
            if charCount in anagramDictionary:
                anagramDictionary[charCount].append(string)
            else:
                anagramDictionary[charCount] = [string]
        
        return list(anagramDictionary.values())