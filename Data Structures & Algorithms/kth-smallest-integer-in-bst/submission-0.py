# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # i assume 2n: first pass to find smallest element by dfs
        # 2nd pass to find kth element
        counter = 0
        val = 0

        def dfs(root):
            nonlocal counter
            nonlocal val

            if root == None:
                return
            
            dfs(root.left)
            counter+=1
            if counter == k:
                val = root.val
                return root.val

            dfs(root.right)
        
        dfs(root)
        return val
        
        