#User function Template for python3
class Solution:
    def upperBound(self, arr, target):
        #code here
        n=len(arr)
        
        ans=n
        start,end=0,n-1
        
        while start<=end:
            mid=(start+end)//2
            
            if arr[mid]>target:
                ans=mid 
                
                end=mid-1
            else:
                start=mid+1 
        return ans 