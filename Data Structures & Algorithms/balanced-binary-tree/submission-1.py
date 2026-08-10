# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return [0, True]
            
            leftHeight = dfs(curr.left)
            rightHeight = dfs(curr.right)
            balanced = (leftHeight[1] and rightHeight[1] and abs(leftHeight[0] - rightHeight[0]) <= 1)

            return [1 + max(leftHeight[0], rightHeight[0]), balanced]
        
        return dfs(root)[1] 


        