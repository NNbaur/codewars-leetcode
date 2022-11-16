# You are given an integer array height of length n.
# There are n vertical lines drawn such that the
# two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis
# form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
# Constraints:
#
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

from typing import List


class Solution:
    def maxArea(self, lst: List[int]) -> int:
        # Starting with first and last elements of list
        h1 = 0
        h2 = len(lst) - 1
        # Set variable for saving max area of container
        res = 0
        while h1 < h2:
            # Find area of rectangle,
            # height - minimal of two side, because
            # it is maximal possible height, that water can't pour out
            # Width - diff between x-axis points
            s = (h2 - h1) * min(lst[h1], lst[h2])
            # Save max area of container
            res = max(res, s)
            if lst[h1] < lst[h2]:
                h1 += 1
            elif lst[h2] <= lst[h1]:
                h2 -= 1
        return res
