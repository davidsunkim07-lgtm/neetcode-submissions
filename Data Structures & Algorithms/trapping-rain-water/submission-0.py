class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = []
        prefMax = height[0]
        for i in height:
            prefMax = max(i, prefMax)
            prefix.append(prefMax)
        
        suffix = []
        suffMax = height[-1]
        for i in range(len(height) - 1, -1, -1):
            suffMax = max(height[i], suffMax)
            suffix.append(suffMax)
        suffix.reverse()
        
        sum = 0
        for i in range(len(height)):
            water = max(0, min(prefix[i],suffix[i])-height[i])
            sum += water
        return sum
        