#User function Template for python3
class Solution:
    def lowerBound(self, arr, target):
        #code here
        n=len(arr)
        
        if target>arr[n-1]:
            return n 
        
        start,end=0,n-1 
        
        while start<=end:
            mid=(start+end)//2
            
            if target<=arr[mid]:
                ans=mid 
                
                end=mid-1 
            else:
                start=mid+1
        return start 