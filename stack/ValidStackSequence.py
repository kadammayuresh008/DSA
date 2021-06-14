# https://leetcode.com/problems/validate-stack-sequences/

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack=[]
        i=0
        for j in range(0,len(pushed)):
            stack.append(pushed[j])
            while(stack and stack[-1]==popped[i]):
                stack.pop()
                i+=1
        return i==len(pushed)