class Solution:
    #User function Template for python3
    #Function to count inversions in the array.

    # merge function
    def merge(self,arr, low, mid, high):
        left, right = low, mid + 1
        tmp = []
        cnt = 0
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                cnt += mid - left + 1
                right += 1
    
        while left <= mid:
            tmp.append(arr[left])
            left += 1
    
        while right <= high:
            tmp.append(arr[right])
            right += 1
    
        for i in range(low, high + 1):
            arr[i] = tmp[i - low]
        return cnt
    
    
    # merge sort
    def merge_sort(self,arr, low, high):
        cnt = 0
        if low >= high:
            return cnt
    
        mid = (low + high) // 2
    
        cnt += self.merge_sort(arr, low, mid)
        cnt += self.merge_sort(arr, mid + 1, high)
        cnt += self.merge(arr, low, mid, high)
        return cnt
   
    def inversionCount(self, arr):
        # Your Code Here
        n=len(arr)
        return self.merge_sort(arr,0,n-1)