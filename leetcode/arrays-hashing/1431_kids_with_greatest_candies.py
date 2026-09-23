"""
Problem:                Kids With the Greatest Number of Candies
LeetCode #:             1431
Difficulty:             Easy
Date:                   2026-09-22
Status:                 🟢 Independent
Pattern:                Precompute Maximum
Time Spent (min):

Key Idea:
    Instead of comparing every kid against every other kid (O(n^2)),
    compute max(candies) once, then check whether each kid's
    candies + extraCandies would reach or beat that max.

What I Missed:


Recognition Clue:
    "Would X be the greatest if given Y more" -> precompute the current
    max once rather than recomputing/comparing pairwise.

Time Complexity:  O(n)
Space Complexity: O(n) for the output list

Review Schedule:
    [ ] 3-day review  (YYYY-MM-DD)
    [ ] 7-day review  (YYYY-MM-DD)
    [ ] 30-day review (YYYY-MM-DD)
"""


class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        greatest = max(candies)
        return [candy + extraCandies >= greatest for candy in candies]
