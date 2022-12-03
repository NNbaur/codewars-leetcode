# Given a string s, find the length of
# the longest substring without repeating characters.
#
# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution1:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        res = 0
        l_ind = 0
        r_ind = 1
        ss = s[l_ind] if len(s) > 0 else ''
        if len(s) == 1:
            return 1
        while r_ind < len(s):
            if s[r_ind] not in ss:
                ss += s[r_ind]
                r_ind += 1
            else:
                l_ind += 1
                r_ind = l_ind + 1
                ss = s[l_ind]
            res = max(res, len(ss))
        return res


class Solution2:
    def lengthOfLongestSubstring2(self, s: str) -> int:
        set_chars = set()
        res = 0
        l_ind = 0

        for r in range(len(s)):
            while s[r] in set_chars:
                set_chars.remove(s[l_ind])
                l_ind += 1
            set_chars.add(s[r])
            res = max(res, r - l_ind + 1)
        return res
