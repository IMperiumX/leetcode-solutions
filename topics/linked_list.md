# Linked List

A linked list is a linear data structure where elements are not stored at contiguous memory locations. Instead, each element (called a **node**) points to the next element in the sequence. This structure allows for efficient insertion and deletion of elements compared to arrays, but it makes accessing elements by index slower.

## Components of a Linked List

A linked list consists of the following components:

* **Node:** Each node in a linked list contains two parts:
  * **Data:** The value or data stored in the node.
  * **Next:** A pointer or reference to the next node in the list. The last node in the list has a `next` pointer that points to `None` (or `NULL` in some languages), indicating the end of the list.
* **Head:** A pointer to the first node in the linked list. It serves as the entry point to the list.
* **Tail:** (Optional) A pointer to the last node in the linked list. It can make appending elements more efficient.

## Types of Linked Lists

There are several types of linked lists, including:

* **Singly Linked List:** Each node has a pointer only to the next node.
* **Doubly Linked List:** Each node has pointers to both the next and the previous nodes. This allows for traversal in both directions but requires more memory per node.
* **Circular Linked List:** The last node's `next` pointer points back to the first node (the head), forming a loop.
* **Circular Doubly Linked List:** A combination of doubly and circular linked lists, where the last node's `next` points to the first node, and the first node's `prev` points to the last node.

## Basic Operations and Time Complexity

| Operation        | Singly Linked List | Doubly Linked List |
| ---------------- | :----------------: | :----------------: |
| Access (by index) |        O(n)        |        O(n)        |
| Insertion (head) |        O(1)        |        O(1)        |
| Insertion (tail) |   O(n) or O(1)\*   |        O(1)        |
| Insertion (middle) |  O(n) (search) + O(1)  |  O(n) (search) + O(1)  |
| Deletion (head)  |        O(1)        |        O(1)        |
| Deletion (tail)  |        O(n)        |   O(n) or O(1)\*   |
| Deletion (middle) |  O(n) (search) + O(1)  |  O(n) (search) + O(1)  |
| Search           |        O(n)        |        O(n)        |

\* O(1) if you have a pointer to the tail node.

## Applications

* Implementing stacks and queues.
* Dynamic memory allocation.
* Representing polynomial equations.
* Implementing hash tables (chaining).
* Situations where frequent insertions and deletions are needed, especially at the beginning or end (with a tail pointer).

## Advantages of Linked Lists

* **Dynamic Size:** Linked lists can grow or shrink dynamically as needed.
* **Efficient Insertions and Deletions:** Inserting or deleting elements at the beginning or middle of a linked list is generally faster than with arrays, as it only requires updating a few pointers.
* **No Memory Waste:** Linked lists only use as much memory as they need to store the elements, unlike arrays, which may have pre-allocated memory that is not fully utilized.

## Disadvantages of Linked Lists

* **Slow Access:** Accessing an element at a specific index is slow (O(n)) because you have to traverse the list from the head.
* **Memory Overhead:** Each node in a linked list requires extra memory to store the pointer(s) to the next (and previous, in doubly linked lists) node(s).
* **Not Cache-Friendly:** Linked list nodes may not be stored contiguously in memory, which can lead to poor cache performance compared to arrays.

## When to Use Linked Lists

* When you need frequent insertions and deletions, especially at the beginning or middle of the list.
* When you don't know the number of elements in advance and need a dynamic data structure.
* When you don't need random access to elements.
* When memory usage is a concern, and you want to avoid pre-allocating a large block of memory.

## Example Implementation (Singly Linked List in Python)

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" -> ")
            curr_node = curr_node.next
        print("None")

# Example Usage
my_list = LinkedList()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.print_list()  # Output: 1 -> 2 -> 3 -> None
```

## Related LeetCode Problems

* [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
* [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
* [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
* [23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
* [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
* [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
* [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)

# Linked List

A linked list is a linear data structure where each element (called a node) contains a value and a pointer (or reference) to the next node in the sequence. Unlike arrays, linked lists do not store elements in contiguous memory locations.

## Types of Linked Lists

* **Singly Linked List:** Each node has a pointer to the next node only.
* **Doubly Linked List:** Each node has pointers to both the next and previous nodes.
* **Circular Linked List:** The last node's pointer points back to the first node, forming a cycle.

## Advantages of Linked Lists

* **Dynamic Size:** Linked lists can grow or shrink dynamically as needed, unlike arrays which have a fixed size (or require resizing).
* **Efficient Insertion and Deletion:** Inserting or deleting a node in a linked list only requires updating pointers, which can be done in O(1) time if you have a pointer to the node before the insertion/deletion point. In contrast, inserting or deleting in the middle of an array can require shifting elements, which takes O(n) time.
* **No wasted space:** Because a linked list only takes memory space that it is using.

## Disadvantages of Linked Lists

* **No Random Access:** Accessing an element at a specific index in a linked list requires traversing the list from the beginning, which takes O(n) time. Arrays allow O(1) random access.
* **Extra Memory Overhead:** Each node in a linked list requires extra memory to store the pointer(s).
* **Cache Inefficiency:** Due to non-contiguous memory allocation, linked lists can have poor cache performance compared to arrays.

## Common Linked List Operations

* **Traversal:** Visiting each node in the list.
* **Insertion:** Adding a new node at the beginning, end, or a specific position.
* **Deletion:** Removing a node from the beginning, end, or a specific position.
* **Searching:** Finding a node with a specific value.
* **Reversal:** Reversing the order of the nodes in the list.

## LeetCode Problems Related to Linked Lists

* [21. Merge Two Sorted Lists](0021-merge-two-sorted-lists/README.md)
* [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
* [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
* [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
* [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)
* [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)
* [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
