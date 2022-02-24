import sys
def shortDistance(start,graph,distance):
    queue=[]
    queue.append(start)
    distance[start]=0
    while(queue):
        x=queue.pop(0)
        dis=distance[x]
        for j in graph[x]:
            if(dis+1<distance[j]):
                distance[j]=dis+1 
                queue.append(j)
            else:
                continue

start=0
graph={
    0:[1,3],
    1:[0,2,3],
    2:[1,6],
    3:[0,4],
    4:[3,5],
    5:[4,6],
    6:[2,5,7,8],
    7:[6,8],
    8:[6,7],
}
distance=[sys.maxsize for i in range(0,len(graph))]
shortDistance(start,graph,distance)
print("The shortest distance from source to destination is:")
for i in range(0,len(distance)):
    print(str(start)+" to "+str(i)+" is "+str(distance[i]))
# print(distance)
