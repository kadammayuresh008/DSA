# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1#



class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        interval=[]
        for i in range(0,n):
            a=[start[i],end[i]]
            interval.append(a)
        x=len(interval)
        interval.sort(key=lambda x:x[1])
        ans=[interval[0]]
        time_limit=interval[0][1]
        for i in range(1,len(interval)):
            if(interval[i][0]>time_limit):
                time_limit=interval[i][1]
                ans.append(interval[i])
        return len(ans)
            