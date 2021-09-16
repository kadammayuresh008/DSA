# https://leetcode.com/problems/spiral-matrix/



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        m=0
        c=len(matrix[0])
        p=0
        r=len(matrix)
        while(m<c and p<r):
            for j in range(m,c):
                ans.append(matrix[p][j])
            p+=1
            for j in range(p,r):
                 ans.append(matrix[j][c-1])
            c-=1
            if(p<r):
                for j in range(c-1,m-1,-1):
                    ans.append(matrix[r-1][j])
                r-=1
            if(m<c):
                for j in range(r-1,p-1,-1):
                    ans.append(matrix[j][m])
                m+=1
        return ans



