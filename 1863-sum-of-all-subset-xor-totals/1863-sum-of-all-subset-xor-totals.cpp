class Solution {
public:
    int ans = 0;
    void fun(vector<int>& nums , int i , int x){
        if(i == nums.size()){
            ans += x;
            return;
        }
        fun(nums , i+1,x^nums[i]);
        fun(nums , i+1 , x);
    } 
    int subsetXORSum(vector<int>& nums) {
        fun(nums,0,0);
        return ans;
    }
};