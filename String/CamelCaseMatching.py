# https://leetcode.com/problems/camelcase-matching/


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def isMatch(word, pat):
            i, j = 0, 0
            while j < len(word) and i < len(pat):
                if word[j] == pat[i]:
                    i += 1
                elif word[j].isupper(): 
                    return False                                 
                j += 1
            return i == len(pat) and not any(ch.isupper() for ch in word[j:])    
        return [isMatch(word, pattern) for word in queries]