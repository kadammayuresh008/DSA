# https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col={i:[] for i in range(0,9)}
        rows={i:[] for i in range(0,9)}
        grids={i:[] for i in range(0,9)}
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if(board[i][j]=="."):
                    continue
                else:
                    if(i>=0 and i<3):
                        if(board[i][j] not in grids[int(i//3+j//3)]):
                            grids[int(i//3+j//3)].append(board[i][j])
                        else:
                            return False
                    if(i>=3 and i<6):
                        if(board[i][j] not in grids[int(i//3+j//3+2)]):
                            grids[int(i//3+j//3+2)].append(board[i][j])
                        else:
                            return False
                    if(i>=6 and i<9):
                        if(board[i][j] not in grids[int(i//3+j//3+4)]):
                            grids[int(i//3+j//3+4)].append(board[i][j])
                        else:
                            return False
                    if(board[i][j] not in rows[i]):
                        rows[i].append(board[i][j])
                    else:
                        return False
                    if(board[i][j] not in col[j]):
                        col[j].append(board[i][j])
                    else:
                        return False
        return True
                    
                    
         