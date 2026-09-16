class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ans = []
        sub = []
        nums = sorted(nums)

        def dfs(i):
            
            if i == len(nums):
                if sorted(sub) not in ans:
                    ans.append(sorted(sub.copy()))
                return
                
            else:
                sub.append(nums[i])
                dfs(i+1)
                sub.pop()
                dfs(i+1)

        dfs(0)
        return ans