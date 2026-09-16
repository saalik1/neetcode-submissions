class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "(":")", "{":"}", "[":"]"  }
        stack = []
        if len(s) %2 != 0:
            return False
        for char in s:
            if char in hashmap.keys():
                stack.append(hashmap.get(char))
            else:
                if len(stack) == 0:
                    return False
                l = stack.pop()
                if l != char:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False