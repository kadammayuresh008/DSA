

# https://leetcode.com/problems/reorder-list/

# Solution1



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        start=head
        while(start.next):
            end=start
            while(end.next):
                prev=end
                end=end.next
            if(prev==start):
                break
            end.next=start.next
            prev.next=None
            start.next=end
            start=end.next
        return head
            
# ######################################################################################################


# Solution2


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        count=0
        ptr=head
        while(ptr):
            count+=1
            ptr=ptr.next
        if(count%2==0):
            fh=[]
            lh=[]
            st=head
            half=int(count/2)
            i=0
            while(st):
                if(i<half):
                    fh.append(st.val)
                else:
                    lh.append(st.val)
                st=st.next
                i+=1
            pt=head
            j=0
            lh[:]=lh[::-1]
            while(pt):
                if(j%2==0):
                    pt.val=fh[0]
                    fh.pop(0)
                else:
                    pt.val=lh[0]
                    lh.pop(0)
                j+=1
                pt=pt.next
        else:
            fh=[]
            lh=[]
            st=head
            half=int(count/2)
            i=0
            while(st):
                if(i<half):
                    fh.append(st.val)
                else:
                    lh.append(st.val)
                st=st.next
                i+=1
            last=lh.pop(0)
            pt=head
            j=0
            lh[:]=lh[::-1]
            while(pt.next):
                if(j%2==0):
                    pt.val=fh[0]
                    fh.pop(0)
                else:
                    pt.val=lh[0]
                    lh.pop(0)
                j+=1
                pt=pt.next
            pt.val=last