class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
         nums.sort()
         length = len(nums) 
         
         solution = []
         for i in range(1,length+1):
            if i not in nums:
                solution.append(i)

         return solution
