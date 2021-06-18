

# https://leetcode.com/problems/minimum-distance-between-bst-nodes/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def minDiffInBST(self, root: TreeNode) -> int:
        if(root==None):
            return self.ans
        else:
            self.ans.append(root.val)
            if(root.left):
                Solution.minDiffInBST(self, root.left)
            if(root.right):
                Solution.minDiffInBST(self, root.right)
        min1=99999
        for i in range(0,len(self.ans)):
            for j in range(i+1,len(self.ans)):
                diff=abs(self.ans[i]-self.ans[j])
                if(diff<min1):
                    min1=diff
        return min1