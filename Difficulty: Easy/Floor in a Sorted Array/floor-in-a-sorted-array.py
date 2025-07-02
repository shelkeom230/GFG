class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        #Your code here
        n=len(arr)
        
        ans=-1
        
         
        start,end=0,n-1
        while start<=end:
            mid=(start+end)//2
            
            if arr[mid]<=x:
                ans=mid
                
                start=mid+1
            else:
                end=mid-1  
        return ans 
        