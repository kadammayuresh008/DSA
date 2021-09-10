
# https://leetcode.com/problems/largest-plus-sign/


# Solution 1
# Recursion solution

class Solution:
    def caldis(row,col,maze,dire,length):
        if(row<0 or row>=len(maze) or col<0 or col>=len(maze[0])):
            return length
        if(maze[row][col]==0):
            return length
        if(dire=="U"):
            return Solution.caldis(row-1,col,maze,dire,length+1)
        elif(dire=="D"):
            return Solution.caldis(row+1,col,maze,dire,length+1)
        elif(dire=="L"):
            return Solution.caldis(row,col-1,maze,dire,length+1)
        else:
            return Solution.caldis(row,col+1,maze,dire,length+1)
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        maze=[[1 for i in range(0,n)] for j in range(0,n)]
        for k in mines:
            maze[k[0]][k[1]]=0
        max_plus=0
        for i in range(0,n):
            for j in range(0,n):
                if(maze[i][j]==0):
                    continue
                else:
                    l1=Solution.caldis(i,j,maze,"U",0)
                    l2=Solution.caldis(i,j,maze,"D",0)
                    l3=Solution.caldis(i,j,maze,"L",0)
                    l4=Solution.caldis(i,j,maze,"R",0)
                    l=min(l1,l2,l3,l4)
                    print(l,i,j)
                    if(l>max_plus):
                        max_plus=l
                    else:
                        continue
        return max_plus
                    

# Solution 2
# Dp Solution


class Solution:
    def callone(left,maze):
        count=0
        for i in range(0,len(maze)):
            for j in range(0,len(maze[0])):
                if(maze[i][j]==0):
                    count=0
                else:
                    count+=1
                left[i][j]=count
            count=0
        return left
            
    def calrone(right,maze):
        count=0
        for i in range(0,len(maze)):
            for j in range(len(maze[0])-1,-1,-1):
                if(maze[i][j]==0):
                    count=0
                else:
                    count+=1
                right[i][j]=count
            count=0
        return right
    
    def caltone(top,maze):
        count=0
        for j in range(0,len(maze[0])):
            for i in range(0,len(maze)):
                if(maze[i][j]==0):
                    count=0
                else:
                    count+=1
                top[i][j]=count
            count=0
        return top
    
    
    def calbone(bottom,maze):
        count=0
        for j in range(0,len(maze)):
            for i in range(len(maze[0])-1,-1,-1):
                if(maze[i][j]==0):
                    count=0
                else:
                    count+=1
                bottom[i][j]=count
            count=0
        return bottom
        
    
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        maze=[[1 for i in range(0,n)] for j in range(0,n)]
        for k in mines:
            maze[k[0]][k[1]]=0
        left=[[0 for i in range(0,n)] for j in range(0,n)]
        right=[[0 for i in range(0,n)] for j in range(0,n)]
        top=[[0 for i in range(0,n)] for j in range(0,n)]
        bottom=[[0 for i in range(0,n)] for j in range(0,n)]
        m1=Solution.callone(left,maze)
        m2=Solution.calrone(right,maze)
        m3=Solution.caltone(top,maze)
        m4=Solution.calbone(bottom,maze)
        # print(m1)
        # print(m2)
        # print(m3)
        # print(m4)
        max_dis=0
        for i in range(0,n):
            for j in range(0,n):
                l=min(m1[i][j],m2[i][j],m3[i][j],m4[i][j])
                if(l>max_dis):
                    max_dis=l
                else:
                    continue
        return max_dis
                    