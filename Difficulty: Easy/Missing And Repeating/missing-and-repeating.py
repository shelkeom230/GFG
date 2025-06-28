#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        
        hash={}
        
        for ele in arr:
            if ele in hash:
                hash[ele]+=1
            else:
                hash[ele]=1
        
        for key,val in hash.items():
            if val==2:
                A=key 
                break 
        
        arr.remove(A)
        
        totalSum=n*(n+1)//2
        currentSum=0
        for ele in arr:
            currentSum+=ele 
        
        B=totalSum-currentSum 
        return [A,B]

