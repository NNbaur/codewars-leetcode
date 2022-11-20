# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water
# it can trap after raining.

# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented
# by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain
# water (blue section) are being trapped.

# Constraints:
#
# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l_ind = 0
        r_ind = len(height) - 1
        l_value = height[l_ind]
        r_value = height[r_ind]
        res = 0
        while l_ind < r_ind:
            if r_value > l_value:
                l_ind += 1
                l_value = max(l_value, height[l_ind])
                res += l_value - height[l_ind]
            else:
                r_ind -= 1
                r_value = max(r_value, height[r_ind])
                res += r_value - height[r_ind]
        return res
