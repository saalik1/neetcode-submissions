class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # for each word in the list sort it
        # if sorted_word not in hashmap add it and add a empty array as the key
        # then add the actual word to the array entry
        # if already there, add the unsorted word to the array
        # once last word done return the keys
        # edge case of empty starting array return ""
        hashmap = {}
        for word in strs:
            sortedword = str(sorted(word))
            if sortedword not in hashmap.keys():
                hashmap[sortedword] = []
                hashmap[sortedword].append(word)
            else:
                hashmap[sortedword].append(word)
        
        answer  = []
        for z in hashmap.keys():
            answer.append(hashmap[z])
        return answer