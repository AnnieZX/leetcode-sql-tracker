"""
Problem:                Can Place Flowers
LeetCode #:             605
Difficulty:             Easy
Date:                   2026-09-22
Status:                 🟢 Independent
Pattern:                Linear Scan / Greedy
Time Spent (min):

Key Idea:
    Scan each plot. If it's empty and both neighbors are empty (or off
    the edge), plant a flower there immediately and decrement n. Don't
    bail out early on a single bad position — only decide failure after
    scanning the whole bed.

What I Missed:


Recognition Clue:
    "Can we place N non-adjacent items" over a 1D array -> greedy left-
    to-right scan, planting as soon as it's safe, since planting earlier
    never hurts a later placement.

Time Complexity:  O(n)
Space Complexity: O(1)

Review Schedule:
    [ ] 3-day review  (YYYY-MM-DD)
    [ ] 7-day review  (YYYY-MM-DD)
    [ ] 30-day review (YYYY-MM-DD)
"""


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
        return n <= 0
