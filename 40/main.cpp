#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>

using namespace std;

// remaining Sum
void makeCombination(vector<int> &arr, int remSum, vector<int> &cur,
                     vector<vector<int>> &res, int index)
{
    if (remSum == 0)
    {
        res.push_back(cur);
        return;
    }

    if (remSum < 0 || index >= arr.size())
    {
        return;
    }

    cur.push_back(arr[index]);

    makeCombination(arr, remSum - arr[index], cur, res, index + 1);

    cur.pop_back();

    makeCombination(arr, remSum, cur, res, index + 1);
}

vector<vector<int>> targetSumComb(vector<int> &arr, int target)
{
    vector<int> cur;
    vector<vector<int>> res;
    makeCombination(arr, target, cur, res, 0);
    return res;
}

int main()
{
    vector<int> arr = {10, 1, 2, 7, 6, 1, 5};
    sort(arr.begin(), arr.end());
    int target = 8;

    vector<vector<int>> res = targetSumComb(arr, target);
    sort(res.begin(), res.end());
    res.erase(unique(res.begin(), res.end()), res.end());

    for (vector<int> &v : res)
    {
        for (int i : v)
        {
            cout << i << " ";
        }
        cout << endl;
    }

    return 0;
}