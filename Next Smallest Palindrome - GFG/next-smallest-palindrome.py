#User function Template for python3
class Solution:


	def generateNextPalindrome(self,num, n ) :
	    def isAllNines(arr):
            return all(x == 9 for x in arr)
        
        if isAllNines(num):
            return [1] + [0] * (n - 1) + [1]
        
        new_num = num[:]
        mid = n // 2
        left, right = mid - 1, mid + 1 if n % 2 == 1 else mid
        
        # Find the next non-palindromic index
        while left >= 0 and new_num[left] == new_num[right]:
            left -= 1
            right += 1
        
        # Check if a higher value should be propagated
        if left < 0 or new_num[left] < new_num[right]:
            carry = 1
            left = mid - 1
            
            # Handle odd-length palindrome
            if n % 2 == 1:
                new_num[mid] += carry
                carry = new_num[mid] // 10
                new_num[mid] %= 10
                right = mid + 1
            else:
                right = mid
            
            # Propagate the carry
            while left >= 0:
                new_num[left] += carry
                carry = new_num[left] // 10
                new_num[left] %= 10
                new_num[right] = new_num[left]
                left -= 1
                right += 1
        
        # Copy the left half to the right half to ensure palindrome
        left, right = mid - 1, mid + 1 if n % 2 == 1 else mid
        while left >= 0:
            new_num[right] = new_num[left]
            left -= 1
            right += 1
        
        return new_num

	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        num=list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.generateNextPalindrome(num, n)
        for x in ans:
            print(x, end=" ")
        print()
        tc=tc-1
# } Driver Code Ends