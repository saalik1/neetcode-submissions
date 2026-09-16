class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        top = 0
        l = 1
        r = 1
        curr = 1
        if len(nums) == 1:
            return 1
        while l<len(nums):
            
            if nums[l]>nums[l-1]:
                curr +=1
            else:
                curr = 1
            if curr > top:
                top = curr
            

            l +=1

        curr = 1
        while r<len(nums):
            
            if nums[r]<nums[r-1]:
                curr +=1
            else:
                curr = 1
            if curr > top:
                top = curr
            

            r +=1

        return top