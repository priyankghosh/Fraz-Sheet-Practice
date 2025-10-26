# https://leetcode.com/problems/maximum-subarray/description/
# Maximum Subarray (Kadane's Algorithm)

from typing import List

def maxSubArray_bruteForce(nums: List[int]) -> int:
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += nums[j]  # sum of subarray nums[i:j+1]
            max_sum = max(max_sum, curr_sum)
    return max_sum

def maxSubArray_optimized(nums: List[int]) -> List[int]:
    curr_sum = max_sum = nums[0]

    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum

def maxSubArray_optimized_2(nums: List[int]) -> List[int]:
    curr_sum = max_sum = nums[0]

    for num in nums[1:]:
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        elif curr_sum < 0:
            curr_sum = 0

    return max_sum

if __name__=="__main__":
    # INPUT
    nums1 = [-2,1,-3,4,-1,2,1,-5,4] # 6
    nums2 = [1] # 1
    nums3 = [5,4,-1,7,8] # 23

    print(maxSubArray_optimized_2(nums1))