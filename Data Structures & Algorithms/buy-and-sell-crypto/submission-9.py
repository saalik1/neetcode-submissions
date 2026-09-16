class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        length = len(nums)
        l,r = 0, 1
        max = 0

        while (r< len(nums)) and (l<len(nums)):
            if nums[l]< nums[r]:
                if (nums[r]- nums[l])> max:
                    max = nums[r] - nums[l]
            else:
                l =r 
            r+=1
        


        return max 
