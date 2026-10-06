# Technical Interview Prep

Tracking my preparation for 2027 New Grad technical interviews across Software Engineering, Product Engineering, AI/ML Engineering, and Data roles.

**Started:** September 19, 2026

> Learn patterns, not solutions. Consistency over problem count.

## Overall Goals

- LeetCode: 5 / 75
- SQL: 10 / 40

## Current Focus

- Array/String fundamentals (Python syntax fluency over problem count)
- Two Pointers (currently learning)
- SQL Fundamentals

## LeetCode Pattern Readiness

| Pattern | Status |
|---|---|
| Arrays & Hashing | 🟡 In Progress |
| Two Pointers | 🟡 In Progress |
| Sliding Window | 🔴 Not Started |
| Stack | 🔴 Not Started |
| Binary Search | 🔴 Not Started |
| Linked List | 🔴 Not Started |
| Trees | 🔴 Not Started |
| Heap / Priority Queue | 🔴 Not Started |
| Graphs | 🔴 Not Started |
| Dynamic Programming | 🔴 Not Started |

## SQL Readiness

| Topic | Status |
|---|---|
| SELECT / WHERE | 🟡 In Progress |
| GROUP BY / HAVING | 🟡 In Progress |
| JOIN | 🟡 In Progress |
| CASE WHEN | 🔴 Not Started |
| CTE / Subqueries | 🔴 Not Started |
| Window Functions | 🔴 Not Started |

## This Week

- [x] 1768 Merge Strings Alternately
- [x] 1071 Greatest Common Divisor of Strings
- [x] 1431 Kids With the Greatest Number of Candies
- [x] 605 Can Place Flowers
- [x] 151 Reverse Words in a String
- [ ] 345 Reverse Vowels of a String (in progress — Two Pointers)
- [ ] 238 Product of Array Except Self
- [ ] 334 Increasing Triplet Subsequence
- [ ] 443 String Compression
- [ ] Build Python syntax fluency; hold off on more Mediums until Easy problems can be written independently

## Review System

Each problem is tagged with a status reflecting how it was solved:

- 🟢 = can solve independently
- 🟡 = understand but need review / needed a hint
- 🔴 = could not solve independently

Problems marked 🟡 or 🔴 are scheduled for spaced review at **3, 7, and 30 days** after first attempt, using the checkboxes in [`templates/leetcode-template.py`](templates/leetcode-template.py) and [`templates/sql-template.sql`](templates/sql-template.sql). See [`reviews/mistakes.md`](reviews/mistakes.md) for the mistake log, [`reviews/weekly-review.md`](reviews/weekly-review.md) for weekly retrospectives, and [`reviews/python-concepts.md`](reviews/python-concepts.md) for a running Python syntax/pattern reference sheet.

## Weekly Progress

| Week | Dates | LeetCode Solved | SQL Solved | Independent Solve Rate | Notes |
|---|---|---|---|---|---|
| 1 | 2026-09-19 – 2026-09-25 | 5 | 0 | 100% (5/5) | Array/String basics; bottleneck is Python syntax fluency, not algorithm recognition |
| 3 | 2026-10-03 – 2026-10-09 | 0 | 10 | — | 2026-10-05: SQL Select, Basic Joins, Basic Aggregate Functions (SELECT/WHERE, DISTINCT, AS, ORDER BY, LENGTH(), INNER/LEFT JOIN, LEFT JOIN + IS NULL, GROUP BY/COUNT, self joins, DATEDIFF) |

## Repository Structure

```
leetcode/       # Solutions organized by pattern
sql/            # SQL practice organized by topic
templates/      # Reusable templates for new problems
reviews/        # Mistake log, weekly reviews, Python concepts reference
tracker.csv     # Master log of every problem attempted
```
