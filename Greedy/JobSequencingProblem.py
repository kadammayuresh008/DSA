# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,J,n):
        Jobs=[]
        max_deadline=0
        for i in J:
            if(i.deadline>max_deadline):
                max_deadline=i.deadline
            Jobs.append([i.id,i.deadline,i.profit])
        Jobs.sort(key=lambda x:x[2],reverse=True)   
        arr=[0]*max_deadline 
        for i in range(0,len(Jobs)):
            if(arr[Jobs[i][1]-1]==0):
                arr[Jobs[i][1]-1]=Jobs[i][2]
            else:
                for j in range(Jobs[i][1]-1,-1,-1):
                    if(arr[j]==0):
                        arr[j]=Jobs[i][2]
                        break
                    else:
                        continue
        count=0
        sum1=0
        for i in range(0,len(arr)):
            if(arr[i]>0):
                count+=1
                sum1+=arr[i]
        return [count,sum1]
        


