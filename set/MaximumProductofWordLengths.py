
# https://leetcode.com/problems/maximum-product-of-word-lengths/


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max1=0
        for i in range(0,len(words)-1):
            x=set(words[i])
            for j in range(i+1,len(words)):
                y=set(words[j])
                if(x.intersection(y)==set()):
                    pro=len(words[i])*len(words[j])
                    if(pro>max1):
                        max1=pro
        return max1
                    