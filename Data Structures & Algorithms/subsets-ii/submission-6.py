class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sub = []
        nums = sorted(nums)

        def dfs(i):
            ans.append(sub.copy())

            for j in range(i,len(nums)):
                if nums[j] == nums[j-1] and j>i:
                    continue
                
                sub.append(nums[j])
                dfs(j+1)
                sub.pop()
                    


        dfs(0)
        return ans