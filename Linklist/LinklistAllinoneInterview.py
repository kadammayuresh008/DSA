# Linklist Question



class Linklist:
    def __init__(self,val=None):
        self.val=val
        self.next=None 
        
    # creation of Linklist    
    def Create_Linklist(val,head):
        if(head==None):
            node=Linklist(val)
            head=node 
        else:
            node=Linklist(val)
            ptr=head
            while(ptr.next!=None):
                ptr=ptr.next
            ptr.next=node
        return head 
    
    # Print Linklist
    def Print_Linklist():
        if(head):
            ptr=head
            while(ptr!=None):
                print(ptr.val,end=" ")
                ptr=ptr.next 
            print("\n")
        else:
            print("List is empty.")
        
    # to find middle of linklist 
    def middleElement():
        if(head):
            fast=head.next
            slow=head.next
            while(fast.next!=None and fast.next.next!=None):
                fast=fast.next.next
                slow=slow.next
            return slow.val 
            
    # delete middle element of Linklist
    def DeleteMiddleElement():
        if(head):
            fast=head.next
            slow=head.next
            ptr=slow
            while(fast.next!=None and fast.next.next!=None):
                ptr=slow
                fast=fast.next.next
                slow=slow.next
            ptr.next=slow.next
            return head
            
            
    # delete Linklist
    def deleteLinklist(head):
        if(head):
            pre=head
            head=head.next
            while(head!=None):
                pre=None 
                pre=head
                head=head.next
            return head
            
            
    # To reverse linklist using stack in o(n)
    def reverseLinklist(head):
        if(head):
            stack=[]
            ptr=head
            ptr2=head
            while(ptr!=None):
                stack.append(ptr.val)
                ptr=ptr.next
            while(stack):
                x=stack.pop(-1)
                head.val=x
                head=head.next
            return ptr2
            
    # to print Linklist in reverse order
    def print_rec(head):
        if(head==None):
            return 
        Linklist.print_rec(head.next)
        print(head.val,end=" ")
        
    def reverseLinklistws(head):
        prev=None
        curr=head
        next_1=curr.next
        while(curr):
            next_1=curr.next 
            curr.next=prev
            prev=curr
            curr=next_1
        return prev
        
    # Plaindrome in o(n) space
    def is_palindorme(head):
        ptr=head
        ans=[]
        while(ptr):
            ans.append(ptr.val)
            ptr=ptr.next
        ptr2=head
        count=0 
        while(ptr2):
            if(ptr2.val!=ans[len(ans)-1-count]):
                return False
            ptr2=ptr2.next
            count+=1
        return True
        
    # # Palindrome in o(1) space
    # def is_pali(left,right):
    #     if(right==None):
    #         return 0
    #     first=Linklist.is_pali(left,right.next)
    #     if(first==None):
    #         return 1
    #     second=(right.val==left.val)
    #     left=left.next 
    #     return second


    def duplicate(head):
        if(head):
            li=[]
            ptr=head
            prev=ptr 
            while(ptr):
                if(ptr.val not in li):
                    li.append(ptr.val)
                else:
                    prev.next=ptr.next 
                prev=ptr 
                ptr=ptr.next
                
    
    
    def detect_loop(head):
        fast=head
        slow=head
        while(fast and fast.next):
            slow=slow.next 
            fast=fast.next.next
            if(fast.data==slow.data):
                return True 
        return False
        
    def Remove_loop(head):
        fast=head
        slow=head
        while(fast and fast.next):
            slow=slow.next 
            fast=fast.next.next
            if(fast.data==slow.data):
                slow=head
                while(slow.next.data!=fast.next.data):
                    slow=slow.next
                    fast=fast.next 
                fast.next=None 
                return head 
        return head

        
    
            
head=Linklist(1)  
head=Linklist.Create_Linklist(2,head)
head=Linklist.Create_Linklist(3,head)
head=Linklist.Create_Linklist(1,head)
# head=Linklist.Create_Linklist(3,head)
# head=Linklist.Create_Linklist(4,head)
# head=Linklist.Create_Linklist(5,head)
# head=Linklist.Create_Linklist(6,head)
# head=Linklist.Create_Linklist(7,head)

print("The linklist is:")
Linklist.Print_Linklist()

# print("The Reverse printing of linklist is:")
# Linklist.print_rec(head)
# print("\n")



# print("The middle element is:")
# ele=Linklist.middleElement()
# print(ele)
# print("\n")


# print("Delete middle element of linklist")
# head=Linklist.DeleteMiddleElement()
# Linklist.Print_Linklist()

# print("Reverse linklist")
# head=Linklist.reverseLinklist(head)
# Linklist.Print_Linklist()

            
# print("Delete linklist")
# head=Linklist.deleteLinklist(head)
# Linklist.Print_Linklist()

# print("Reverse linklist")
# head=Linklist.reverseLinklistws(head)
# Linklist.Print_Linklist()

# print("Linklist is Palindrome:")
# x=Linklist.is_pali(head,head)
# print(x)

print("Remove Duplicate")
Linklist.duplicate(head)
Linklist.Print_Linklist()



