# graph problem

# bfs function
def BFS(graph,start,end):
    vi=[]
    ne=[]
    vi.append(start)
    ne.append(start)
    while(ne):
        x=ne.pop(0)
        if(x==end):
            print(x,end=" ")
            return
        print(x,end=" ")
        if(x in graph):
            for i in graph[x]:
                if i not in vi:
                    vi.append(i)
                    ne.append(i)
                
#dfs function   
def DFS(graph,start,end):
    vi=[]
    ne=[]
    vi.append(start)
    ne.append(start)
    while(ne):
        x=ne.pop(-1)
        if(x==end):
            print(x,end=" ")
            return
        print(x,end=" ")
        if(x in graph):
            for i in graph[x]:
                if i not in vi:
                    vi.append(i)
                    ne.append(i)

# # Undirected Graph
# n,m=map(int,input().split())
# map1={}
# for i in range(0,m):
#     u,v=map(int,input().split())
#     if(u in map1):
#         map1[u].append(v)
#     else:
#         map1[u]=[v]
#     if(v in map1):
#         map1[v].append(u)
#     else:
#         map1[v]=[u]
# print("Undirected Graph")
# print(map1)
# start=int(input())
# end=int(input())
# print("BFS:")
# BFS(map1,start,end)
# print("\n")
# print("DFS:")
# DFS(map1,start,end)


# directed Graph
n,m=map(int,input().split())
map1={}
for i in range(0,m):
    u,v=map(int,input().split())
    if(u in map1):
        map1[u].append(v)
    else:
        map1[u]=[v]
print("Directed Graph")
print(map1)
start=int(input())
end=int(input())
print("BFS:")
BFS(map1,start,end)
print("\n")
print("DFS:")
DFS(map1,start,end)
