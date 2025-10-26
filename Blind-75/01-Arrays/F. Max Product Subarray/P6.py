# https://leetcode.com/problems/maximum-product-subarray/description/
# Maximum Product Subarray

from typing import List

def maxProduct_bruteForce(nums: List[int]) -> int:
    n = len(nums)
    max_prod = float('-inf')

    for i in range(n):
        curr_prod = 1
        for j in range(i, n):
            curr_prod *= nums[j]  # sum of subarray nums[i:j+1]
            max_prod = max(max_prod, curr_prod)

    return max_prod

def maxProduct_optimized(nums: List[int]) -> List[int]:
    if not nums:
        return 0

    curr_max = curr_min = result = nums[0]

    for num in nums[1:]:
        # If number is negative, swap curr_max and curr_min
        if num < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(num, curr_max * num)
        curr_min = min(num, curr_min * num)

        result = max(result, curr_max)

    return result

def maxProduct_optimized_2(nums: List[int]) -> List[int]:
    # set product to be first number initially
    # set currMax,currMin to 1's
    # iterate over nums
    #   get nums * currMax, nums*currMin, and nums
    #   set currMax to max of vals
    #   set currMin to min of vals
    #   update res if bigger product is seen
    # return res

    currMax, currMin = 1, 1
    res = nums[0]
    for i in range(len(nums)):
        vals = {nums[i], currMax * nums[i], currMin * nums[i]}
        currMax, currMin = max(vals), min(vals)
        res = max(res, currMax)
    return res

if __name__=="__main__":
    # INPUT
    nums1 = [2,3,-2,4] # 6
    nums2 = [-2,0,-1] # 0
    nums3 = [-2,3,-4] # 3

    print(maxProduct_optimized(nums3))