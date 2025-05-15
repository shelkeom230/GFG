 #User function Template for python3
 
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        n=len(arr)
        if n==0:
            return 0
        
        longest,cntCurr,lastSmallest=1,0,float('-inf')
        arr=sorted(arr)
        
        for i in range(n):
            if arr[i]-1==lastSmallest:
                cntCurr+=1
                lastSmallest=arr[i]
            elif arr[i]!=lastSmallest:
                cntCurr=1
                lastSmallest=arr[i]
            longest=max(longest,cntCurr)
        return longest 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        print(Solution().longestConsecutive(a))
        print("~")
# } Driver Code Ends