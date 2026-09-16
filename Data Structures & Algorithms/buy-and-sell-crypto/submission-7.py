class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        length = len(nums)
        max = 0
        for i in range(0,length-1):
            for j in range(i+1,length):
                if (nums[j] - nums[i]) > max:
                    max = (nums[j] - nums[i])
        return max