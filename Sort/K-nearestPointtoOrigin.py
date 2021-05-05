# https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        li=[]
        ans=[]
        for i in range(0,len(points)):
            x=pow(pow(points[i][0],2)+pow(points[i][1],2),0.5)
            li.append([x,i])
        li.sort(key=lambda x:x[0])
        for i in range(0,k):
            ans.append(points[li[i][1]])
        return ans