class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        output = []
        sol = []
        nums = sorted(candidates)
        def dfs(i,total):
            

                
                if total == target:
                    
                    output.append((sol.copy()))
                    return
                if i>=len(nums):
                    return output
                elif total>target:
                    return
                else:
                    sol.append(nums[i])
                    dfs(i+1,total+nums[i])
                    sol.pop()
                    while i+1< len(nums) and nums[i] == nums[i+1]:
                        i = i+1
                    dfs(i+1,total)
                

                
        


        dfs(0,0)
    
        return output