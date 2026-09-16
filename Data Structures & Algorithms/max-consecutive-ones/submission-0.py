class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        score = 0
        length = len(nums)
        for i in range(0,length):
            if nums[i] == 1:
                score+=1
                if score > max:
                    max = score
            elif nums[i] == 0:
                if score > max:
                    max = score
                score = 0
        return max
            
