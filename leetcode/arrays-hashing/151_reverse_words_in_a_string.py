"""
Problem:                Reverse Words in a String
LeetCode #:             151
Difficulty:             Medium
Date:                   2026-09-22
Status:                 🟢 Independent
Pattern:                Split -> Reverse -> Join
Time Spent (min):

Key Idea:
    split() with no argument already collapses repeated whitespace and
    strips leading/trailing spaces, so the remaining work is just
    reversing the word list and rejoining with single spaces.

What I Missed:


Recognition Clue:
    "Reverse order of words, normalize whitespace" -> split() handles
    the whitespace normalization for free; don't hand-roll a parser.

Time Complexity:  O(n)
Space Complexity: O(n)

Review Schedule:
    [ ] 3-day review  (YYYY-MM-DD)
    [ ] 7-day review  (YYYY-MM-DD)
    [ ] 30-day review (YYYY-MM-DD)
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        return " ".join(words[::-1])
