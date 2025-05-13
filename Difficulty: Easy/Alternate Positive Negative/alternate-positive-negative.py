#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        n=len(arr)
        pos,neg=[],[]
        
        for ele in arr:
            neg.append(ele) if ele<0 else pos.append(ele)
        
        
        if len(pos)>len(neg):
            for i in range(len(neg)):
                arr[2*i]=pos[i]
                arr[2*i+1]=neg[i]
            
            index=len(neg)*2
            for i in range(len(neg),len(pos)):
                arr[index]=pos[i]
                index+=1
        else:
            for i in range(len(pos)):
                arr[2*i]=pos[i]
                arr[2*i+1]=neg[i]
                
            index=len(pos)*2
            for i in range(len(pos),len(neg)):
                arr[index]=neg[i]
                index+=1
        return arr
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends