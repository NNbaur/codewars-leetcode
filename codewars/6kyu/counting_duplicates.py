# Count the number of Duplicates
# Write a function that will return the count
# of distinct case-insensitive alphabetic characters
# and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets
# (both uppercase and lowercase) and numeric digits.
#
# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times
# "Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
# "aA11" -> 2 # 'a' and '1'
# "ABBA" -> 2 # 'A' and 'B' each occur twice
from collections import Counter


def count_char1(s: str) -> int:
    c = Counter(s.lower())
    res = list(filter(lambda x: x > 1, c.values()))
    return len(res)


def count_char2(s: str) -> int:
    res = {i for i in s.lower() if s.lower().count(i) > 1}
    return len(res)
