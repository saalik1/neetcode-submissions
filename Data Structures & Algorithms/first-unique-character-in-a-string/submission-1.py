class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        seen_array = {}
        
    
        for k in s:
            if k not in hashmap:
                hashmap.update({k:1})
            else:
               seen_array.update({k:0})
            
        index = 0
        for m in s:
            if m not in seen_array:
                return index
            index+=1
        return -1
                
        
            
            