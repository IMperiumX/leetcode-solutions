# Hash Table

A hash table (also known as a hash map, dictionary, or associative array) is a data structure that implements a set or map abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions are typically accommodated in some way (e.g., chaining or open addressing).

Hash tables are commonly used to implement associative arrays, database indexing, caches, and sets.

## Key Concepts

- **Hash Function:** A hash function is a function that takes a key as input and returns an integer value, called a hash code or hash value. The hash code is used as an index into the hash table's underlying array.
- **Buckets:** A hash table is typically implemented as an array of buckets (or slots). Each bucket can store one or more key-value pairs.
- **Collision Handling:** When two different keys produce the same hash code, a collision occurs. Hash tables need a mechanism to handle collisions, as multiple key-value pairs may need to be stored in the same bucket.
- **Load Factor:** The load factor of a hash table is the ratio of the number of key-value pairs stored in the table to the number of buckets. It is a measure of how full the hash table is.

## Hash Function

A hash function is any function that can be used to map data of arbitrary size to fixed-size values. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. A good hash function should:

- Be deterministic: The same input should always produce the same hash value.
- Be efficient to compute: The hash function should be fast to calculate.
- Distribute keys evenly: The hash function should distribute keys uniformly across the hash table to minimize collisions.

## Collision Handling Techniques

There are several techniques for handling collisions in hash tables:

1. **Separate Chaining:** In this technique, each bucket contains a linked list (or another data structure) to store multiple key-value pairs that hash to the same index. When a collision occurs, the new key-value pair is added to the linked list of the corresponding bucket.

2. **Open Addressing:** In this technique, all key-value pairs are stored directly in the hash table array. When a collision occurs, the algorithm probes the array in a specific sequence until an empty slot is found. Common probing techniques include:
    - **Linear Probing:** Probes the next consecutive slot.
    - **Quadratic Probing:** Probes slots with increasing quadratic increments.
    - **Double Hashing:** Uses a second hash function to determine the probing sequence.

## Time Complexity

The performance of a hash table depends on the quality of the hash function, the collision handling technique, and the load factor. In the average case, with a good hash function and a reasonable load factor, hash tables offer the following time complexities:

- **Insertion:** O(1)
- **Deletion:** O(1)
- **Lookup (Retrieval):** O(1)

However, in the worst case (e.g., all keys hash to the same bucket), the time complexity can degrade to O(n), where n is the number of key-value pairs.

The worst case occurs when all keys hash to the same bucket, effectively turning the hash table into a linked list.

## Space Complexity

The space complexity of a hash table depends on the number of buckets, the load factor, and the collision handling technique. In general, hash tables have a space complexity of O(n), where n is the number of key-value pairs stored.

## Advantages

- **Fast Lookups, Insertions, and Deletions:** Hash tables provide efficient average-case performance for these operations, making them suitable for applications that require quick access to data.
- **Flexibility:** Hash tables can store a wide range of data types as keys and values.
- **Dynamic Resizing:** Many hash table implementations can dynamically resize themselves to maintain a reasonable load factor as the number of elements changes.

## Disadvantages

- **Worst-Case Performance:** In the worst case, hash table operations can degrade to O(n) time complexity.
- **Space Overhead:** Hash tables may require more space than other data structures, especially when the load factor is low or when using separate chaining.
- **Unordered:** Hash tables do not maintain the order of elements, which may be a limitation for some applications.
- **Hash Function Dependency:** The performance of a hash table heavily depends on the quality of the hash function used.

## Use Cases

- **Database Indexing:** Hash tables are used to create indexes for fast data retrieval in databases.
- **Caching:** They can be used to implement caches to store frequently accessed data.
- **Symbol Tables in Compilers:** Hash tables store identifiers and their associated information during compilation.
- **Spell Checkers:** They can store dictionaries of words for quick spell checking.
- **Associative Arrays in Programming Languages:** Many programming languages implement associative arrays (like dictionaries in Python or maps in Java) using hash tables.

## Problems

- [1. Two Sum](./../problems/0001-two-sum/README.md)
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [15. 3Sum](./0015-3sum/README.md)
- [36. Valid Sudoku](./../problems/0036-valid-sudoku/README.md)
- [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)
  - Demonstrates the use of a hash table (dictionary in Python) to efficiently count the frequency of elements in an array, which is a crucial step in solving the problem.
- [128. Longest Consecutive Sequence](./../problems/0128-longest-consecutive-sequence/README.md)
- [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [347. Top K Frequent Elements](./../problems/0347-top-k-frequent-elements/README.md)
- [1930. Unique Length-3 Palindromic Subsequences](https://leetcode.com/problems/unique-length-3-palindromic-subsequences/)
