
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max1=0
        for i in range(0,len(s)):
            ans=""
            for j in s[i:]:
                if(j not in ans):
                    ans+=j
                else:
                    if(len(ans)>max1):
                        max1=len(ans)
                    ans=" "
                    break
            if(len(ans)>max1):
                max1=len(ans)
        return max1
                