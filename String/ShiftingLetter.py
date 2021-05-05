# https://leetcode.com/problems/shifting-letters/


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        shifts=shifts[::-1]
        for i in range(1,len(shifts)):
            shifts[i]=shifts[i]+shifts[i-1]
        shifts=shifts[::-1]
        S=list(S)
        for i in range(0,len(shifts)):
            x=(ord(S[i])+(shifts[i]%26))
            if(x>122):
                S[i]=chr(x-122+96)
            else:
                S[i]=chr(x)
        return "".join(S)
            