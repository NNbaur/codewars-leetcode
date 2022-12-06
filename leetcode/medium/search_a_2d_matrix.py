# Write an efficient algorithm that searches for a value
# target in an m x n integer matrix matrix.
# This matrix has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the
# last integer of the previous row.
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find position of list in matrix, where located our target
        low = 0
        high = len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            if target < matrix[mid][0]:
                high = mid - 1
            elif target > matrix[mid][-1]:
                low = mid + 1
            else:
                break

        # Check if target in list
        low1 = 0
        # mid is index of list in matrix
        high1 = len(matrix[mid]) - 1

        while low1 <= high1:
            mid1 = (low1 + high1) // 2
            guess = matrix[mid][mid1]
            if guess == target:
                return True
            elif guess > target:
                high1 = mid1 - 1
            else:
                low1 = mid1 + 1
        return False
