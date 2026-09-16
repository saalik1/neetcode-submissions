class Solution:
    def confusingNumber(self, n: int) -> bool:
        hash_map = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        stringed_int = str(n)
        rotated = [""]
        for c in stringed_int:
            if c not in hash_map:
                return False
            else:
                rotated.insert(0,hash_map[c]) 
        zxx = ""
        for xn in rotated:
            zxx += xn
        if zxx != stringed_int:
            return True
        else:
            return False

        