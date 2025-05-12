#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        cnt0=0
        cnt1=0
        cnt2=0
        n=len(arr)
        
        for i in range(n):
            cnt0+=1 if arr[i]==0 else 0
            cnt1+=1 if arr[i]==1 else 0
            cnt2+=1 if arr[i]==2 else 0
        
        for i in range(cnt0): arr[i]=0
        for i in range(cnt0,cnt0+cnt1): arr[i]=1
        for i in range(cnt0+cnt1,n): arr[i]=2
        return arr 
        


#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends