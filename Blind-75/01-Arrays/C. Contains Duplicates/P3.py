# https://leetcode.com/problems/contains-duplicate/description/
# Contains Duplicate

from typing import List, Counter


def containsDuplicate_bruteForce(nums: List[int]) -> bool:
    frequency_dict = Counter(nums)
    for num in nums:
        if frequency_dict[num] >= 2:
            return True

    return False

def containsDuplicate_optimized(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def containsDuplicate_optimized_2(nums: List[int]) -> bool:
    return len(set(nums))<len(nums)
    # Here, len(nums): Gives actual len
    # len(set(nums)): Gives len of unique elements in set

if __name__=="__main__":
    # INPUT
    nums1 = [1,2,3,1] # true
    nums2 = [1,2,3,4] # false
    nums3 = [1,1,1,3,3,4,3,2,4,2] # true

    print(containsDuplicate_optimized(nums1))