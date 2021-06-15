class Solution:
    def reorganizeString(self, s: str) -> str:
        x=set(s)
        list1=[]
        for i in x:
            list1.append([i,s.count(i)])
        str1=""
        while(len(list1)>1):
            list1.sort(key = lambda x: x[1],reverse=True)
            ans1=list1.pop(0)
            ans2=list1.pop(0)
            str1+=ans1[0]+ans2[0]
            ans1[1]-=1
            ans2[1]-=1
            if(ans1[1]>0):
                list1.append(ans1)
            if(ans2[1]>0):
                list1.append(ans2)
        if(len(list1)==1):
            if(list1[0][1]>=2):
                return ""
            else:
                str1+=list1[0][0]
            return str1
        else:
            return str1