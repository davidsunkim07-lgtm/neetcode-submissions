class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCountDict = {}

        for num in nums:
            numCountDict[num] = numCountDict.get(num, 0) + 1
        
        bucketArray = [[] for _ in range(len(nums) + 1)]

        for n,c in numCountDict.items():
            bucketArray[c].append(n)
        
        res = []
        for i in range(len(bucketArray) - 1, 0, -1):
                for num in bucketArray[i]:
                    res.append(num)
                if len(res) == k:
                    return res

        