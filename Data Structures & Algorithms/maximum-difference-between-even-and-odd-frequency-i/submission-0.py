class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap.update({char:1})
            else:
                hashmap[char]+=1
        # now we have all the frequencies we just need to compare
        # highest odd value subtract lowest even value
        nums = []
        for i in hashmap.values():
            nums.append(i)
        
        k=101
        for i in range(0,len(nums)):
            if (nums[i]<k) and (nums[i]%2 == 0):
                k = nums[i]
        z= 0
        for v in range(0,len(nums)):
            if (nums[v]>z) and (nums[v]%2 ==1):
                z = nums[v]
        return z - k



        