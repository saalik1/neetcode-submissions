class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for x in nums:
            if x not in hashmap:
                hashmap.update({x:1})
            else:
                hashmap[x]+=1
        array = []
        for z in hashmap:
            if hashmap[z] == 1:
                array.append(z)

        array = sorted(array)
        if len(array) != 0 :
            return array[-1]
        else:
            return -1
        