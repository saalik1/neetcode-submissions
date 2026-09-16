class Solution:
    def scoreOfString(self, s: str) -> int:
        # use function ord()
        # left and right pointer compare add to total shift each by 1
        l,r = 0,1
        length = len(s)
        total = 0
        while r<=len(s)-1:
            score = abs(ord(s[l])-ord(s[r]))
            total = total + score
            l+=1
            r+=1
        return total
            