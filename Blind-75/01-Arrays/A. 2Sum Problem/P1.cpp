#include <bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> v;
    
    for (int i = 0; i < nums.size(); i++) {
        int n = nums[i];
        int m = target - n;
        
        auto itr = find(nums.begin(), nums.end(), m);
        
        if (itr != nums.end()) {
            int p = itr - nums.begin();
            if (i != p) {
                v.push_back(i);
                v.push_back(p);
                break;
            }
        }
    }
    
    return v;    
}

int main() {
    int n, target;
    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> nums(n);
    cout << "Enter the elements: ";
    for (int i = 0; i < n; ++i)
        cin >> nums[i];

    cout << "Enter the target sum: ";
    cin >> target;

    vector<int> result = twoSum(nums, target);

    if (!result.empty()) {
        cout << "Indices: " << result[0] << " " << result[1] << endl;
    } else {
        cout << "No two numbers sum up to the target." << endl;
    }

    return 0;
}
