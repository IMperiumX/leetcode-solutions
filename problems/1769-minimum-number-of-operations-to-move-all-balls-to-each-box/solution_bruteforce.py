"""
1.    Minimum Number of Operations to Move All Balls to Each Box - Brute Force Approach
"""


def minOperations_bruteforce(boxes: str) -> list[int]:
    """
    Calculates the minimum operations to move all balls to each box (brute force).

    Args:
      boxes: A binary string representing the boxes (1: ball, 0: empty).

    Returns:
      A list of integers, where each element represents the minimum operations for that box.
    """
    n = len(boxes)
    answer = []
    for i in range(n):
        operations = 0
        for j in range(n):
            if boxes[j] == "1":
                operations += abs(i - j)
        answer.append(operations)
    return answer

minOperations_bruteforce("110")  # Output: [1, 1, 3]
