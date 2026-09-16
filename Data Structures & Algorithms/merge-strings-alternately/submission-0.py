class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ''
        new_length = len(word1)+len(word2)
        a=0
        while len(new_string)<new_length:
            try : 
                new_string+=(word1[a])
            except:
                pass
            try:
                new_string+=(word2[a])
            except:
                pass
            a+=1
        return new_string
            