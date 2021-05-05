

# https://leetcode.com/problems/search-a-2d-matrix/



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ans=False
        for i in matrix:
            if(target>=i[0] and target<=i[len(i)-1]):
                low=0
                high=len(i)-1
                if(low==high):
                    return True
                while(low<=high):
                    mid=(low+high)//2
                    if(target<i[mid]):
                        high=mid-1
                    elif(target>i[mid]):
                        low=mid+1
                    elif(target==i[mid]):
                        ans=True
                        break
            else:
                continue
        return ans