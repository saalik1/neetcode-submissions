class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        magazine_map = {}

        for char in ransomNote:
            if char not in ransom_map: 
                ransom_map.update({char:1}) 
            else: 
                ransom_map[char] += 1
        
        for c in magazine:
            if c not in magazine_map:
                magazine_map.update({c:1})
            else:
                magazine_map[c] +=1
        
        for no in ransom_map:
            if no not in magazine_map:
                return False
            else:
                if ransom_map[no] > magazine_map[no]:
                    return False
        return True
        
             