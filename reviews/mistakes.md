# Mistake Log

A running log of problems that didn't go well, so the same gap doesn't get missed twice. Add an entry any time a problem is marked 🟡 or 🔴.

## Template

```
### [Problem Name]

- **Date:** YYYY-MM-DD
- **Pattern:** e.g. Sliding Window
- **What went wrong:**
- **Pattern missed:**
- **Recognition clue:** (what should have signaled this pattern next time)
- **Current status:** 🔴 Not Started / 🟡 Needs Review / 🟢 Resolved

---
```

## Entries

### 345. Reverse Vowels of a String

- **Date:** 2026-09-22
- **Pattern:** Two Pointers
- **What went wrong:** Understood the general idea (move pointers inward, swap vowels) but couldn't implement it independently from a blank editor yet.
- **Pattern missed:** Two Pointers on a mutable copy of the string (strings are immutable in Python, so convert to `list(s)` first, then `"".join(chars)` at the end).
- **Recognition clue:** Any problem asking to reorder/swap characters in-place from both ends is a signal for Two Pointers (left starts at 0, right starts at len-1, move inward).
- **Current status:** 🟡 Needs Review (3-day: 2026-09-25, 7-day: 2026-09-29, 30-day: 2026-10-22)

---
