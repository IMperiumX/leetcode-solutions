
## Topic: Prefix Sum

A **Prefix Sum** (also known as a cumulative sum, inclusive scan, or running total) is an array where each element is the sum of all preceding elements in an original array, including itself. It's a powerful pre-computation technique that allows for rapid calculation of the sum of any contiguous subarray. ➕

### How It Works

Given an input array `nums`: `[a, b, c, d]`
The corresponding prefix sum array `prefix` would be: `[0, a, a+b, a+b+c, a+b+c+d]`

The prefix sum array is often created with an initial `0` to simplify calculations.
`prefix[i]` stores the sum of the first `i` elements of `nums`.

### Key Advantage

Once the prefix sum array is built, the sum of any subarray `nums[i...j]` can be calculated in constant time, $O(1)$.
**Sum(i, j) = `prefix[j+1] - prefix[i]`**

### Use Cases

* Quickly finding the sum of a range in an array.
* Problems where you repeatedly need to calculate sums of different subarrays.
* As a building block for more complex algorithms, such as those involving binary search on subarray sums.

### Complexity

* **Preprocessing (Building the array):**
  * Time: $O(n)$
  * Space: $O(n)$
* **Query (Sum of a range):**
  * Time: $O(1)$
  * Space: $O(1)$

### Related Problems

* [209. Minimum Size Subarray Sum](../problems/0209-minimum-size-subarray-sum/README.md)
