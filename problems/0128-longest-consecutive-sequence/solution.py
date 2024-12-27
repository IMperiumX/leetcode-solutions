# problems/0128-longest-consecutive-sequence/solution.py
# 128. Longest Consecutive Sequence - Using a Set for O(n) Time

"""
This solution achieves O(n) time complexity by using a set to efficiently check for the presence of numbers.

Convert to Set: The input list nums is converted into a set num_set for fast lookups (checking if a number exists).

Iterate and Find Start of Sequences: The code iterates through each num in the num_set.
The condition if num - 1 not in num_set: checks if the current number is the starting
point of a consecutive sequence. If num - 1 is not in the set, it means num is the smallest
 number in its potential consecutive sequence.

Extend the Sequence: If num is the start of a sequence, the inner while loop extends
the sequence by checking if current_num + 1 exists in the set. It increments
current_streak for each consecutive element found.

Track Longest Streak: The longest_streak variable keeps track of the
maximum consecutive sequence length found so far.

By only starting the sequence count from numbers that are the beginning of a sequence,
it avoids redundant counting and ensures an O(n) time complexity overall.
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in an unsorted array.

        This approach uses a set to efficiently check for the presence of elements and achieves O(n) time complexity.
        """
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            if num - 1 not in num_set:  # Check if 'num' is the start of a sequence
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
