# https://leetcode.com/problems/number-of-provinces/


class Solution:
    def dfs(self,graph,v,visited):
        visited.append(v)
        for i in graph[v]:
            if(i not in visited):
                Solution.dfs(self,graph,i,visited)
            
    def findCircleNum(self, isc: List[List[int]]) -> int:
        graph={i:[] for i in range(0,len(isc))}
        for i in range(0,len(isc)):
            for j in range(0,len(isc[0])):
                if(isc[i][j]==1 and i!=j):
                    graph[i].append(j)
        count=0
        visited=[]
        for i in range(0,len(graph)):
            if(i not in visited):
                Solution.dfs(self,graph,i,visited)
                count+=1
        return count
                    
                    