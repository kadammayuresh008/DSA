# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

# Solution 1:(iterative) solved 83 of 85 cases

class Solution:
    def isunique(s):
        li=list(s)
        if(len(li)==len(set(li))):
            return True
        else:
            return False
    def sortbyLength(arr):
        for i in range(0,len(arr)-1):
            for j in range(i+1,len(arr)):
                if(len(arr[i])<len(arr[j])):
                    arr[i],arr[j]=arr[j],arr[i]
                else:
                    continue
        return arr
        
    def maxLength(self, arr: List[str]) -> int:
        max1=0
        i=0
        arr=Solution.sortbyLength(arr)
        while(i<len(arr)):
            if(Solution.isunique(arr[i])):
                max1=max(max1,len(arr[i]))
                i+=1
            else:
                arr.pop(i)
        for i in range(0,len(arr)-1):
            str1=""
            for j in range(i,len(arr)):
                count=0
                for k in arr[j]:
                    if(k in str1):
                        count=1
                if(count==0):
                    str1+=arr[j]
                    if(Solution.isunique(str1)):
                        x=len(str1)
                        if(x>max1):
                            max1=x
                        else:
                            continue
        return max1



# Solution 2:(Recursion)

class Solution:
    def isunique(s):
        li=list(s)
        if(len(li)==len(set(li))):
            return True
        else:
            return False
        
    def formString(curr,ans):
        ans2=[]
        for j in ans:
            count=0
            for k in j:
                if k in curr:
                    count=1
                else:
                    continue
            if(count==0):
                ans2.append(j+curr)
            else:
                continue
        ans+=ans2
        return ans
        
            
    def maxLength(self, arr: List[str]) -> int:
            max1=0
            i=0
            while(i<len(arr)):
                if(Solution.isunique(arr[i])):
                    max1=max(max1,len(arr[i]))
                    i+=1
                else:
                    arr.pop(i)
            li=[""]
            for j in range(0,len(arr)):
                li=Solution.formString(arr[j],li)
            for j in li:
                if(len(j)>max1):
                    max1=len(j)
            return max1
                    
            
                
        