class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        if len(nums) == 0:
            return [[]]

        def dfs(i):

            if i>=len(nums):
                ans.append(subset.copy())
                 
            else:
                subset.append(nums[i])
                dfs(i+1)
                subset.pop()
                dfs(i+1)
        
        dfs(0)
        return ans
            

        
            
        