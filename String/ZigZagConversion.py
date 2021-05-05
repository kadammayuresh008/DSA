

# https://leetcode.com/problems/zigzag-conversion/


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1):
            return s
        else:
            li=[]
            for i in range(0,numRows):
                rows=[]
                for j in range(0,len(s)):
                    rows.append("-")
                li.append(rows)
            down=False
            r,c=0,0
            for j in range(0,len(s)):
                if(r==0 or r==(numRows-1)):
                    down=not down
                li[r][c]=s[j]
                c+=1
                if down:
                    r+=1
                if not down:
                    r-=1
            ans=""
            for i in li:
                for j in i:
                    if(j!="-"):
                        ans+=j
            return ans

        