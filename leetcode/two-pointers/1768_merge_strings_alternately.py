"""
Problem:                Merge Strings Alternately
LeetCode #:             1768
Difficulty:             Easy
Date:                   2026-09-22
Status:                 🟢 Independent
Pattern:                Two Pointers
Time Spent (min):

Key Idea:
    Walk both strings with a pointer each, appending one character from
    each in turn. Once one string runs out, append whatever remains of
    the other.

What I Missed:


Recognition Clue:
    "Merge two sequences by alternating elements" -> two pointers walking
    in lockstep, with a tail case for whichever sequence is longer.

Time Complexity:  O(n + m)
Space Complexity: O(n + m)

Review Schedule:
    [ ] 3-day review  (YYYY-MM-DD)
    [ ] 7-day review  (YYYY-MM-DD)
    [ ] 30-day review (YYYY-MM-DD)
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1
        result.append(word1[i:])
        result.append(word2[j:])
        return "".join(result)
