class Tree(object):
    def __init__(self,val):
        self.left=None
        self.right=None
        self.val=val
        
        
    def insert(root,val):
        if(root==None):
            return Tree(val)
        if(val<root.val):
            root.left=Tree.insert(root.left,val)
        else:
            root.right=Tree.insert(root.right,val)
        return root
        
        
    def dfs(root):
        queue=[]
        queue.append(root)
        while(queue):
            x=queue.pop(-1)
            print(x.val,end=" ")
            if(x.right):
                queue.append(x.right)
            if(x.left):
                queue.append(x.left)
    
    def bfs(root):
        queue=[]
        queue.append(root)
        while(queue):
            x=queue.pop(0)
            print(x.val,end=" ")
            if(x.left):
                queue.append(x.left)
            if(x.right):
                queue.append(x.right)
                
                
    def inorder(root):
        if(root):
            Tree.inorder(root.left)
            print(root.val,end=" ")
            Tree.inorder(root.right)
    
    
    def preorder(root):
        if(root):
            print(root.val,end=" ")
            Tree.inorder(root.left)
            Tree.inorder(root.right)
    
    def postorder(root):
        if(root):
            Tree.inorder(root.left)
            Tree.inorder(root.right)
            print(root.val,end=" ")
    
                
    def level_order_transversal(root):
        queue=[]
        queue.append(root)
        while(queue):
            x=queue.pop(0)
            print(x.val,end=" ")
            if(x.left):
                queue.append(x.left)
            if(x.right):
                queue.append(x.right)
                
    def left_view(root):
        queue=[]
        queue.append(root)
        while(queue):
            size=len(queue)
            for i in range(0,size):
                x=queue.pop(0)
                if(i==0):
                    print(x.val,end=" ")
                if(x.left):
                    queue.append(x.left)
                if(x.right):
                    queue.append(x.right)
                    
                    
    def right_view(root):
        queue=[]
        queue.append(root)
        while(queue):
            size=len(queue)
            for i in range(0,size):
                x=queue.pop(0)
                if(i==size-1):
                    print(x.val,end=" ")
                if(x.left):
                    queue.append(x.left)
                if(x.right):
                    queue.append(x.right)
                    
                    
    def top_view(root):
        dict1={}
        queue=[[root,0]]
        while(queue):
            x=queue.pop()
            if(x[1] not in dict1):
                dict1[x[1]]=x[0].val
            if(x[0].right):
                queue.append([x[0].right,x[1]+1])
            if(x[0].left):
                queue.append([x[0].left,x[1]-1])
        for i in dict1:
            print(dict1[i],end=" ")
    
    def bottom_view(root):
        dict1={}
        queue=[[root,0]]
        while(queue):
            x=queue.pop()
            dict1[x[1]]=x[0].val
            if(x[0].left):
                queue.append([x[0].left,x[1]-1])
            if(x[0].right):
                queue.append([x[0].right,x[1]+1])
        for i in dict1:
            print(dict1[i],end=" ")
    
    def maximum_depth(root):
        if(root==None):
            return 0
        else:
            return 1+max(Tree.maximum_depth(root.left),Tree.maximum_depth(root.right))
        
    
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)  
root.right.left=Tree(6)
root.right.right=Tree(7) 
Tree.insert(root,10)
Tree.insert(root,20)
Tree.insert(root,30)



print("The dfs of the given tree is:")
Tree.dfs(root)
print("\n")
print("The bfs of the given tree is:")
Tree.bfs(root)
print("\n")
print("The inorder transversal of the tree is")
Tree.inorder(root)
print("\n")
print("The preorder transversal of the tree is")
Tree.preorder(root)
print("\n")
print("The postorder transversal of the tree is")
Tree.postorder(root)
print("\n")
print("The levelorder transversal of the tree is")
Tree.level_order_transversal(root)
print("\n")
print("The leftview transversal of the tree is")
Tree.left_view(root)
print("\n")
print("The rightview transversal of the tree is")
Tree.right_view(root)
print("\n")
print("The topview transversal of the tree is")
Tree.top_view(root)
print("\n")
print("The bottomview transversal of the tree is")
Tree.bottom_view(root)
print("\n")
print("The Maximum depth of the tree is")
depth=Tree.maximum_depth(root)
print(depth)