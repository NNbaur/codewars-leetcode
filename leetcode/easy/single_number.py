# Given a non-empty array of integers nums,
# every element appears twice except for one.
# Find that single one.
#
# You must implement a solution with a linear
# runtime complexity and use only constant extra space.
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except
# for one element which appears only once.
from collections import Counter
from typing import List


class Solution:
    # Option 1
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i

    # Option 2
    def singleNumber2(self, nums: List[int]) -> int:
        c = Counter(nums)
        return c.most_common()[-1][0]

    # Option 3
    def singleNumber3(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor
