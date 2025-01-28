"""
FIXME
3223. Minimum Length of String After Operations - Stack-based Approach

This problem requires careful consideration of how to optimally choose the indices for operations.
A greedy approach might seem tempting, but it's not guaranteed to yield the minimum length.
Since the string can be up to 2 * 10^5 characters long, a dynamic programming or a more
sophisticated approach might be needed for an optimal solution.

I will implement a solution using a stack-based approach. Here's how it works:

1. We iterate through the string, maintaining a stack of indices.
2. If the current character matches the character at the top of the stack, it means we have a potential operation.
3. We find the nearest left and right matching characters and mark them for deletion.
4. We continue this process until no more operations can be performed.
5. Finally, we count the number of characters that were not marked for deletion.

"""


def minLength(s: str) -> int:
    """
    Calculates the minimum length of the string after performing the operations.

    Args:
      s: The input string.

    Returns:
      The minimum length of the string after operations.
    """
    n = len(s)
    deleted = [False] * n
    stack = []

    for i in range(n):
        if stack and s[stack[-1]] == s[i]:
            # Find nearest left and right
            left = -1
            for j in range(stack[-1] - 1, -1, -1):
                if not deleted[j] and s[j] == s[i]:
                    left = j
                    break
            right = -1
            for j in range(i + 1, n):
                if not deleted[j] and s[j] == s[i]:
                    right = j
                    break

            if left != -1 and right != -1:
                deleted[left] = True
                deleted[right] = True
                stack.pop()
                continue

        stack.append(i)

    count = 0
    for i in range(n):
        if not deleted[i]:
            count += 1

    return count
if __name__ == "__main__":
    min_length = minLength("aabccabba")
    print(min_length)
