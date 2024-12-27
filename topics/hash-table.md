# Hash Table

A hash table (also known as a hash map, dictionary, or associative array) is a data structure that implements a set or map abstract data type, a structure that can map keys to values. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.

Ideally, the hash function will assign each key to a unique bucket, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. Such collisions are typically accommodated in some way (e.g., chaining or open addressing).

Hash tables are commonly used to implement associative arrays, database indexing, caches, and sets.
