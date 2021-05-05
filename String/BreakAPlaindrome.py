
# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, pal: str) -> str:
        if(len(pal)==1):
            return ""
        else:
            for i in range(0,len(pal)):
                y=pal[i]
                if(y=="a"):
                    continue
                else:
                    pal=pal[0:i]+"a"+pal[i+1:]
                    if(pal!=pal[::-1]):
                        return pal
                    else:
                        pal=pal[0:i]+y+pal[i+1:]
            if(pal[len(pal)-1]=="a"):
                return pal[0:len(pal)-1]+"b"
            else:
                return pal[0:len(pal)-1]+"a"