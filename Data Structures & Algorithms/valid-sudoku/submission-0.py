class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check for duplicates in the rows
        for r in board:
            exists = set()
            for c in r:
                if c == ".":
                    continue
                if c in exists:
                    return False
                else:
                    exists.add(c)
        
        # Check for duplicates in cols
        for c in range(9):
            exists = set()
            for r in board:
                if r[c] == ".":
                    continue
                if r[c] in exists:
                    return False
                else:
                    exists.add(r[c])
        
        # Check sub-boxes for duplicates
        exists = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in exists[(r//3, c//3)]:
                    return False
                else:
                    exists[(r//3, c//3)].add(board[r][c])
        
        return True

                    

        
