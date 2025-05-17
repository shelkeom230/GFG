#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        n=len(mat)
        m=len(mat[0])
        # most optimal solution 
        # row=[0]*n  // matrix[i][0] -- first column 
        # cols=[0]*m // matrix[0][j] -- first row 
        
        col0=1 # for the overlapping matrix[0][0]
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    # mark the ith row
                    mat[i][0]=0
                    
                    # mark the jth col
                    if j!=0:
                        mat[0][j]=0
                    else:
                        col0=0
        
        # transform to 0 for rest of the elements 
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j]!=0:
                    # check for row and col 
                    if mat[i][0]==0 or mat[0][j]==0:
                        mat[i][j]=0
        
        # mark the first row 
        if mat[0][0]==0:
            for j in range(m):
                mat[0][j]=0
        
        # mark the first col 
        if col0==0:
            for i in range(n):
                mat[i][0]=0
        return mat 
                    
        


#{ 
 # Driver Code Starts
import sys

# Position this line where user code will be pasted.
if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()

    idx = 0
    t = int(data[idx])
    idx += 1
    results = []

    for _ in range(t):
        n, m = map(int, data[idx:idx + 2])
        idx += 2
        arr = []
        for i in range(n):
            arr.append(list(map(int, data[idx:idx + m])))
            idx += m

        sol = Solution()
        sol.setMatrixZeroes(arr)

        for row in arr:
            results.append(" ".join(map(str, row)))

        results.append("~")

    sys.stdout.write("\n".join(results) + "\n")

# } Driver Code Ends