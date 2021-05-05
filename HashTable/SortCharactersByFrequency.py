# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, s: str) -> str:
        c=Counter(s)
        x=heapq.nlargest(len(c), c.keys(), key=c.get)
        str1=""
        for i in x:
            str1+=c[i]*i
        return str1