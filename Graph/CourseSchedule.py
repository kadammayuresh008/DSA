# https://leetcode.com/problems/course-schedule/

class Solution:
    def isCyclic(self,graph,visited,helper,curr):
        visited.append(curr)
        helper.append(curr)
        for i in graph[curr]:
            if(i in helper):
                return True
            if(i not in visited):
                if(Solution.isCyclic(self,graph,visited,helper,i)):
                    return True
        helper.remove(curr)
        return False
        
    
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph={}
        for i in range(0,numCourses):
            graph[i]=[]
        for i in prerequisites:
            graph[i[1]].append(i[0])
        visited=[]
        helper=[]
        for num in range(0,numCourses):
            if(num not in visited):
                ans=Solution.isCyclic(self,graph,visited,helper,num)
                if(ans==True):
                    return False
        return True