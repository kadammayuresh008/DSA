
// https://leetcode.com/problems/k-closest-points-to-origin/

class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue <pair<int,pair<int,int>>> queue;
         for (int i = 0; i < points.size(); i++)
        {
            int dist = points[i][0]*points[i][0]+points[i][1]*points[i][1];
            queue.push({dist,{points[i][0],points[i][1]}});
            if(queue.size()>k){
                queue.pop();
            }     
        }
        vector<vector<int>> ans;
        while(queue.size()>0){
            vector<int> l={queue.top().second.first,queue.top().second.second};
            ans.push_back(l);
            queue.pop();
        }
        return ans;
    }
};