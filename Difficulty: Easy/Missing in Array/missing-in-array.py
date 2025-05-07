class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)+1
        
        totalSum=n*(n+1)/2
        
        currSum=sum(arr)
        
        return int(totalSum-currSum)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends