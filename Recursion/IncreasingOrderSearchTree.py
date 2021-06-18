

# https://leetcode.com/problems/increasing-order-search-tree/




# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def __init__(self):
#         self.head=TreeNode(None)
#         self.ptr=self.head
#     def increasingBST(self, root: TreeNode) -> TreeNode:
#         if(root):
#             Solution.increasingBST(self, root.left)
#             self.head.left=None
#             self.head.right=root
#             self.head=root
#             Solution.increasingBST(self, root.right)
#         return self.ptr.right


class Solution:
    def increasingBST(self, root):
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
            