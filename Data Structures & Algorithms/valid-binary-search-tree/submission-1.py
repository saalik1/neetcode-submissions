# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
    
        def dfs(root,min1,max1):
           
            
            if root == None:
                return True
            
            if root.val<=min1 or root.val>=max1:
                return False

            return dfs(root.left,min1,root.val) and dfs(root.right,root.val,max1)
            

        return dfs(root,float("-inf"), float("inf"))

