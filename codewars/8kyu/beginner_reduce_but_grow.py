# Given a non-empty array of integers, return the result of multiplying the values together in order. Example:
#
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
from functools import reduce


def grow(arr):
    multiply = 1
    for num in arr:
        multiply *= num
    return multiply


def grow1(arr):
    return reduce(lambda x, y: x * y, arr)
