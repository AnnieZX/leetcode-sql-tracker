"""
Problem:                Reverse Vowels of a String
LeetCode #:             345
Difficulty:             Easy
Date:                   2026-09-22
Status:                 🟡 Needed Hint
Pattern:                Two Pointers
Time Spent (min):

Key Idea:
    left starts at index 0, right starts at the last index. Advance
    left until it sits on a vowel, advance right until it sits on a
    vowel, swap them, then move both pointers inward. Continue while
    left < right.

What I Missed:
    Solved the shape of the algorithm but couldn't write it independently
    from a blank editor yet — still building fluency with converting a
    mutable-list swap into working Python (strings are immutable, so
    operate on list(s) and "".join() at the end).

Recognition Clue:
    "Swap/reorder characters in place, from both ends inward" -> Two
    Pointers, one starting at each end, moving toward the middle.

Time Complexity:  O(n)
Space Complexity: O(n) (string -> list conversion)

Review Schedule:
    [ ] 3-day review  (2026-09-25)
    [ ] 7-day review  (2026-09-29)
    [ ] 30-day review (2026-10-22)
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)
        left, right = 0, len(chars) - 1
        while left < right:
            if chars[left] not in vowels:
                left += 1
            elif chars[right] not in vowels:
                right -= 1
            else:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        return "".join(chars)
