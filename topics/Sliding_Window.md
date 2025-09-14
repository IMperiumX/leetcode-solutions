
## Topic: Sliding Window

The **Sliding Window** is an algorithmic technique used for problems that involve processing a contiguous subarray or substring of a given array or string. It maintains a "window" (a sub-list) that slides over the data, adjusting its size by moving its start and end pointers. 🪟

### Core Idea

Instead of re-computing values for overlapping subarrays (like a brute-force approach would), the sliding window reuses the computation from the previous window. It *slides* the window by adding an element at one end and removing an element from the other, updating the result in constant or near-constant time.

### When to Use It

This pattern is particularly useful for problems that ask for something like:

* The longest/shortest/minimum/maximum subarray or substring that satisfies a certain condition.
* The number of subarrays/substrings that meet a criteria.
* Problems involving contiguous sequences.

### Types of Sliding Windows

1. **Fixed-Size Window:** The window size `k` is constant. The `end` pointer moves forward, and the `start` pointer follows to maintain the size.
2. **Variable-Size Window:** The window size changes based on a condition. The `end` pointer always expands the window, and the `start` pointer contracts it only when a certain condition is met (e.g., the sum within the window exceeds a target).

### Complexity

* **Time Complexity:** Typically $O(n)$, as each pointer (`start` and `end`) traverses the array only once.
* **Space Complexity:** Usually $O(1)$ if only a few variables are needed, or $O(k)$ if a hash map or similar structure is used to store the contents of the window of size `k`.

### Related Problems

* [209. Minimum Size Subarray Sum](../problems/0209-minimum-size-subarray-sum/README.md)
