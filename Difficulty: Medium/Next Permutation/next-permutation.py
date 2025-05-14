#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        index=-1
        
        # find the breakpoint 
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                index=i 
                break 
        
        # if no breakpoint, just return the sorted array 
        if index==-1:
            arr.reverse()
            return arr 
        
        # find first element greater than index 
        for i in range(n-1,index,-1):
            if arr[i]>arr[index]:
                arr[i],arr[index]=arr[index],arr[i]
                break 
        
        # reverse the remaining array 
        arr[index+1:]=sorted(arr[index+1:])
        return arr 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends