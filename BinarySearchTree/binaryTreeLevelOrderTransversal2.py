# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root:
            queue=[]
            queue.append(root)
            ans=[]
            while(queue):
                size=len(queue)
                ans1=[]
                for i in range(0,size):
                    x=queue.pop(0)
                    ans1.append(x.val)
                    if(x.left):
                        queue.append(x.left)
                    if(x.right):
                        queue.append(x.right)
                ans.append(ans1)
            return ans[::-1]
        