class Solution:
    def countSeniors(self, details: List[str]) -> int:
        sum = 0
        for k in details:
            if (int(k[11])*10 + int(k[12]))>60:
                sum+=1
        return sum