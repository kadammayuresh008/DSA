# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/submissions/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root:
            queue=[]
            queue.append(root)
            ans=[]
            count=0
            while(queue):
                count+=1
                size=len(queue)
                ans1=[]
                for i in range(0,size):
                    x=queue.pop(0)
                    ans1.append(x.val)
                    if(x.left):
                        queue.append(x.left)
                    if(x.right):
                        queue.append(x.right)
                if(count%2==0):
                    ans.append(ans1[::-1])
                else:
                    ans.append(ans1)
            return ans
            
                
        