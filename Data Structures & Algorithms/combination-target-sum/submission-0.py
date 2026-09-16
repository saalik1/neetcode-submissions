class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # backtracking
        # start with number i = 0
        # go again through the list
        #


        output = []
        sol = []
        def dfs(i,total):
            
            
                if total == target:
                    output.append(sol.copy())
                    return
                if i>=len(nums):
                    return output
                elif total>target:
                    return
                elif total<target:
                    sol.append(nums[i])
                    dfs(i,total+nums[i])
                    sol.pop()
                    dfs(i+1,total)
                

                
        


        dfs(0,0)
    
        return output