class Solution:
    def leaders(self, arr):
        # code here
        n=len(arr)
        leaders=[]
        maxi=float('-inf')
        for i in range(n-1,-1,-1):
            if arr[i]>=maxi:
                leaders.append(arr[i])
                maxi=arr[i]
        leaders.reverse()
        return leaders 


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends