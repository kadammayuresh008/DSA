# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/


class Solution:
    def win_condition(dp):
        # horizontal
        if((dp[0][0]=="X" and dp[0][1]=="X" and dp[0][2]=="X")
          or (dp[0][0]=="O" and dp[0][1]=="O" and dp[0][2]=="O")):
            return True
        elif((dp[1][0]=="X" and dp[1][1]=="X" and dp[1][2]=="X")
          or (dp[1][0]=="O" and dp[1][1]=="O" and dp[1][2]=="O")):
            return True
        elif((dp[2][0]=="X" and dp[2][1]=="X" and dp[2][2]=="X")
          or (dp[2][0]=="O" and dp[2][1]=="O" and dp[2][2]=="O")):
            return True
        # vertical
        elif((dp[0][0]=="X" and dp[1][0]=="X" and dp[2][0]=="X")
          or (dp[0][0]=="O" and dp[1][0]=="O" and dp[2][0]=="O")):
            return True
        elif((dp[0][1]=="X" and dp[1][1]=="X" and dp[2][1]=="X")
          or (dp[0][1]=="O" and dp[1][1]=="O" and dp[2][1]=="O")):
            return True
        elif((dp[0][2]=="X" and dp[1][2]=="X" and dp[2][2]=="X")
          or (dp[0][2]=="O" and dp[1][2]=="O" and dp[2][2]=="O")):
            return True
        # diagonal
        elif((dp[0][0]=="X" and dp[1][1]=="X" and dp[2][2]=="X")
          or (dp[0][0]=="O" and dp[1][1]=="O" and dp[2][2]=="O")):
            return True
        elif((dp[2][0]=="X" and dp[1][1]=="X" and dp[0][2]=="X")
          or (dp[2][0]=="O" and dp[1][1]=="O" and dp[0][2]=="O")):
            return True
        
        
    def tictactoe(self, moves: List[List[int]]) -> str:
        dp=[["" for i in range(0,3)] for j in range(0,3)]
        for j in range(0,len(moves)):
            x=moves[j][0]
            y=moves[j][1]
            if(j%2==0):
                dp[x][y]="X"
                ans=Solution.win_condition(dp)
                if(ans==True):
                    return "A"
            else:
                dp[x][y]="O"
                ans=Solution.win_condition(dp)
                if(ans==True):
                    return "B"
        count=0
        for i in range(0,3):
            for j in range(0,3):
                if(dp[i][j]==""):
                    count+=1
        if(count==0):
            return "Draw"
        else:
            return "Pending"
        