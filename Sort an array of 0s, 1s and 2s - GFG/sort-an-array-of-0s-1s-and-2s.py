#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        low = 0
        mid = 0
        high = n-1
        while mid <= high:
            if arr[mid] == 0:
                arr[low] , arr[mid] = arr[mid] , arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else:
                arr[mid] , arr[high] = arr[high] , arr[mid]
                high -= 1
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends