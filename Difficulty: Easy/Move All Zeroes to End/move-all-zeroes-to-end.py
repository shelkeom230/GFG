#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# brute force solution 
    	
    	temp=[]
    	
    	for ele in arr:
    	    if ele!=0: temp.append(ele)
    	   
    	for i in range(len(temp)):
    	    arr[i]=temp[i]
    	   
    	for i in range(len(temp),len(arr)):
    	    arr[i]=0
    	
    	return 0 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
        print("~")
# } Driver Code Ends