# https://leetcode.com/problems/sort-an-array/

class Solution:
    def Merge(nums,l,mid,h):
        left=[0]*(mid-l+1)
        right=[0]*(h-mid)
        for i in range(0,mid-l+1):
            left[i]=nums[l+i]
        for j in range(0,h-mid):
            right[j]=nums[mid+j+1]
        i=0
        j=0
        k=l
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
                nums[k]=left[i]
                i+=1
                k+=1 
            else:
                nums[k]=right[j]
                j+=1
                k+=1
        while(j<len(right)):
            nums[k]=right[j]
            j+=1
            k+=1
        while(i<len(left)):
            nums[k]=left[i]
            i+=1
            k+=1
    def Merge_sort(nums,l,h):
        if(l<h):
            mid=int((l+h)/2)
            Solution.Merge_sort(nums,l,mid)
            Solution.Merge_sort(nums,mid+1,h)
            Solution.Merge(nums,l,mid,h)
    def sortArray(self, nums: List[int],l=0,h=0) -> List[int]:
        Solution.Merge_sort(nums,0,len(nums)-1)
        return nums