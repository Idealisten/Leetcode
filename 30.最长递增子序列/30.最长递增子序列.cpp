#include <algorithm>
class Solution {
public:
    int lengthOfLIS(vector<int>& heights) {
        int nums=heights.size();
        int height;
        vector<int>left(nums);

        for(int i=0;i<nums;i++)
        {
            left[i] = 1;
            for(int ii=0;ii<i;ii++)
            {
                if(heights[i]>heights[ii])
                {
                    left[i]= max(left[i], left[ii]+1);
                }
            }
        }
        int max_value=0;
        for(auto it=left.begin();it!=left.end();it++){
            if(*it>max_value)
                max_value = *it;
        }
        return max_value;
    }
};