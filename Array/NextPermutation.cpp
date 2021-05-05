// https://leetcode.com/problems/next-permutation/

#include<vector>
#include<stdio.h>

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int x=nums.size();
        int arr[x];
        for(int i=0;i<x;i++)
        {
            arr[i]=nums[i];
        }
        next_permutation(arr,arr+x);
        for(int i=0;i<x;i++)
        {
            nums[i]=arr[i];
        }
    }
};