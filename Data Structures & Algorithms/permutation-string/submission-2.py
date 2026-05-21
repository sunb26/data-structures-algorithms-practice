class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) - 1
        s1_count = Counter(s1)

        while r < len(s2):
            new_count = Counter(s2[l:r+1])
            if new_count == s1_count:
                return True
            l += 1
            r += 1
        
        return False