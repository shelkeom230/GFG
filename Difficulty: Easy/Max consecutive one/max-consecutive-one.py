#User function Template for python3
class Solution:
    def maxConsecutiveCount(self, arr):
        #code here 
        current1,current2,cnt1,cnt2=0,0,0,0
        
        for i in range(0,len(arr)):
            if arr[i]==1:
                current1+=1
                cnt1=max(cnt1,current1)
            else:
                current1=0
            if arr[i]==0:
                current2+=1
                cnt2=max(cnt2,current2)
            else:
                current2=0
        return max(cnt1,cnt2) 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxConsecutiveCount(arr)
        print(ans)
        print("~")
# } Driver Code Ends