# Solution 1: recursive apporach 
# count=0
# def steps(n):
#     if(n==0):
#         global count
#         count+=1 
#         return
#     if(n<0):
#         return 
#     steps(n-1)
#     steps(n-2)
        
# n=3
# steps(n)
# print(count)


# Dp solution
# n=3
# dp=[0 for i in range(0,n+1)]
# for i in range(0,n+1):
#     if(i==0):
#         dp[i]=1
#     elif(i==1):
#         dp[i]=1 
#     else:
#         dp[i]=dp[i-1]+dp[i-2]
# print(dp)