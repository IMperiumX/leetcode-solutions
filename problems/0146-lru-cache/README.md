Okay, let's generate the solution structure for LeetCode problem 146, "LRU Cache."

**Step 1: Problem Identification**

*   **Prompt 1:** "Identify the LeetCode problem from the following input: `Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.`"
*   **Output:** `Problem Number: 146, Problem Name: LRU Cache, Difficulty: Medium`

**Step 2: Problem File Creation**

*   Create a directory named `0146-lru-cache`.

**Step 3: Solution File Generation**

*   **Prompt 3.2:** (No solution provided) "Generate solutions in Python for the LeetCode problem: `LRU Cache` (Number: `146`)..."  The standard approach is to use a combination of a Hash Map (Dictionary in Python) and a Doubly Linked List.  We'll also show how to use Python's `OrderedDict` for a more concise solution.

*   **File 1: `0146-lru-cache/solution_doubly_linked_list.py`**

```python
# 146. LRU Cache - Doubly Linked List + Hash Map Approach

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Key: Node
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        """Adds a node right after the head (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        """Removes a node from the linked list."""
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def _move_to_head(self, node):
        """Moves a node to the head (most recently used)."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        """Removes the least recently used node (tail.prev)."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)
```

*   **File 2: `0146-lru-cache/solution_ordered_dict.py`**

```python
# 146. LRU Cache - OrderedDict Approach

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Move accessed key to the end (most recently used)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove from the beginning (least recently used)
```

**Step 4: Problem README Generation**

*   **Prompt 4:** "Generate a `README.md` file..."

*   **File: `0146-lru-cache/README.md`**

