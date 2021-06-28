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
        ptr=head.next
        while(ptr!=None):
            print(ptr.val,end=" ")
            ptr=ptr.next 
        print("\n")
        
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
    
            
head=Linklist()  
head=Linklist.Create_Linklist(1,head)
head=Linklist.Create_Linklist(2,head)
head=Linklist.Create_Linklist(3,head)
head=Linklist.Create_Linklist(4,head)
head=Linklist.Create_Linklist(5,head)
head=Linklist.Create_Linklist(6,head)
head=Linklist.Create_Linklist(7,head)

print("The linklist is:")
Linklist.Print_Linklist()


print("The middle element is:")
ele=Linklist.middleElement()
print(ele)

print("Delete middle element of linklist")
head=Linklist.DeleteMiddleElement()
Linklist.Print_Linklist()
            