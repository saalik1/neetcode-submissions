class Solution:
    def countElements(self, arr: List[int]) -> int:
        counter = 0
        for k in arr:
            if k+1 in arr:
                counter+=1
        return counter