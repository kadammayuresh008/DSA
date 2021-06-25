


# https://leetcode.com/problems/binary-search-tree-iterator/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def inorder(self,root):
        if(root):
            BSTIterator.inorder(self,root.left)
            self.list.append(root.val)
            BSTIterator.inorder(self,root.right)
        
    def __init__(self, root: TreeNode):
        self.list=[]
        BSTIterator.inorder(self,root)
        self.index=0
        

    def next(self) -> int:
        self.index+=1
        return self.list[self.index-1]
        

    def hasNext(self) -> bool:
        if(self.index<len(self.list)):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()