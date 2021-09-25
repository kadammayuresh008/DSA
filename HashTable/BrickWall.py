

# https://leetcode.com/problems/brick-wall/

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count=0
        for i in wall:
            if(len(i)==1):
                count+=1
            else:
                continue
        if(count==len(wall)):
            return len(wall)
        else:
            dict1={}
            for i in range(0,len(wall)):
                sum1=0
                for j in range(0,len(wall[i])):
                    sum1+=wall[i][j]
                    if(sum1 not in dict1):
                        dict1[sum1]=1
                    else:
                        dict1[sum1]+=1
            min1=-999999999999999999
            for i in dict1:
                if(dict1[i]>min1 and i!=max(dict1)):
                    min1=dict1[i]
            return len(wall)-min1
                
        