class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        ans=[]
        j=0
        for i in range(len(nums)):
            if i+1==len(nums) or nums[i]+1!=nums[i+1]:
                if j==i:
                    ans.append(str(nums[i]))
                else:
                    ans.append(str(nums[j])+"->"+str(nums[i]))
                j=i+1
        return ans    