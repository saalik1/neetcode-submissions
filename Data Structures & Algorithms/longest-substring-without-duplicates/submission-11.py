class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # could make a hashmap
        # convert text to ascii
        # add ascii to hashmap
        # increment counter each time until duplicate found
        # delete all entries and repeat onwards 
        # ord function
        if (len(s) == 0):
            return 0 
        if len(s) ==  1:
            return 1 
        array = []
        counter = 0
        max = 0
        for c in s:
            ch = ord(c)
            if ch not in array:
                array.append(ch)
                counter+=1
                if counter> max:
                    max = counter
            else:
                if counter> max:
                    max = counter
                a = 0
                while array[a] != ch:
                    array.pop(0)
                    counter -=1
                array.pop(0)
                array.append(ch)
                

        return max

        