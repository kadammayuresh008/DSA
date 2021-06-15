
// https://leetcode.com/problems/find-k-pairs-with-smallest-sums/


class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        priority_queue <pair<int,pair<int,int>>> queue;
        for(int i=0;i<nums1.size();i++)
        {
            for(int j=0;j<nums2.size();j++)
            {
                queue.push({nums1[i]+nums2[j],{nums1[i],nums2[j]}});
                if(queue.size()>k)
                {
                    queue.pop();
                }
            }
        }
        vector<vector<int>> ans;
        while(queue.size()>0)
        {
        vector<int> points={queue.top().second.first,queue.top().second.second};
        ans.push_back(points);
        queue.pop();
        }
      return ans;  
    }
};