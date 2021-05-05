
# https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:
        li=[[i,len(i)] for i in text.split(" ")]
        li.sort(key=lambda x:x[1])
        print(*li)
        # str1=""
        # count=0
        # for i in range(0,len(li)):
        #     if(count==0):
        #         str1+=li[i][0].capitalize()+" "
        #         count=1
        #     else:
        #         str1+=li[i][0].lower()+" "
        # return str1[0:len(str1)-1]
        