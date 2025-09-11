```python
# 895. Maximum Frequency Stack - Hash Tables and Stacks Approach
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)  # Frequency of each element
        self.group = defaultdict(list)  # Map frequency to a stack of elements with that frequency
        self.max_freq = 0  # Keep track of the maximum frequency


    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.max_freq = max(self.max_freq, f)
        self.group[f].append(val)


    def pop(self) -> int:
        val = self.group[self.max_freq].pop()  # Pop from the stack with max frequency
        self.freq[val] -= 1

        if not self.group[self.max_freq]:  # If the stack for max_freq is empty, decrement max_freq
            self.max_freq -= 1

        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
```

```markdown
# 895. Maximum Frequency Stack, Difficulty: Hard

## Problem Description

Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the `FreqStack` class:

*   `FreqStack()` constructs an empty frequency stack.
*   `void push(int val)` pushes an integer `val` onto the top of the stack.
*   `int pop()` removes and returns the most frequent element in the stack.
    *   If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].

Constraints:

0 <= val <= 109
At most 2 * 104 calls will be made to push and pop.
It is guaranteed that there will be at least one element in the stack before calling pop.

## Approach(es)

### Hash Tables and Stacks

Algorithm:

1.  **Data Structures:**
    *   `freq`: A hash table (dictionary in Python) to store the frequency of each element (`element -> frequency`).
    *   `group`: A hash table (dictionary in Python) to map frequencies to stacks of elements.  `group[f]` is a stack containing all elements that have frequency `f`.
    * `max_freq`: An integer to keep track of the maximum frequency seen so far.
2.  **`push(val)`:**
    *   Increment the frequency of `val` in the `freq` dictionary.
    *   Get the new frequency `f` of `val`.
    *   Update `max_freq` to be the maximum of its current value and `f`.
    *   Append `val` to the stack associated with frequency `f` in the `group` dictionary (i.e., `group[f].append(val)`).

3.  **`pop()`:**
    *   Get the value `val` from the top of the stack associated with `max_freq` in `group`: `val = group[max_freq].pop()`.
    *   Decrement the frequency of `val` in the `freq` dictionary.
    *   If the stack associated with `max_freq` becomes empty, decrement `max_freq`. This ensures we always pop from the highest frequency stack.
    *   Return `val`.

Data Structures:

*   Hash Tables (Dictionaries in Python)
*   Stacks (Lists in Python)

Time Complexity:

*   `push(val)`: O(1) - Hash table operations and stack push are constant time on average.
*   `pop()`: O(1) - Hash table operations and stack pop are constant time on average.

Space Complexity:

*   O(n), where n is the number of elements pushed onto the stack. In the worst case, all elements are distinct, and we'll store them in both `freq` and `group`.

Trade-offs:
* This approach guarantees O(1) time for both push and pop operations which make it a good choice.
* Memory can grow if too many elements are added, but complexity will remain O(n)

## Code

```python
# 895. Maximum Frequency Stack - Hash Tables and Stacks Approach
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)  # Frequency of each element
        self.group = defaultdict(list)  # Map frequency to a stack of elements with that frequency
        self.max_freq = 0  # Keep track of the maximum frequency


    def push(self, val: int) -> None:
        self.freq[val] += 1
        f = self.freq[val]
        self.max_freq = max(self.max_freq, f)
        self.group[f].append(val)


    def pop(self) -> int:
        val = self.group[self.max_freq].pop()  # Pop from the stack with max frequency
        self.freq[val] -= 1

        if not self.group[self.max_freq]:  # If the stack for max_freq is empty, decrement max_freq
            self.max_freq -= 1

        return val
```

## Notes

*   This problem is a good example of using multiple data structures (hash tables and stacks) in combination to achieve a desired functionality efficiently.
*   The `group` hash table cleverly organizes elements by their frequency, allowing us to quickly access the most frequent elements.
* Using defaultdict simplifies the code.
* The use of stacks within `group` ensures the "closest to the top" tie-breaking rule is followed.

```
**Step 5: Topic Extraction and Files**

*Prompt:* Topic Extraction.
*Analysis:* The relevant topics are "Stack", "Hash Table", and "Design".

* `Stack.md`: (already exists, reuse)
* `Hash Table.md`: (already exists, reuse)
* `Design.md`: (already exists, reuse)
This solution provides a complete, well-documented, and efficient solution for the "Maximum Frequency Stack" problem using hash tables and stacks, along with a detailed README and links to all relevant topics.  It follows all instructions and coding best practices.
