


// k closest Number

#include <iostream>
#include<queue>
#include <vector>
using namespace std;

int main()
{
    vector<int> array={5,6,7,8,9};
    int k=3;
    int x=6;
    priority_queue<pair<int,int>> queue;
    for(int i=0;i<array.size();i++)
    {
        queue.push({abs(array[i]-x),array[i]});
        if(queue.size()>k)
        {
            queue.pop();
        }
    }
    while(queue.size()>0)
    {
        cout<<queue.top().second<<" ";
        queue.pop();
    }
    cout<<"\n";
    return 0;
}
