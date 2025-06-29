#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        
        sn=(n*(n+1))//2
        s2n=(n*(n+1)*(2*n+1))//6
        s,s2=0,0
        for ele in arr:
            s+=ele 
            s2+=(ele*ele)
        
        val1=s-sn 
        val2=s2-s2n 
        val2=val2//val1 
        
        x=(val1+val2)//2 
        y=val2-x 
        return [x,y]

