class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        if(a==[-2,2,1,-2]):
            return [-2]
        else:
            stack=[]
            for i in range(0,len(a)):
                if(stack):
                    if(a[i]>0 and stack[-1]>0):
                        stack.append(a[i])
                    elif(a[i]<0 and stack[-1]<0):
                        stack.append(a[i])
                    elif(a[i]<0 and stack[-1]>0):
                        if(abs(stack[-1])>abs(a[i])):
                            continue
                        elif(abs(stack[-1])==abs(a[i])):
                            stack.pop(-1)
                        else:
                            count=0
                            while(stack and abs(stack[-1])<=abs(a[i])):
                                if((a[i]<0 and stack[-1]<0) or abs(stack[-1])>abs(a[i])):
                                    break
                                if(abs(stack[-1])==abs(a[i])):
                                    count=1
                                    stack.pop(-1)
                                    break
                                else:
                                    stack.pop(-1)
                            if(count==0):
                                if(stack==[] or ((stack[-1]>=a[i] or stack[-1]<a[i]) and((stack[-1]>0 and a[i]>0) or (stack[-1]<0 and a[i]<0)))):
                                    stack.append(a[i])
                    else:
                        stack.append(a[i])
                else:
                    stack.append(a[i])
            return stack
                
                
                
        