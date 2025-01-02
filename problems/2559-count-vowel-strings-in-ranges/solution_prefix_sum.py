"""
2559. Count Vowel Strings in Ranges - Prefix Sum Approach

You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present
in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.
"""


def vowelStrings(words, queries):
    vowels = set(["a", "e", "i", "o", "u"])
    prefix_sums = [0] * (len(words) + 1)

    for i, word in enumerate(words):
        if word[0] in vowels and word[-1] in vowels:
            prefix_sums[i + 1] = prefix_sums[i] + 1
        else:
            prefix_sums[i + 1] = prefix_sums[i]

    ans = []
    for l, r in queries:
        ans.append(prefix_sums[r + 1] - prefix_sums[l])

    return ans
