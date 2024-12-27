# 347. Top K Frequent Elements, Difficulty: Medium

## Problem Description

Given an integer array `nums` and an integer `k`, return the *k* most frequent elements. You may return the answer in **any order**.

**Example 1:**

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

**Example 2:**

Input: nums = [1], k = 1
Output: [1]

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is guaranteed that the answer is unique.

**Follow up:** Your algorithm's time complexity must be better than *O*(*n* log *n*), where *n* is the array's size.

## Approach

The solution utilizes the **Bucket Sort** approach to achieve a time complexity better than O(n log n).

1. **Frequency Counting:** We first count the frequency of each element in the input array `nums` using a dictionary (hash map).
2. **Bucket Creation:** We create a list of buckets, where each bucket represents a frequency. The index of the bucket corresponds to the frequency.
3. **Bucket Filling:** We iterate through the frequency dictionary and place each element into the bucket corresponding to its frequency.
4. **Result Gathering:** We iterate through the buckets in reverse order (from highest frequency to lowest). For each bucket, we add its elements to the result list until we have collected `k` elements.

**Time Complexity:** O(n), where n is the length of the input array `nums`. We iterate through the array once to count frequencies, and then iterate at most `n` times when creating and traversing the buckets.

**Space Complexity:** O(n) in the worst case, where we might have `n` unique elements, requiring space for the frequency dictionary and buckets.

## Code

### Python - Bucket Sort

[solution](./solution.py)

## Notes

Another common approach is to use a **Min-Heap** (Priority Queue) of size k. This approach has a time complexity of O(n log k), which is also acceptable for this problem, though slightly less efficient than Bucket Sort.

The Bucket Sort approach is particularly efficient when the range of frequencies is relatively small compared to the number of elements.
