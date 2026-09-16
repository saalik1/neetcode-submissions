class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hashmap = {}
        index = 0
        for char in keyboard:
            hashmap.update({char:index})
            index +=1
        
        total_distance = 0
        z = 0
        for k in word:
            total_distance += abs(hashmap.get(k)-z)
            z = hashmap.get(k)
        return total_distance
            