class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first make a hashmap 
        # key is the number, value is the frequency
        # if not in hashmap add it and make the value 1
        # else make value +=1
        # use a for loop to build it
        # make an answer array
        # count = 3
        # while count>3
        # for i in range n, -1, 1
        # check if a value of a key matches i 
        # if so make count -= 1 and add it to answer array
        hashmap = {}

        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] += 1

        answers = []
        x = k

        for j in range(len(nums), 0, -1):
            for key, value in hashmap.items():
                if value == j:
                    answers.append(key)
                    x -= 1

                if len(answers) == k:
                    return answers

        return answers