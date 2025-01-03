def ways_to_split_array(nums: list[int]) -> int:
    """
    Calculates the number of valid splits in an array.

    A split is valid if the sum of the first i+1 elements is greater than or
    equal to the sum of the last n-i-1 elements, and there's at least one
    element to the right of i.

    Args:
        nums: The input array of integers.

    Returns:
        The number of valid splits.
    """
    n = len(nums)
    total_sum = sum(nums)
    left_sum = 0
    count = 0

    for i in range(n - 1):
        left_sum += nums[i]
        right_sum = total_sum - left_sum
        if left_sum >= right_sum:
            count += 1

    return count
