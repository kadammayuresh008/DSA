
// Sort K sorted Array

#include <iostream>
#include<queue>
#include <vector>
using namespace std;

int main()
{
    priority_queue<int,vector<int>,greater<int>> queue;
    vector<int> array; 
    int k=3,x;
    for(int i=0;i<7;i++)
    {
        cin>>x;
        array.push_back(x);
    }
    for(int j=0;j<array.size();j++)
    {
        queue.push(array[j]);
        if(queue.size()>k)
        {
            cout<<queue.top()<<" ";
            queue.pop();
        }
    }
    cout<<"\n";
    return 0;
}
