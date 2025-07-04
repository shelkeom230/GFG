/**
 * @param {number[]} arr
 * @returns {number}
 */
class Solution {
    missingNumber(arr) {
        // code here
        let n=arr.length;
        
        let i=0;
        
        // run cyclic sort
        while(i<n){
            let correctIndex=arr[i]-1;
            // ignore -ve values
            if(arr[i]>=0 && arr[i]<=n && arr[i]!=arr[correctIndex]){
                //swap 
                [arr[i],arr[correctIndex]]=[arr[correctIndex],arr[i]];
                
            }else{
                i++;
            }
        }
        
        // check the first missing +ve value
        for(let i=0;i<n;i++){
            if(arr[i]!=i+1) return i+1;
        }
        
        // if [1--N] are present, then return n+1 wich will be absent
        return n+1;
    }
}