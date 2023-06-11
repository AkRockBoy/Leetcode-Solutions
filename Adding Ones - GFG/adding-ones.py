#User function Template for python3

class Solution:
    def update(self, arr , n , updates, k):
        prefixsum = [0] * (n + 1)
        for i in range(k):
            prefixsum[updates[i]] += 1
        
        for i in range(1, n + 1):
            prefixsum[i] += prefixsum[i - 1]
        
        for i in range(n):
            arr[i] = prefixsum[i + 1]

                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n , k = sz[0] , sz[1]
        a = [0 for i in range(n)]
        updates = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.update(a, n, updates, k)
        print(*a)

        T -= 1


# } Driver Code Ends