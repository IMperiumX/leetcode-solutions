# 78. Subsets - Iterative Approach


def subsets(nums):
    """
    Generates all possible subsets of a given set of numbers using an iterative approach.

    Args:
      nums: A list of unique integers.

    Returns:
      A list of lists, where each inner list represents a subset.
    """
    result = [[]]  # Start with an empty subset

    for num in nums:
        new_subsets = []
        for subset in result:
            new_subsets.append(
                subset + [num]
            )  # Create new subsets by adding the current number
        result.extend(new_subsets)  # Add the new subsets to the result

    return result
