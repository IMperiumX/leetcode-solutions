# 20. Valid Parentheses - Stack Approach


def isValid(s: str) -> bool:
    """
    Checks if the input string containing parentheses is valid.

    Args:
        s: The input string.

    Returns:
        True if the string is valid, False otherwise.
    """
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:  # If it's a closing bracket
            top_element = (
                stack.pop() if stack else "#"
            )  # Pop from stack, or use '#' as a placeholder
            if mapping[char] != top_element:
                return False  # Mismatch
        else:
            stack.append(char)  # Push opening brackets onto the stack

    return not stack  # The stack should be empty if all brackets are matched
