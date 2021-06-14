
# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack(object):

    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack=[-1]*maxSize
        self.top=-1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if(self.top+1==len(self.stack)):
            return -1
        else:
            self.top+=1
            self.stack[self.top]=x
        

    def pop(self):
        """
        :rtype: int
        """
        if(self.top==-1):
            return -1
        else:
            ele=self.stack[self.top]
            self.top-=1
            return ele
        

    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        for i in range(0,min(len(self.stack),k)):
            self.stack[i]=self.stack[i]+val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)