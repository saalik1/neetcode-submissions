class Solution:
    def findLucky(self, arr: List[int]) -> int:
        # use a hashmap - number is key 
        # frequency is the value
        # check the largest value
        # if not equal to the key then delete
        # repeat
        # if empty hashmap return -1

        hashmap = {}
        for i in arr:
            if i not in hashmap:
                hashmap.update({i:1})
            else:
                hashmap.update({i:hashmap.get(i)+1})
        
        max = -1
        for num in hashmap:
            if (hashmap.get(num) == num) and (num>max):
                max = num
            
        return max

