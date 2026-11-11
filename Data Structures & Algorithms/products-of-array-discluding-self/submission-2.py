class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]
        
        forward = 1
        for i in range(len(nums)):
            res[i] = forward
            forward *= nums[i]
        
        backward = 1
        for j in range(len(nums) - 1, -1 , -1):
            res[j] *= backward
            backward *= nums[j]
        
        return res
