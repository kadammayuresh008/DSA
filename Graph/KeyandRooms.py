class Solution:
    def dfs(self,rooms,start):
        visited=[]
        queue=[]
        count=0
        visited.append(start)
        queue.append(start)
        while(queue):
            x=queue.pop(0)
            count+=1
            for i in rooms[x]:
                if(i not in visited):
                    visited.append(i)
                    queue.append(i)
        if(count==len(rooms)):
            return True
        else:
            return False
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        x=Solution.dfs(self,rooms,0)
        return x