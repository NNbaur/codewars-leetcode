# Given an integer array nums, return true
# if any value appears at least twice
# in the array, and return false
# if every element is distinct.

# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
