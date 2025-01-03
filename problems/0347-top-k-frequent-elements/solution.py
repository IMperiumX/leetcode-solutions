"""
347. Top K Frequent Elements - Bucket Sort Approach

Approach:
1. Count the frequency of each element using a dictionary.
2. Create buckets based on frequency (from 1 to the maximum frequency).
3. Place each element in its corresponding frequency bucket.
4. Iterate through the buckets in reverse order (highest frequency to lowest) and collect the elements until we have k elements.
"""

from collections import Counter


def topKFrequent(nums, k):
    """
    Finds the k most frequent elements in a list of integers.

    Args:
        nums: The input list of integers.
        k: The number of most frequent elements to return.

    Returns:
        A list of the k most frequent elements.
    """
    count = Counter(nums)
    buckets = [
        [] for _ in range(len(nums) + 1)
    ]  # Buckets for frequencies 1 to len(nums)

    for num, freq in count.items():
        buckets[freq].append(num)

    result = []
    for bucket in buckets[::-1]:
        for num in bucket:
            result.append(num)
            if len(result) == k:
                return result
