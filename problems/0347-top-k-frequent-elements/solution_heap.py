"""
347. Top K Frequent Elements - Hash Map and Heap Approach
"""

import heapq


def topKFrequent_heap(nums: list[int], k: int) -> list[int]:
    """
    Finds the k most frequent elements using a hash map and a min-heap.

    Args:
      nums: The input list of integers.
      k: The number of most frequent elements to return.

    Returns:
      A list of the k most frequent elements.
    """
    counts = {}  # Hash map to store element frequencies
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Use a min-heap to store the top k frequent elements.
    # The heap will store (frequency, element) pairs.
    min_heap = []
    for num, count in counts.items():
        heapq.heappush(min_heap, (count, num))
        if len(min_heap) > k:
            heapq.heappop(
                min_heap
            )  # Remove the least frequent element if size exceeds k

    # Extract the elements from the heap
    result = []
    while min_heap:
        count, num = heapq.heappop(min_heap)
        result.append(num)

    return result[::-1]  # Reverse to get descending order of frequency
