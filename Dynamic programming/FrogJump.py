

# # frog jump
# # 1) recursive Solution
# result=0 
# def generate(arr,n):
#     if(n==0):
#         return 0
#     rec1=generate(arr,n-1)+abs(arr[n]-arr[n-1])
#     if(n>1):
#         rec2=generate(arr,n-2)+abs(arr[n]-arr[n-2])
#     else:
#         rec2=9999999999999
#     global result
#     result=min(rec1,rec2)
#     return result

# arr=[10,20,30,10]
# x=generate(arr,len(arr)-1)
# print(x)

# # 2) Dp solution
# arr=[10,20,30,10]
# dp=[0 for i in range(0,len(arr))]

# for i in range(1,len(dp)):
#     if(i==1):
#         dp[i]=dp[i-1]+abs(arr[i]-arr[i-1])
#     else:
#         dp[i]=min(dp[i-1]+abs(arr[i]-arr[i-1]),dp[i-2]+abs(arr[i]-arr[i-2]))
# print(dp[-1])



# # 3) Dp solution 2
# arr=[10,20,30,10]
# dp=[0 for i in range(0,len(arr))]
# min1=0
# prevmin1=0
# for i in range(1,len(arr)):
#     if(i==1):
#         prevmin1=min1
#         min1=min1+abs(arr[i]-arr[i-1])
#     else:
#         temp=prevmin1
#         prevmin1=min1
#         min1=min(min1+abs(arr[i]-arr[i-1]),temp+abs(arr[i]-arr[i-2]))
# print(min1)



