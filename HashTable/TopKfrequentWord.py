# https://leetcode.com/problems/top-k-frequent-words/


from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        li=[]
        x=Counter(words).most_common()
        for i in range(0,k):
            li.append(x[i][0])
        return li