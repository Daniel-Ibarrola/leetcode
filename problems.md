### Module 1 – Basic Coding

- [1672. Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/)
- [1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)
- [CodeSignal: Add Border](https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm)

### Module 2 – Data Manipulation

- [2810. Faulty Keyboard](https://leetcode.com/problems/faulty-keyboard/)
- [1374. Generate a String With Characters That Have Odd Counts](https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/)
- [CodeSignal: Are Following Patterns](https://app.codesignal.com/interview-practice/task/h8XNjj6bzskoD3hPS)

### Module 3 – Implementation Efficiency

- [CodeSignal: Sudoku](https://app.codesignal.com/arcade/intro/level-7/ZMR5n7zvQcuju8bP2)
- [79. Word Search](https://leetcode.com/problems/word-search/)

### Module 4 – Problem Solving

- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [974. Subarray Sums Divisible by K](https://leetcode.com/problems/subarray-sums-divisible-by-k/)
- [CodeSignal: Is Sum of Consecutive](https://app.codesignal.com/interview-practice/task/Y8jQd7PnuKHkuyjz4)


✅ How to Get Better (Tactical Plan)

1. Deliberate Practice: Pattern-Based

Focus on problem types, not just problems.
	•	Prefix sum + hash map
	•	Problems like: Subarray sum equals K, Count nice subarrays, Range sum queries
	•	Frequency maps
	•	Problems like: Two sum, K-diff pairs, Majority elements
	•	Sliding window + sets/maps
	•	Problems like: Longest substring without repeating characters, Minimum window substring
	•	State tracking
	•	Problems like: Number of subarrays divisible by K, Balance of 0s and 1s, etc.

🛠 Practice Strategy:
	•	Solve 3–5 problems per category.
	•	After each, explicitly write down:
	•	“What was the key insight?”
	•	“What data structure helped and what did it store?”

⸻

2. Redesign the Brute Force First

Don’t skip it! Writing or simulating a brute-force solution:
	•	Helps you identify repeated computation
	•	Shows which parts vary and which parts don’t
	•	Suggests what can be stored to avoid recomputation

Once you spot redundancy, ask:

“Can I precompute this?”
“Can I cache it?”
“Can I represent this evolving state more compactly?”

⸻

3. Work Backward from Examples

Take a small input (like [1,2,3]) and manually trace:
	•	The brute force pairs
	•	The cumulative data (like prefix sum)
	•	When/where the condition is met

Ask:

“What must be true before I reach this element for the condition to hold?”

This is often how you discover what you should track in a hash map.

⸻

4. Study Editorials & Re-implement

After solving a problem (or seeing the solution), don’t just move on. Try this:
	•	Close the solution.
	•	Re-implement from scratch 1–2 days later.
	•	Force yourself to rederive the key insight.
	•	If you can’t, re-read the solution and explain it out loud or write a comment block about it.

⸻

5. Keep a “Tricks Notebook”

Every time you solve an optimized solution using a hash table, sliding window, or prefix sum:
	•	Write down the name of the problem
	•	What structure you used
	•	What you stored and why
	•	The key insight that made it click

This builds your intuition library.