```markdown
# 146. LRU Cache, Difficulty: Medium

## Problem Description

Design a data structure that follows the constraints of a **Least Recently Used (LRU)** cache.

Implement the `LRUCache` class:

*   `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
*   `int get(int key)` Return the value of the `key` if the `key` exists, otherwise return `-1`.
*   `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair to the cache. If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions `get` and `put` must each run in **O(1)** average time complexity.

**Example 1:**

**Input**
`["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]`
`[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]`
**Output**
`[null, null, null, 1, null, -1, null, -1, 3, 4]`

**Explanation**
```
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

**Constraints:**

*   `1 <= capacity <= 3000`
*   `0 <= key <= 10^4`
*   `0 <= value <= 10^5`
*   At most `2 * 10^5` calls will be made to `get` and `put`.

## Approach(es)

### Doubly Linked List + Hash Map Approach

**Algorithm:**

1.  **Data Structures:**
    *   **Doubly Linked List:**  Used to maintain the order of keys based on recency of use.  The most recently used key is at the head, and the least recently used key is at the tail.
    *   **Hash Map (Dictionary):** Used to store the key-value pairs and provide O(1) access to nodes in the linked list given a key.  The keys are the cache keys, and the values are pointers to the corresponding nodes in the doubly linked list.
2.  **`get(key)`:**
    *   If the key exists in the hash map:
        *   Retrieve the corresponding node from the linked list.
        *   Move the node to the head of the linked list (mark it as most recently used).
        *   Return the node's value.
    *   If the key doesn't exist, return -1.
3.  **`put(key, value)`:**
    *   If the key exists in the hash map:
        *   Retrieve the corresponding node.
        *   Update the node's value.
        *   Move the node to the head of the linked list.
    *   If the key doesn't exist:
        *   Create a new node.
        *   Add the new node to the head of the linked list.
        *   Add the key-node pair to the hash map.
        *   If the cache is full (size exceeds capacity):
            *   Remove the tail node (least recently used) from the linked list.
            *   Remove the corresponding key from the hash map.

**Data Structures:**

*   Doubly Linked List (`Node` class with `key`, `value`, `prev`, and `next` attributes)
*   Hash Map (Python dictionary)

**Time Complexity:**

*   `get()`: O(1) - Accessing the hash map and moving a node in the linked list are both O(1) operations.
*   `put()`: O(1) -  Adding/updating in the hash map and adding/removing/moving nodes in the linked list are all O(1) operations.

**Space Complexity:**

*   O(capacity) - The space used is proportional to the capacity of the cache.  The hash map and the linked list will store, at most, `capacity` number of elements.

**Trade-offs:**

* This is the most common and efficient solution, as it provides O(1) time complexity for both operations.

### OrderedDict Approach

**Algorithm:**

Python's `collections.OrderedDict` is a dictionary subclass that remembers the order in which its keys were first inserted. This makes it a perfect fit for implementing an LRU cache.

1.  **Data Structures:**
    *  Use an `OrderedDict`

2.  **`get(key)`:**
    *    If the key is not in the `OrderedDict` return -1.
    *    Move the (key, value) pair to the end (mark it as most recently used) `move_to_end()`.
    *   Return Value.

3.  **`put(key, value)`:**
    *   If the key exists:
        * Remove it.
    *   Insert the new key-value pair at the end.
    *   If the cache is full, remove the first item (least recently used) using `popitem(last=False)`.

**Data Structures:**

*   `OrderedDict` (from `collections`)

**Time Complexity:**

*   `get()`: O(1) -  Accessing and moving to the end are O(1) on average.
*   `put()`: O(1) - Inserting, removing, and moving to the end are O(1) on average.

**Space Complexity:**

*   O(capacity)

**Trade-offs:**

*   This is a much more concise and Pythonic solution, leveraging the built-in `OrderedDict`. It achieves the same time and space complexity as the manual doubly linked list approach.

## Code

[Doubly Linked List + Hash Map Approach](./solution_doubly_linked_list.py)
[OrderedDict Approach](./solution_ordered_dict.py)

```

**Step 5: Topics Files**

*   **File: `0146-lru-cache/Hash_Table.md`**

```markdown
# Hash Table

A hash table (hash map) is a data structure that implements an associative array abstract data type, mapping keys to values.  It uses a *hash function* to compute an *index* (hash code) into an array of *buckets*, from which the value can be found.

**Key Concepts:**

*   **Hash Function:** Converts a key to a hash code. Good hash functions should be deterministic, efficient, and distribute keys uniformly.
*   **Collision:** When two different keys produce the same hash code.
*   **Collision Resolution:**
    *   **Separate Chaining:** Each bucket stores a linked list of key-value pairs.
    *   **Open Addressing:** If a collision occurs, probe for an empty slot (linear probing, quadratic probing, double hashing).

**Common Operations (Average Case):**

*   **Insertion:** O(1)
*   **Deletion:** O(1)
*   **Search:** O(1)

**Python Dictionaries:**

Python's `dict` is a highly optimized hash table.

**Related Problems:**

*   [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
* [1. Two Sum](https://leetcode.com/problems/two-sum/)
*   [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
```

*   **File: `0146-lru-cache/Doubly_Linked_List.md`**

```markdown
# Doubly Linked List

A doubly linked list is a linked data structure where each node contains a data field and *two* pointer fields: one pointing to the *next* node in the sequence and another pointing to the *previous* node.

**Key Properties:**

*   **Bidirectional Traversal:**  You can traverse the list in both forward and reverse directions.
*   **Efficient Insertion and Deletion:**  Inserting or deleting a node only requires updating the pointers of the neighboring nodes (unlike singly linked lists, where you might need to traverse from the head to find the previous node).
*   **More Memory Overhead:** Each node requires extra space to store the `prev` pointer.

**Common Operations:**

*   **Insertion (at head, tail, or specific position):** O(1) - If you have a pointer to the insertion point.  If you need to search for the position, it can be O(n).
*   **Deletion (at head, tail, or specific position):** O(1) - If you have a pointer to the node to be deleted.
*   **Search:** O(n) - Requires traversing the list.
* **Access by index** : O(n)

**Python Implementation (Node Class):**

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

**Applications:**
* Used to implement other Data Structures.
* Undo/Redo functionality.
* Browser history.
* LRU Cache

**Related Problems:**

*   [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
*   [460. LFU Cache](https://leetcode.com/problems/lfu-cache/)
* Design Browser History

```

*   **File: `0146-lru-cache/Design.md`**

```markdown
# Design Problems

Design problems in coding interviews assess your ability to create a system or data structure from scratch, meeting specific requirements and constraints. They test your understanding of data structures, algorithms, and object-oriented design principles.

**Key Aspects:**

*   **Requirements Gathering:**  Clearly understand the functional and non-functional requirements (e.g., performance, scalability, memory usage).  Ask clarifying questions!
*   **API Design:** Define the public interface of your system (classes, methods, data structures).
*   **Data Structure Choice:** Select appropriate data structures to meet the requirements efficiently.
*   **Algorithm Design:**  Develop algorithms for the operations of your system.
*   **Trade-offs:**  Discuss the trade-offs between different design choices (e.g., time vs. space complexity, simplicity vs. flexibility).
*   **Object-Oriented Principles (if applicable):**  Consider principles like encapsulation, inheritance, and polymorphism.
*   **Error Handling:** How to deal with unexpected situations and inputs.
* **Testing:** How to unit test your class.

**Common Design Problem Types:**

*   **Data Structure Design:** Implement a specific data structure (e.g., LRU Cache, LFU Cache, Trie, Min Stack).
*   **System Design:** Design a larger system (e.g., a rate limiter, a URL shortener, a parking lot system).

**Example: LRU Cache**

The LRU Cache problem (LeetCode 146) is a classic design problem.  It requires you to:

*   Understand the LRU eviction policy.
*   Design a class with `get` and `put` methods.
*   Achieve O(1) time complexity for both operations.
*   Choose appropriate data structures (Hash Map and Doubly Linked List).

**Related Problems:**

*   [146. LRU Cache](https://leetcode.com/problems/lru-cache/)
*   [460. LFU Cache](https://leetcode.com/problems/lfu-cache/)
* Design Twitter
* Design a parking lot.
```

This completes the generation of the solution structure, including two solution implementations (one using a doubly linked list and hash map, and another using `OrderedDict`), a detailed README explaining both approaches, and relevant topic files. This fully satisfies the problem requirements.
