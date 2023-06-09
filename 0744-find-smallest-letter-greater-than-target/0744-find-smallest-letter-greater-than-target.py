class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        if n == 0:
            return None
        low = 0
        high = n - 1
        result = 0 
        while low <= high:
            mid = low + (high-low) // 2
            if letters[mid] > target:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return letters[result]