class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1=[]
        for x in nums:
            if x not in list1:
                list1.append(x)
        # now we have original list nums and non duplicate list list1
        if len(list1) == len(nums):
            return False
        else:
            return True


        