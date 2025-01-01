# 167. Two Sum II - Input Array Is Sorted - Binary Search Approach

def twoSum(numbers, target):
    """
    Finds two numbers in a sorted array that add up to a specific target using binary search.

    Args:
        numbers: A 1-indexed array of integers sorted in non-decreasing order.
        target: The target sum.

    Returns:
        A list [index1, index2] representing the 1-indexed indices of the two numbers.
    """

    for i in range(len(numbers)):
        complement = target - numbers[i]
        left, right = i + 1, len(numbers) - 1

        # Binary search for the complement
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] == complement:
                return [i + 1, mid + 1]  # 1-indexed indices
            elif numbers[mid] < complement:
                left = mid + 1
            else:
                right = mid - 1

    return []  # Should not reach here as the problem states there is exactly one solution
