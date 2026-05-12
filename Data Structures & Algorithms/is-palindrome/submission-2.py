class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = set("0123456789abcdefghijklmnopqrstuvwxyz")

        l = 0
        r = len(s) - 1

        while l < r:
            while s[l] not in alphabet and l < r:
                l += 1
            while s[r] not in alphabet and r > l:
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
            
