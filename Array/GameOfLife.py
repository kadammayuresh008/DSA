
# https://leetcode.com/problems/game-of-life/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        new_board=[[-1]*n for i in range(0,m)]
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                count=0
                # checking right cell
                try:
                    if(board[i][j+1]==1 and j+1<len(board[i]) ):
                        count+=1
                except:
                    count+=0
                # checking left cell
                try:
                    if(board[i][j-1]==1 and j-1>=0):
                        count+=1
                except:
                    count+=0
                # checking up cell
                try:
                    if(board[i-1][j]==1 and i-1>=0):
                        count+=1
                except:
                    count+=0
                # checking down cell
                try:
                    if(board[i+1][j]==1 and i+1<len(board)):
                        count+=1
                except:
                    count+=0
                # checking right-up cell
                try:
                    if(board[i-1][j+1]==1 and i-1>=0 and  j+1<len(board[i])):
                        count+=1
                except:
                    count+=0
                # checking left-up cell
                try:
                    if(board[i-1][j-1]==1 and  i-1>=0 and j-1>=0):
                        count+=1
                except:
                    count+=0
                # checking right-down cell
                try:
                    if(board[i+1][j+1]==1 and i+1<len(board) and j+1<len(board[i])):
                        count+=1
                except:
                    count+=0
                # checking left-down cell
                try:
                    if(board[i+1][j-1]==1 and i+1<len(board) and j-1>=0):
                        count+=1
                except:
                    count+=0
                if(board[i][j]==0):
                    if(count==3):
                        new_board[i][j]=1
                    else:
                        new_board[i][j]=0
                elif(board[i][j]==1):
                    if(count<2):
                        new_board[i][j]=0
                    elif(count==2 or count==3):
                        new_board[i][j]=1
                    elif(count>3):
                        new_board[i][j]=0
        for i in range(0,len(board)):
            for j in range(0,len(board[i])):
                board[i][j]=new_board[i][j]