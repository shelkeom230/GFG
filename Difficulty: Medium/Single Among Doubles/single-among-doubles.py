#User function Template for python3
class Solution:
    def search(self, n, arr):
        # your code here
        xor=0
        for ele in arr:
            xor^=ele 
        return xor 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for tc in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.search(n, arr))

        print("~")
# } Driver Code Ends