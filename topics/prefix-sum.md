# Prefix Sum

## Description

A prefix sum array is a data structure that helps to efficiently calculate the sum of elements in a range of an array. Given an array `arr`, the prefix sum array `prefix_sum` is an array of the same length where `prefix_sum[i]` stores the sum of the first `i+1` elements of `arr`. In other words:
`prefix_sum[i] = arr[0] + arr[1] + ... + arr[i]`

The Prefix Sum technique, also known as cumulative sum, is a powerful algorithmic approach used to efficiently compute the sum of elements within a given range of an array. It involves creating a new array (prefix sum array) where each element at index `i` stores the sum of all elements in the original array from index 0 up to `i`. This precomputed array allows for constant-time retrieval of the sum of any subarray.

## Algorithm

1. **Initialization:** Create a prefix sum array `prefix_sums` of the same size as the input array `arr`, plus one extra element at the beginning initialized to 0. This extra element simplifies calculations for ranges starting from index 0.
2. **Computation:** Iterate through the input array `arr` from left to right. For each element at index `i`:
    - Calculate the cumulative sum up to that element: `prefix_sums[i + 1] = prefix_sums[i] + arr[i]`.
3. **Range Query:** To find the sum of elements within a range `[l, r]` (inclusive):
    - Calculate the sum as `prefix_sums[r + 1] - prefix_sums[l]`.

## Key Idea

The core idea behind the prefix sum technique is that the sum of any subarray `arr[l:r+1]` can be expressed as the difference between two prefix sums: the sum up to index `r` minus the sum up to index `l-1`.

## Use Cases

Prefix sums are useful in various scenarios, including:

- **Range Sum Queries**: Answering multiple queries about the sum of elements in different ranges of an array.
- **Finding Subarrays with a Given Sum**: Efficiently finding subarrays that satisfy specific sum conditions.
- **Dynamic Programming**: As a building block in dynamic programming solutions.
- **Image Processing**: Calculating cumulative sums in image data.

## Example

Consider the array `arr = [1, 2, 3, 4, 5]`.

1. **Initialization:** `prefix_sums = [0, 0, 0, 0, 0, 0]`
2. **Computation:**
    - `prefix_sums[1] = prefix_sums[0] + arr[0] = 0 + 1 = 1`
    - `prefix_sums[2] = prefix_sums[1] + arr[1] = 1 + 2 = 3`
    - `prefix_sums[3] = prefix_sums[2] + arr[2] = 3 + 3 = 6`
    - `prefix_sums[4] = prefix_sums[3] + arr[3] = 6 + 4 = 10`
    - `prefix_sums[5] = prefix_sums[4] + arr[4] = 10 + 5 = 15`
    - Result: `prefix_sums = [0, 1, 3, 6, 10, 15]`

3. **Range Query:** Find the sum of elements in the range `[1, 3]` (i.e., `[2, 3, 4]`):
    - `sum = prefix_sums[3 + 1] - prefix_sums[1] = prefix_sums[4] - prefix_sums[1] = 10 - 1 = 9`

## Time Complexity

- **Prefix Sum Array Construction:** O(n), where n is the size of the input array.
- **Range Query:** O(1) - constant time.

## Space Complexity

- O(n) to store the prefix sum array.

## Advantages

- **Efficient Range Queries:** Allows for constant-time retrieval of subarray sums.
- **Simple Implementation:** The algorithm is relatively straightforward to implement.
- **Versatile:** Can be extended to higher dimensions (e.g., 2D prefix sum for matrices).

## Limitations

- **Extra Space:** Requires additional space to store the prefix sum array.
- **Not Suitable for Frequent Updates:** If the original array is frequently modified, the prefix sum array needs to be recomputed, which can be time-consuming.

## Example (Python)

```python
def build_prefix_sum(arr):
  """Builds a prefix sum array from the given array."""
  n = len(arr)
  prefix_sums = [0] * (n + 1)
  for i in range(n):
    prefix_sums[i + 1] = prefix_sums[i] + arr[i]
  return prefix_sums

def range_sum_query(prefix_sums, l, r):
  """Calculates the sum of elements in the range [l, r] using the prefix sum array."""
  return prefix_sums[r + 1] - prefix_sums[l]

# Example usage
arr = [1, 2, 3, 4, 5]
prefix_sums = build_prefix_sum(arr)

print("Prefix Sums:", prefix_sums)

l = 1
r = 3
sum_range = range_sum_query(prefix_sums, l, r)
print(f"Sum of elements in range [{l}, {r}]: {sum_range}")
```

## Related LeetCode Problems

- [238. Product of Array Except Self](./../problems/0238-product-of-array-except-self/README.md)
- [303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)
- [304. Range Sum Query 2D - Immutable](https://leetcode.com/problems/range-sum-query-2d-immutable/)
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)
- [1413. Minimum Value to Get Positive Step by Step Sum](https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/)
- [2270. Number of Ways to Split Array](https://leetcode.com/problems/number-of-ways-to-split-array/)
- [2559. Count Vowel Strings in Ranges](./2559-count-vowel-strings-in-ranges/README.md)
