def dfs(graph,start):
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
    
n,m=map(int,input().split())
vi=[]
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
end=int(input())
print("DFS:")
count=0
for i in map1:
    if(i not in vi):
        dfs(map1,i)
        count+=1 
print("\n")
print("Total number of component")
print(count)



