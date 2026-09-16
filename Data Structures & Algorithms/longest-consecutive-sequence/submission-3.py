class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortednums = sorted(nums)
        if len(nums) == 0:
            return 0
        top = 1

        curr = 1
        for i in range(0, len(nums)-1):
            if (abs(sortednums[i] - sortednums[i+1]) == 1):
                curr +=1
                if curr>top:
                    top = curr
            elif (sortednums[i] == sortednums[i+1]):
                pass
            else: #(sortednums[i] != ((sortednums[i+1] -1))):
                curr = 1
        return top