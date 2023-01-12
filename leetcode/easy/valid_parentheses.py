# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding
# open bracket of the same type.


class Solution:
    def isValid(self, string: str) -> bool:
        dict = {')': '(', ']': '[', '}': '{'}
        stack = []
        for i in string:
            if stack and stack[-1] == dict.get(i):
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        return True