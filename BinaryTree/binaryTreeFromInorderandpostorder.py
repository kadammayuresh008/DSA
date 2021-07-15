# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if(inorder):
            x=postorder.pop(-1)
            index=inorder.index(x)
            node=TreeNode(x)
            node.right=Solution.buildTree(self,inorder[index+1:],postorder)
            node.left=Solution.buildTree(self,inorder[0:index],postorder)
            return node
        
        