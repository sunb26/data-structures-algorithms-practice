class Solution:
    def isValid(self, s: str) -> bool:
        if not len(s) % 2 == 0:
            return False

        stack = []

        for b in s:
            if (b == ")" or b == "]" or b == "}") and stack:
                prev = stack.pop(-1)
                print(prev, b)
                if prev == "(" and b == ")" or prev == "[" and b == "]" or prev == "{" and b == "}":
                    continue
                else:
                    return False
            else:
                stack.append(b)
        
        return len(stack) == 0