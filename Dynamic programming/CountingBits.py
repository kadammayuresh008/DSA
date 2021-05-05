# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, num: int) -> List[int]:
        li=[0]
        for i in range(1,num+1):
            if(i%2==1):
                li.append(li[i//2]+1)
            else:
                li.append(li[i//2])
        return li
        