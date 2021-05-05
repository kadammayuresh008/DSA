
# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            temp=''.join(sorted(i))
            if(temp in dict1):
                dict1[temp].append(i)
            else:
                dict1[temp]=[i]
        return list(dict1.values())