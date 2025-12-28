#include <bits/stdc++.h>
#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> nums;
    int target;
    int n;

    cin >> n >> target;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin >> x;
        nums.push_back(x);
    }

    int frontIndex = 0;
    int middleIndex = ceil((nums.size()) / 2); // 2
    int lastIndex = nums.size() - 1;                // 5

    int leftIndex = -1;
    int rightIndex = -1;

    while (true)
    {

        int currentValue = nums[middleIndex];

        cout << "loop" << endl;
        cout << frontIndex << ' ' << middleIndex << ' ' << lastIndex << endl;
        cout << currentValue << endl;

        if (frontIndex > lastIndex | frontIndex > nums.size() - 1 | lastIndex < 0)
        {
            break;
        }

        if (currentValue == target)
        {

            cout << "middleIndex " << middleIndex;
            leftIndex = middleIndex - 1;
            rightIndex = middleIndex + 1;

            if (rightIndex <= lastIndex)
            {
                while (currentValue == nums[rightIndex])
                {
                    rightIndex++;
                }
            }
            if (leftIndex >= 0)
            {
                while (currentValue == nums[leftIndex])
                {
                    leftIndex--;
                }
            }

            leftIndex++;
            rightIndex--;
            break;
        }

        if (currentValue < target)
        {
            frontIndex = middleIndex + 1;
            middleIndex = frontIndex + ceil((lastIndex - frontIndex) / 2);
        }
        if (currentValue > target)
        {
            lastIndex = middleIndex - 1;
            middleIndex = frontIndex + ceil((lastIndex - frontIndex) / 2);
        }
    }

    cout << endl;

    cout << leftIndex << ' ' << rightIndex;
}