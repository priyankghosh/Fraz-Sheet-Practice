# https://leetcode.com/problems/product-of-array-except-self/description/
# Product of Array Except Self

from typing import List

def productExceptSelf_bruteForce(nums: List[int]) -> List[int]:
    result = []
    for currIndx in range(len(nums)):
        curr_prod = 1
        for otherIndx in range(len(nums)):
            if currIndx != otherIndx:
                curr_prod *= nums[otherIndx]
        result.append(curr_prod)

    return result

def productExceptSelf_optimized(nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n

    # Calculate prefix products (product of all elements to the left)
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]

    # Calculate suffix products (product of all elements to the right)
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]

    return answer

if __name__=="__main__":
    # INPUT
    nums1 = [1,2,3,4] # [24,12,8,6]
    nums2 = [-1,1,0,-3,3] # [0,0,9,0,0]
    nums3 = [0,0] # [0,0]

    print(productExceptSelf_optimized(nums3))