def HamiltonianPath(graph,start,target,visited,path,length):
    if(start==target and length==0):
        if(0 in graph[target]):
            print("Hamiltonian cycle")
            print(path)
        else:
            print("Hmailtonian Path")
            print(path)
        return 
    visited[start]=True 
    for neigh in graph[start]:
        if(visited[neigh]==False):
            HamiltonianPath(graph,neigh,target,visited,path+"->"+str(neigh),length-1)
    visited[start]=False 



graph={
    0:[1,3],
  1:[0,2],
  2:[1,3,5],
  3:[0,2,4],
  4:[3,5,6],
  5:[2,4,6],
  6:[4,5]
}


for i in range(1,len(graph)):
    visited=[False for i in range(0,len(graph))]
    start=0
    end=i
    HamiltonianPath(graph,start,end,visited,str(start),len(visited)-1)
