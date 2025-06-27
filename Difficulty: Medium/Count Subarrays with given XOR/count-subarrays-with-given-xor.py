from collections import defaultdict
class Solution:
    def subarrayXor(self, arr, k):
        # code here
        n=len(arr)
        xr=0
        map=defaultdict(int)
        map[xr]=1
        cnt=0
        
        for i in range(n):
            xr^=arr[i]
            
            # x 
            x=xr^k 
            cnt+=map[x]
            map[xr]+=1
        return cnt 
        