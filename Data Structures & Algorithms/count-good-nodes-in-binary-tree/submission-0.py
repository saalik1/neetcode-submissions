# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # run dfs
        # keep track of the values
        # root included
        ans = 0
        top = float("-inf")
        def dfs(root,top):
            nonlocal ans
            if root is None:
                return 0
            
            if root.val >= top:
                    
                ans+=1
            
            if root.val > top:
                top = root.val
                
            dfs(root.left,top)
            dfs(root.right,top)
        dfs(root,top)
        return ans
    
        
            