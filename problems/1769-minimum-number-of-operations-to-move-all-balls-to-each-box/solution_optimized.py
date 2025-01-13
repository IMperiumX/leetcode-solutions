"""
1769. Minimum Number of Operations to Move All Balls to Each Box - Optimized Approach
"""


def minOperations_optimized(boxes: str) -> list[int]:
    """
    Calculates the minimum operations to move all balls to each box (optimized).

    Args:
      boxes: A binary string representing the boxes (1: ball, 0: empty).

    Returns:
      A list of integers, where each element represents the minimum operations for that box.
    """
    n = len(boxes)
    answer = [0] * n

    # Calculate initial operations for the first box
    left_count = 0
    left_cost = 0
    for i in range(1, n):
        if boxes[i - 1] == "1":
            left_count += 1
        left_cost += left_count
        answer[i] = left_cost

    # Calculate operations for other boxes based on the previous box
    right_count = 0
    right_cost = 0
    for i in range(n - 2, -1, -1):
        if boxes[i + 1] == "1":
            right_count += 1
        right_cost += right_count
        answer[i] += right_cost

    return answer
