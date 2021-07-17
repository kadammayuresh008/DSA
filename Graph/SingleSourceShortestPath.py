def dfs(graph,start,dist):
    ne=[]
    vi=[]
    dist1=[0]*len(graph)
    vi.append(start)
    ne.append(start)
    while(ne):
        x=ne.pop(-1)
        print(x)
        if(x in graph):
            for i in graph[x]:
                if i not in vi:
                    dist1[i-1]=dist1[x-1]+1
                    vi.append(i)
                    ne.append(i)
    print("The distance of all node from start Node")
    for i in graph:
        print("Distance of {0} from {1} is {2}".format(i,start,dist1[i-1]))
    
n,m=map(int,input().split())
map1={}
for i in range(0,m):
    u,v=map(int,input().split())
    if(u in map1):
        map1[u].append(v)
    else:
        map1[u]=[v]
    if(v in map1):
        map1[v].append(u)
    else:
        map1[v]=[u]
print("Directed Graph")
print(map1)
start=int(input())
print("DFS:")
dfs(map1,start,0)



