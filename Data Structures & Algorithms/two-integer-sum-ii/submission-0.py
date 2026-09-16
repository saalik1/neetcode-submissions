class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length = len(numbers)
        left,right = 0,length-1
        ans = []
        while len(ans) == 0:
            if numbers[left] + numbers[right] == target:
                ans.append(left+1)
                ans.append(right+1)
            elif numbers[left] + numbers[right] < target:
                left +=1
            else:
                right -=1
        return ans
        
