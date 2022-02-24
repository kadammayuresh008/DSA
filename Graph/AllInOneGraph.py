# import sys
# def shortDistance(start,graph,distance):
#     queue=[]
#     queue.append(start)
#     distance[start]=0
#     while(queue):
#         x=queue.pop(0)
#         dis=distance[x]
#         for j in graph[x]:
#             if(dis+1<distance[j]):
#                 distance[j]=dis+1 
#                 queue.append(j)
#             else:
#           continue


# # topological_sort using bfs

# topo=[]
# def topological_sort(graph,indeg):
#     queue=[]
#     for i in range(0,len(indeg)):
#         if(indeg[i]==0):
#             queue.append(i)
#     while(queue):
#         x=queue.pop(0)
#         topo.append(x)
#         for neigh in graph[x]:
#             indeg[neigh]-=1 
#             if(indeg[neigh]==0):
#                 queue.append(neigh)
        

# graph={
#   0:[],
#   1:[],
#   2:[3],
#   3:[1],
#   4:[0,1],
#   5:[0,2],
# }
# indeg=[0 for i in range(0,len(graph))]
# for i in graph:
#     for j in graph[i]:
#         indeg[j]+=1 
# topological_sort(graph,indeg)
# print(topo)




# # topological_sort using dfs
# stack=[]

# def topological_sort(graph,visited,start):
#     visited[start]=1 
#     for neighbour in graph[start]:
#         if(visited[neighbour]!=1):
#             topological_sort(graph,visited,neighbour)
#     stack.append(start)
    

# graph={
#   0:[],
#   1:[],
#   2:[3],
#   3:[1],
#   4:[0,1],
#   5:[0,2],
# }
# visited=[0 for i in range(0,len(graph))]
# for i in range(0,len(visited)):
#     if(visited[i]==0):
#         topological_sort(graph,visited,i)
#     else:
#         continue
# print(stack)

# distance=[sys.maxsize for i in range(0,len(graph))]
# shortDistance(start,graph,distance)
# print("The shortest distance from source to destination is:")
# for i in range(0,len(distance)):
#     print(str(start)+" to "+str(i)+" is "+str(distance[i]))
# print(distance)


# # kahn_alorithm to detect cycle in graph
# def kahn_algorithm(graph):
#     top=0
#     queue=[]
#     indeg=[0 for i in range(0,len(graph))]
#     for i in graph:
#         for j in graph[i]:
#             indeg[j]+=1 
#     for k in range(0,len(indeg)):
#         if(indeg[k]==0):
#             queue.append(k)
#     while(queue):
#         x=queue.pop(0)
#         top+=1 
#         for neigh in graph[x]:
#             indeg[neigh]-=1 
#             if(indeg[neigh]==0):
#                 queue.append(neigh)
#             else:
#                 continue
#     if(top==len(graph)):
#         return True
#     else:
#         return False


# graph={
#   0:[],
#   1:[],
#   2:[3],
#   3:[1],
#   4:[0,1],
#   5:[0,2],
# }

# boolean=kahn_algorithm(graph)
# if(boolean==True):
#     print("Cycle not present")
# else:
#     print("Cycle is present")
    
    
    
# Checking cycle detect using dfs in topological sort
# stack=[]
# def dfs(graph,start,visited):
#     visited[start]=1 
#     for neigh in graph[start]:
#         if(visited[neigh]!=1):
#             dfs(graph,neigh,visited)
#     stack.append(start)
  

# graph={
#   0:[],
#   1:[],
#   2:[3],
#   3:[1],
#   4:[0,1],
#   5:[0,2],
# }  
# visited=[0 for i in range(0,len(graph))]
# for j in range(0,len(visited)):
#     if(visited[j]==0):
#         dfs(graph,j,visited)
#     else:
#         continue
# print(stack)


# dijisktras algorithm


