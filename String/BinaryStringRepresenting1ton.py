
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        count=0
        for i in range(N,0,-1):
            str1=str(bin(i)[2:])
            if(str1 in S):
                count+=1
            else:
                count+=0
                break
        if(count==N):
            return True
        else:
            return False