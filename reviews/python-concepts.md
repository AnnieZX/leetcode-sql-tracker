# Python Concepts Review Sheet

A running reference of Python syntax/functions learned while solving problems, so implementation ideas don't need to be re-derived from scratch each time. Add new entries as they come up; don't remove old ones even once they feel obvious.

## Log

### 2026-09-22 — Array/String basics

1. **`len()`**
   ```python
   len(nums)
   ```
   Returns the length of a string/list.

2. **`range()`**
   ```python
   for i in range(len(nums)):
       print(nums[i])
   ```
   Iterate over indices.

3. **List indexing**
   ```python
   nums[i]
   nums[i - 1]
   nums[i + 1]
   ```

4. **List creation**
   ```python
   result = []
   ```

5. **`append()`**
   ```python
   result.append(True)
   ```
   Add an element to the end of a list.

6. **`max()`**
   ```python
   greatest = max(candies)
   ```
   Get the maximum value in an iterable.

7. **`split()`**
   ```python
   words = s.split()
   ```
   - Converts a string into a list of words.
   - With no argument, automatically handles leading/trailing spaces and repeated whitespace.

8. **`join()`**
   ```python
   " ".join(words)
   "".join(chars)
   ```
   - Joins list elements into a string.
   - `" "` inserts spaces between elements; `""` inserts nothing.

9. **Slicing**
   ```python
   sequence[start:stop:step]

   words[::-1]        # start omitted, stop omitted, step = -1 -> traverse backwards
   [1, 2, 3, 4][::-1] # -> [4, 3, 2, 1]
   ```

10. **`list()`**
    ```python
    chars = list(s)
    ```
    Convert an immutable string into a mutable list of characters when individual characters need to be changed.

11. **Membership operators**
    ```python
    vowels = "aeiouAEIOU"
    if chars[left] not in vowels:
        left += 1
    ```
    `in` / `not in` for membership checks.

12. **`+=` and `-=`**
    ```python
    left += 1
    right -= 1
    n -= 1
    ```

13. **Tuple-style swapping**
    ```python
    chars[left], chars[right] = chars[right], chars[left]
    ```
    Swap two values without a temporary variable.

14. **Boolean operators**
    ```python
    left_empty and right_empty
    i == 0 or flowerbed[i - 1] == 0
    ```

15. **String immutability**
    ```python
    # Not allowed:
    s[i] = "x"

    # Instead:
    chars = list(s)
    # ... modify chars ...
    result = "".join(chars)
    ```

## Algorithm Patterns Learned

### Linear Scan / Greedy — *Can Place Flowers (605)*
- Scan each position; check whether current, left, and right positions allow planting.
- If valid, plant immediately and decrement `n`.
- Don't return `False` just because one position fails — only determine failure after all candidates are checked.
- Time O(n), Space O(1).

### Precompute Maximum — *Kids With the Greatest Number of Candies (1431)*
- Instead of comparing every child against every other child (O(n²)), compute `max(candies)` once, then compare `candies[i] + extraCandies` against it.
- Time O(n).

### Split → Reverse → Join — *Reverse Words in a String (151)*
```
string -> split() -> list of words -> [::-1] -> reversed words -> " ".join(...) -> output string
```
- Time O(n).

### Two Pointers — *Reverse Vowels of a String (345)* — 🟡 Learning, not mastered
- `left` moves from the beginning toward the center; `right` moves from the end toward the center.
- Move `left` until it finds a vowel, move `right` until it finds a vowel, swap them, move both pointers inward.
- Continue while `left < right`.
- Status: pattern introduced but not yet solved independently — see [`reviews/mistakes.md`](mistakes.md).
