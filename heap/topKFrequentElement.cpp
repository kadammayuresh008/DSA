// https://leetcode.com/problems/top-k-frequent-elements/submissions/


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> umap;
        priority_queue <pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> queue;
        vector<int> ans;
        for(int i=0;i<nums.size();i++)
        {
            umap[nums[i]]++;
        }
        for (auto x : umap)
        {
            // cout<<x.second<<" "<<x.first<<"\n";
            queue.push({x.second,x.first});
            if(queue.size()>k)
            {
                queue.pop();
            }
        }
        while(queue.size()>0)
        {
            ans.push_back(queue.top().second);
            queue.pop();
        }
        return ans;
    }
};