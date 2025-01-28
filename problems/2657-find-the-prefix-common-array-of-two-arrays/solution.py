"""
2657. Find the Prefix Common Array of Two Arrays
"""

def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
    """
    Finds the prefix common array of two arrays A and B.

    Args:
      A: The first permutation array.
      B: The second permutation array.

    Returns:
      The prefix common array C.
    """
    n = len(A)
    C = [0] * n
    for i in range(n):
        setA = set(A[:i+1])
        setB = set(B[:i+1])
        common_count = len(setA.intersection(setB))
        C[i] = common_count
    return C
