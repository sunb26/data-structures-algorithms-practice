class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []

        def traverse(l, r: int, s: List[str]):
            if len(s) == 2*n:
                res.append("".join(s))
            if l > 0:
                s.append("(")
                traverse(l-1, r, s)
                s.pop()

            if r > l:
                s.append(")")
                traverse(l, r-1, s)
                s.pop()

        traverse(n, n, s)

        return res
    