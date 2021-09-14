
# https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals={}
        for i in range(0,len(s)):
            if(s[i] not in intervals):
                intervals[s[i]]=[i,i]
            else:
                intervals[s[i]][1]=i
        ans=[]
        for i in intervals:
            ans.append(intervals[i])
        i=0
        while(i<len(ans)-1):
            if(ans[i+1][0]<=ans[i][1]):
                ans[i][0]=min(ans[i+1][0],ans[i][0])
                ans[i][1]=max(ans[i+1][1],ans[i][1])
                ans.pop(i+1)
            else:
                i+=1
        diff=[]
        for i in ans:
            diff.append(i[1]-i[0]+1)
        return diff