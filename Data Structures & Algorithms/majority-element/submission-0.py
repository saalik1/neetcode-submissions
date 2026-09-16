class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # add each number to dictionary add a counter, if already
        #if already exist counter +=1
        # after iterating compare counter
        hashednums = {}
        for num in nums:
            if num not in hashednums:
                hashednums[num] = 1
            else:
                hashednums[num]+=1
        x=0
        for num in hashednums:
            if hashednums[num] >= x:
                x = hashednums[num]
                frequents = num
        return frequents        
        
            
            
        