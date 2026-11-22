class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def num(l) -> list[str]:
            r = []
            i = 0
            while i < len(l):
                if "1" <= l[i] <= "9":
                    r.append(l[i])
                i += 1
            return r
        res = True
        for i in range(9):
            row=(i//3) *3
            col=(i%3)*3 
            sq=[board[row+(j//3)][col+ (j%3)] for j in range(9)]     
            if not (len(num(board[i])) ==  len(set(num(board[i])))) :
                res=False
            elif not(len(num([board[j][i] for j in range(9)])) ==  len(set(num([board[j][i] for j in range(9)])))) :
                res = False
            elif not(len(num(sq)) ==  len(set(num(sq)))):
                res=False
        return res