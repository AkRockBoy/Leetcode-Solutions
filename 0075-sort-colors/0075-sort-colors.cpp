class Solution {
public:
    void swap(int a , int b)
    {
        int t = a;
        b = a;
        a = t;
    }
    void sortColors(vector<int>& nums) {
        int i = 0 , left = 0 , n = nums.size()-1;
        int right = n;
        while(i <= right)
        {
            if(nums[i] == 0)
            {
                int t = nums[i];
                nums[i] = nums[left];
                nums[left] = t;
                i++;
                left++;
            }
            else if(nums[i] == 2)
            {
                int t = nums[i];
                nums[i] = nums[right];
                nums[right] = t;
                right--;
            }
            else
            {
                i++;
            }
        }
        
    }
};