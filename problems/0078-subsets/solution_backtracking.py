# 78. Subsets - Backtracking Approach

def subsets(nums):
    """
    Generates all possible subsets of a given set of numbers using a backtracking approach.

    Args:
      nums: A list of unique integers.

    Returns:
      A list of lists, where each inner list represents a subset.
    """
    result = []

    def backtrack(index, current_subset):
        """
        Recursive helper function for backtracking.

        Args:
          index: The current index in the nums array.
          current_subset: The current subset being built.
        """
        result.append(current_subset[:])  # Add a copy of the current subset to the result

        for i in range(index, len(nums)):
            current_subset.append(nums[i])  # Include the current number
            backtrack(i + 1, current_subset)  # Explore further
            current_subset.pop()  # Backtrack: remove the current number

    backtrack(0, [])
    return result
