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

### Hash Map and Bucket Sort

**Algorithm:**

1. **Count Frequencies:** Create a hash map `counts` to store the frequency of each element in `nums`.
2. **Buckets:** Create a list of buckets `buckets`, where `buckets[i]` will store the elements that have a frequency of `i`. The maximum frequency can be `len(nums)`.
    - Iterate through the `counts` hash map.
    - Append each `element` to the `buckets[frequency]` list.
3. **Collect Result:** Iterate through the `buckets` list in reverse order (from highest frequency to lowest).
    - Append the elements from each bucket to the `result` list until the `result` list has `k` elements.

**Data Structures:**

- Hash Map (`counts`)
- List of lists (`buckets`)

**Time Complexity:**

- O(n) on average, where n is the number of elements in `nums`.
  - O(n) to build the hash map.
  - O(n) to create the buckets.
  - O(n) in the worst case to iterate through the buckets (but often much less in practice).

**Space Complexity:**

- O(n) to store the hash map and the buckets.

**Trade-offs:**

- Very efficient on average (O(n) time complexity).
- Can be less efficient in the worst case if the frequencies are very skewed (e.g., one element appears almost `n` times).
- Simpler to implement than the heap approach.

### Hash Map and Heap (Priority Queue)

**Algorithm:**

1. **Count Frequencies:** Create a hash map `counts` to store the frequency of each element in `nums`.
2. **Min-Heap:** Use a min-heap of size `k` to keep track of the `k` most frequent elements. Store `(frequency, element)` pairs in the heap.
    - Iterate through the `counts` hash map.
    - Push the `(frequency, element)` pair onto the heap.
    - If the heap size exceeds `k`, pop the element with the lowest frequency (the root of the min-heap).
3. **Extract Result:** Pop the elements from the heap and add them to the `result` list. Reverse the list to get the elements in descending order of frequency.

**Data Structures:**

- Hash Map (`counts`)
- Min-Heap (`min_heap`)

**Time Complexity:**

- O(n log k), where n is the number of elements in `nums`.
  - O(n) to build the hash map.
  - O(n log k) to iterate through the hash map and maintain the heap of size `k`.

**Space Complexity:**

- O(n) in the worst case to store the hash map (if all elements are unique).
- O(k) to store the min-heap.

**Trade-offs:**

- Efficient for larger inputs when `k` is much smaller than `n`.
- Uses a heap, which adds some overhead compared to a simpler approach like bucket sort.

## Code

[Hash Map and Heap Approach](./solution_heap.py)

[Hash Map and Bucket Sort Approach](./solution_bucket_sort.py)

## Notes

- The follow-up requirement (better than O(n log n) time complexity) guides us towards using a heap of size `k` (O(n log k)) or bucket sort (O(n)).
- Bucket sort is generally preferred for this problem because of its average O(n) time complexity.
- The choice between the two approaches might depend on factors like the expected distribution of frequencies and the specific constraints of the problem.
- The Bucket Sort approach is particularly efficient when the range of frequencies is relatively small compared to the number of elements.
