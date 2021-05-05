# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(list(map(lambda x: x*x, A)))