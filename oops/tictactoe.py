class grid:
    def __init__(self):
        grid=[]
        for j in range(0,3):
            ans=[]
            for i in range(0,3):
                ans.append("-")
            grid.append(ans)
        self.grid=grid
    
    def print_grid(self):
        print(self.grid)
        
    def winning_condition(self):
        # check row
        if((self.grid[0][0]=="X" and self.grid[0][1]=="X" and self.grid[0][2]=="X") or (self.grid[0][0]=="O" and self.grid[0][1]=="O" and self.grid[0][2]=="O")):
            return True
        if((self.grid[1][0]=="X" and self.grid[1][1]=="X" and self.grid[1][2]=="X") or (self.grid[1][0]=="O" and self.grid[1][1]=="O" and self.grid[1][2]=="O")):
            return True
        if((self.grid[2][0]=="X" and self.grid[2][1]=="X" and self.grid[2][2]=="X") or (self.grid[2][0]=="O" and self.grid[2][1]=="O" and self.grid[2][2]=="O")):
            return True
        # check column
        if((self.grid[0][0]=="X" and self.grid[1][0]=="X" and self.grid[2][0]=="X") or (self.grid[0][0]=="O" and self.grid[1][0]=="O" and self.grid[2][0]=="O")):
            return True
        if((self.grid[0][1]=="X" and self.grid[1][1]=="X" and self.grid[2][1]=="X") or (self.grid[0][1]=="O" and self.grid[1][1]=="O" and self.grid[2][1]=="O")):
            return True
        if((self.grid[0][2]=="X" and self.grid[1][2]=="X" and self.grid[2][2]=="X") or (self.grid[0][2]=="O" and self.grid[1][2]=="O" and self.grid[2][2]=="O")):
            return True
        # check diagonal
        if((self.grid[0][0]=="X" and self.grid[1][1]=="X" and self.grid[2][2]=="X") or (self.grid[0][0]=="O" and self.grid[1][1]=="O" and self.grid[2][2]=="O")):
            return True
        if((self.grid[0][2]=="X" and self.grid[1][1]=="X" and self.grid[2][0]=="X") or (self.grid[0][2]=="O" and self.grid[1][1]=="O" and self.grid[2][0]=="O")):
            return True
        
    
    def mark(self,obj,x,y):
        if(x>len(self.grid) and y>len(self.grid)):
            return 
        self.grid[x][y]=obj
        ans=self.winning_condition()
        if(ans==True):
            return "win"
        else:
            return "Lose"
        
        
    
    
    
maze=grid()
maze.print_grid()
# TO CHOOSE PLAYER
import random
player=random.randint(1,2)
print(player)
c=0
for i in range(0,9):
    choice=str(input())
    x,y=map(int,input().split())
    m=maze.mark(choice,x,y)
    if(m=="win"):
        c=1
        if(i%2==0):
            print("Player {0} won".format(player))
        else:
            print("Player {0} won".format(player))
        break
    maze.print_grid()
if(c==0):
    print("match tied")