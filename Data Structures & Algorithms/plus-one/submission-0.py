class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        stringed = ''
        z=0
        while len(stringed) != len(digits) :
            stringed+=(str(digits[z]))
            z+=1
        num = int(stringed)
        num +=1
        stringed2 = str(num)
        list1 = []
        for x in stringed2:
            list1.append(x)
        return list1