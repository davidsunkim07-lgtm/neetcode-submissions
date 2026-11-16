class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()

        for num in nums:
            hashset.add(num)

        res = 0
        for num in hashset:
            high = 0
            if (num - 1) not in hashset:
                curr = num
                while curr in hashset:
                    high += 1
                    curr += 1
            res = max(high,res)
        return res