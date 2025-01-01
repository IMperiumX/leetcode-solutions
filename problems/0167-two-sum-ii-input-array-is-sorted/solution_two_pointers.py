# 167. Two Sum II - Input Array Is Sorted - Two Pointers Approach


def twoSum(numbers, target):
    """
    Finds two numbers in a sorted array that add up to a specific target using the two-pointer approach.

    Args:
        numbers: A 1-indexed array of integers sorted in non-decreasing order.
        target: The target sum.

    Returns:
        A list [index1, index2] representing the 1-indexed indices of the two numbers.
    """
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed indices
        elif current_sum < target:
            left += 1  # Need a larger sum
        else:
            right -= 1  # Need a smaller sum

    return []  # Should not reach here as the problem states there is exactly one solution
