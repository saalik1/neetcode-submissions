class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            z = 1
            for j in range(0,len(nums)):
                if j != i:
                    z = z*nums[j]
            ans.append(z)
        return ans