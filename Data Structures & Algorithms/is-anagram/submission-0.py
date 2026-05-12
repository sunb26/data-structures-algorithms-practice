class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmapS, hashmapT = {}, {}

        for c in s:
            if c in hashmapS.keys():
                hashmapS[c] += 1
            else:
                hashmapS[c] = 1
        
        for c in t:
            if c in hashmapT.keys():
                hashmapT[c] += 1
            else:
                hashmapT[c] = 1

        return hashmapT == hashmapS
        
        