# https://leetcode.com/problems/slowest-key/


class Solution:
    def slowestKey(self, rT: List[int], kP: str) -> str:
        maxdu=rT[0]
        let=kP[0]
        for i in range(1,len(kP)):
            dur=rT[i]-rT[i-1]
            if(dur>maxdu):
                maxdu=dur
                let=kP[i]
            elif(dur==maxdu):
                maxdu=dur
                if(ord(let)<ord(kP[i])):
                    let=kP[i]
                else:
                    continue
            else:
                continue
        return let
                