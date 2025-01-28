# Bucket Sort

Bucket Sort is a non-comparison-based sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm (like Insertion Sort) or by recursively applying Bucket Sort. Finally, the elements from the buckets are gathered back into the original array in sorted order.

Bucket sort, or bin sort, is a sorting algorithm that works by distributing the elements of an array into a number of buckets. Each bucket is then sorted individually, either using a different sorting algorithm or by recursively applying the bucket sorting algorithm. It is a distribution sort, a generalization of pigeonhole sort that allows multiple keys per bucket, and is a cousin of radix sort in the most-to-least significant digit flavor.

Bucket sort is mainly useful when input is uniformly distributed over a range. When the input contains several keys that are close to each other (clustering), those elements are likely to be placed in the same bucket, which results in some buckets containing more elements than others. The worst-case scenario occurs when all the elements are placed in a single bucket.

## Key Concepts

- **Buckets:** The input array is divided into a number of "buckets" or sub-arrays.
- **Distribution:** Each element from the input array is placed into a bucket based on a certain criteria (e.g., a range of values).
- **Sorting Buckets:** Each bucket is sorted individually using another sorting algorithm (often Insertion Sort) or by recursively applying Bucket Sort.
- **Gathering:** The sorted elements from the buckets are concatenated back into the original array in order.

## Algorithm

1. **Create Buckets:** Create an array of empty buckets. The number of buckets can be determined based on the range of input values and the desired distribution.
2. **Scatter:** Iterate through the input array and place each element into the appropriate bucket based on its value.
3. **Sort Buckets:** Sort each non-empty bucket using a sorting algorithm (e.g., Insertion Sort).
4. **Gather:** Iterate through the buckets in order and concatenate the elements from each bucket back into the original array.

## Time Complexity

- **Average Case:** O(n + k), where n is the number of elements to be sorted and k is the number of buckets. This assumes that the elements are uniformly distributed across the buckets.
- **Worst Case:** O(n^2) if all elements fall into the same bucket and the sorting algorithm used for the buckets is Insertion Sort (or another O(n^2) algorithm).
- **Best Case:** O(n + k) if the elements are uniformly distributed and the number of buckets is proportional to the number of elements.

## Space Complexity

- O(n + k), where n is the number of elements and k is the number of buckets.

## Applications

- **Sorting data that is uniformly distributed over a range.**
- **External sorting (when data does not fit in memory).**
- **When the number of unique values is relatively small compared to the number of elements.**

## Trade-offs

- **Advantages:**
  - Can be very efficient (linear time) when the data is uniformly distributed.
  - Relatively easy to implement.
- **Disadvantages:**
  - Performance degrades significantly if the data is not uniformly distributed (can become O(n^2) in the worst case).
  - Not suitable for all types of data (works best for numerical data or data that can be mapped to numerical ranges).
  - Requires extra space for the buckets.

## Related LeetCode Problems

- [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) (can be solved using a variation of Bucket Sort)
- [164. Maximum Gap](https://leetcode.com/problems/maximum-gap/) (can be solved using Bucket Sort)
- [451. Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/) (can be solved using Bucket Sort)
- [791. Custom Sort String](https://leetcode.com/problems/custom-sort-string/) (can be solved using Bucket Sort)
