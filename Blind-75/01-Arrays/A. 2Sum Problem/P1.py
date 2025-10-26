# https://leetcode.com/problems/two-sum/description/
# Two Sum

from typing import List

def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    result = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j]) == target:
                result.append(i)
                result.append(j)

    return result

def two_sum_optimized(nums, target):
    seen = {}  # value -> index
    for indx, num in enumerate(nums):
        #print(seen)
        complement = target - num
        if complement in seen:
            return [seen[complement], indx]
        seen[num] = indx


if __name__=="__main__":
    # INPUT
    nums = [3, 3]
    target = 6

    print(two_sum_optimized(nums, target))
