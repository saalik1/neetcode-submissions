class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums = sorted(nums)
        # we run a for loop for the i and then get two pointers next
        # sort the thingy before adding and check the sorted thing not already in the list
        ans  = []
        for i in range(0,len(nums)):
            
            j = i + 1 
            k = length - 1
            while j<k:
                if nums[i] + nums[j] + nums[k] == 0:
                    minians = []
                    minians.append(nums[i])
                    minians.append(nums[j])
                    minians.append(nums[k])
                    minians = sorted(minians)
                    if minians not in ans:
                        ans.append(minians)
                    k-=1
                if nums[i] + nums[j] + nums[k] < 0:
                    j +=1
                if nums[i] + nums[j] + nums[k] > 0:
                    k -=1
        return ans
                
