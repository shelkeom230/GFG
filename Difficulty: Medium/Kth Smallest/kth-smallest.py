#User function Template for python3


class Solution:
    
    def kthSmallest(self, arr,k):
        # get the max number 
        maxnum=max(arr)
        
        # create a count array to store freq of each number of size len(arr)+1
        cnt=[0]*(maxnum+1)
        
        # update the freq of each element 
        for num in arr:
            cnt[num]+=1
        
        # find the cumulative_cnt 
        cumulative_count=0
        for i in range(len(cnt)):
            cumulative_count+=cnt[i]
            
            if cumulative_count>=k:
                return i 
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends