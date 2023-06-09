class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        mx = max(nums)
        mn = min(nums)
        count = 0
        for i in nums:
            if mn < i < mx:
                count += 1
        return count

        