# https://leetcode.com/problems/sum-of-distances-in-tree/

# partially solved using level order tranversal
class Solution:
    def levelordertrans(self,graph,start):
        queue=[]
        visited=[]
        sum1=0
        queue.append(start)
        visited.append(start)
        level=0
        while(queue):
            size=len(queue)
            for i in range(0,size):
                x=queue.pop(0)
                sum1+=level
                for neigh in graph[x]:
                    if(neigh not in visited):
                        queue.append(neigh)
                        visited.append(neigh)
            level+=1
        return sum1
        
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if(edges==[]):
            return [0]
        else:
            graph={}
            for i in edges:
                if(i[0] not in graph):
                    graph[i[0]]=[i[1]]
                else:
                    graph[i[0]].append(i[1])
                if(i[1] not in graph):
                    graph[i[1]]=[i[0]]
                else:
                    graph[i[1]].append(i[0])
            li=[]
            for j in range(0,n):
                ans=Solution.levelordertrans(self,graph,j)
                li.append(ans)
            return li