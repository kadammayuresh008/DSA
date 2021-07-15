# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if(inorder):
            x=preorder.pop(0)
            index=inorder.index(x)
            node=TreeNode(x)
            node.left=Solution.buildTree(self, preorder, inorder[0:index])
            node.right=Solution.buildTree(self, preorder, inorder[index+1:])
            return node
        