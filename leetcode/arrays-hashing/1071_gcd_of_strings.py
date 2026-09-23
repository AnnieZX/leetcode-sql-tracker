"""
Problem:                Greatest Common Divisor of Strings
LeetCode #:             1071
Difficulty:             Easy
Date:                   2026-09-22
Status:                 🟢 Independent
Pattern:                Math / String manipulation
Time Spent (min):

Key Idea:
    A common divisor string x must satisfy str1 + str2 == str2 + str1
    (otherwise no such x can exist). If that holds, the answer is the
    prefix of length gcd(len(str1), len(str2)).

What I Missed:


Recognition Clue:
    "Divisor" of a string == a substring that can be repeated to build
    it. Two strings share a divisor only if concatenating them in
    either order gives the same result.

Time Complexity:  O(n + m)
Space Complexity: O(n + m)

Review Schedule:
    [ ] 3-day review  (YYYY-MM-DD)
    [ ] 7-day review  (YYYY-MM-DD)
    [ ] 30-day review (YYYY-MM-DD)
"""

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = math.gcd(len(str1), len(str2))
        return str1[:gcd_len]
