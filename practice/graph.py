from msilib.schema import Component
import sys


def is_path(graph,start,target,visited):
    if(start==target):
        return True
    
    visited[start]=True
    for neigh in graph[start]:
        if(visited[neigh]==False):
            ans=is_path(graph,neigh,target,visited)
            if(ans==True):
                return True 
        else:
            continue 
    return False


def printAllPath(graph,start,target,visited,path):
    if(start==target):
        print(path)
        return 
    
    visited[start]=True
    for neigh in graph[start]:
        if(visited[neigh]==False):
            printAllPath(graph,neigh,target,visited,path+"->"+str(neigh))
    visited[start]=False 
    

anspath=""
max1=sys.maxsize

def print_shortest_path(graph,start,target,visited,path,wsf):
    if(start==target):
        global max1
        if(wsf<=max1):
            global anspath
            anspath=path 
            max1=wsf
    visited[start]=True
    for neigh in graph[start]:
        if(visited[neigh[0]]==False):
            print_shortest_path(graph,neigh[0],target,visited,path+"->"+str(neigh[0]),wsf+neigh[1])
    visited[start]=False 



def getConnectedOfGraph(graph,start,visited,component):
    visited[start]=True 
    component.append(start)
    for neigh in graph[start]:
        if(visited[neigh[0]]==False):
            getConnectedOfGraph(graph,neigh[0],visited,component)
    return component 


# graph={
#   0:[1,3],
#   1:[0,2],
#   2:[1,3,5],
#   3:[0,2,4],
#   4:[3,5,6],
#   5:[2,4,6],
#   6:[4,5]
# }

# start=0
# target=6
# visited=[False for i in range(0,len(graph))]
# path=str(start)
# x=is_path(graph,start,target,visited)
# print(x)
# printAllPath(graph,start,target,visited,path)


# graph={
#   0:[[1,10],[3,40]],
#   1:[[0,10],[2,10]],
#   2:[[1,10],[3,10]],
#   3:[[0,40],[2,10],[4,2]],
#   4:[[3,2],[5,3],[6,8]],
#   5:[[4,3],[6,3]],
#   6:[[4,8],[5,3]]
# }


# start=0
# target=6
# visited=[False for i in range(0,len(graph))]
# path=str(start)
# wsf=0



# print_shortest_path(graph,start,target,visited,path,wsf)
# print(anspath)




graph={
    0:[[1,10]],
    1:[[0,10]],
    2:[[3,10]],
    3:[[2,10]],
    4:[[5,10],[6,10]],
    5:[[4,10],[6,10]],
    6:[[4,10]],
}

ans=[]
visited=[False for i in range(0,len(graph))]
for j in range(0,len(visited)):
    component=[]
    if(visited[j]==0):
        component=getConnectedOfGraph(graph,j,visited,component)
    if(component==[]):
        continue
    else:
        ans.append(component)
print(ans)