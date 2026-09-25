class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        ans = []
        def dfs(n,opens,close,ans):
            
            if opens == n and close==n:
                k = ""
                for x in ans:
                    k+=x
                sol.append(k)
                return
            if opens<n:
                ans.append("(")
                    
                dfs(n,opens+1,close,ans)
                ans.pop()
            if close<opens:
                ans.append(")")
                dfs(n,opens,close+1,ans)
                ans.pop()
            
                

        dfs(n,0,0,ans)
        return sol