class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # hashmap thingy
        #sliding window of length s1
        length = len(s1)
        s1_map = {}
        for entry in s1:
            if entry not in s1_map:
                s1_map[entry] = 1
            else:
                s1_map[entry] +=1
        l,r = 0,len(s1) - 1

        while r < len(s2):
            s2_map = {}
            for k in range(l,r+1):
                if s2[k] not in s2_map:
                    s2_map[s2[k]] = 1
                else:
                    s2_map[s2[k]] +=1
            if s1_map == s2_map:
                return True
            l+=1
            r+=1

        return False