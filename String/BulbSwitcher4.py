


# https://leetcode.com/problems/bulb-switcher-iv/



class Solution:
    def minFlips(self, target: str) -> int:
        flip=0
        for i in range(len(target)-2,-1,-1):
            if(target[i+1]==target[i]):
                continue
            else:
                flip+=1
        if(target[0]=="1" and target[len(target)-1]=="1"):
            flip+=1
        if(target[0]=="1" and target[len(target)-1]=="0"):
            flip+=1
        return flip