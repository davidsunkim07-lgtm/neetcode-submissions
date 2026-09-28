class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetDict = {}

        for i in range(len(nums)):
            numNeeded = target - nums[i]
            if numNeeded in targetDict:
                return [targetDict[numNeeded], i]
            else:
                targetDict[nums[i]] = i