def isCyclic(map1,curr,parent,vi):
    vi.append(curr)
    for i in map1[curr]:
        if(i not in vi):
            if(isCyclic(map1,i,curr,vi)):
                return True
        else:
            if(parent!=i):
                return True
    return False


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
x=isCyclic(map1,start,-1,vi)
if x==True:
    print("Cycle present") 
else:
    print("Cycle Absent")