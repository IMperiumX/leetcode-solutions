# Sets

A set is an unordered collection of unique elements. It is a fundamental data structure used to store and manipulate a group of distinct objects. Sets are particularly useful when you need to check for the presence of an element or eliminate duplicates from a collection.

## Key Concepts

- **Uniqueness:** Sets only store unique elements. Duplicate elements are automatically discarded.
- **Unordered:** Elements in a set do not have a specific order.
- **Membership Testing:** Sets provide efficient operations for checking whether an element is present in the set.
- **Set Operations:** Sets support various mathematical set operations like union, intersection, difference, and symmetric difference.

## Operations

- **add(element):** Adds an element to the set.
- **remove(element):** Removes an element from the set. Raises a KeyError if the element is not found.
- **discard(element):** Removes an element from the set if it is present. Does not raise an error if the element is not found.
- **contains(element) or element in set:** Checks if an element is present in the set. Returns `True` if the element is found, `False` otherwise.
- **union(other_set) or set1 | set2:** Returns a new set containing all elements from both sets.
- **intersection(other_set) or set1 & set2:** Returns a new set containing only the elements that are present in both sets.
- **difference(other_set) or set1 - set2:** Returns a new set containing elements that are present in the first set but not in the second set.
- **symmetric_difference(other_set) or set1 ^ set2:** Returns a new set containing elements that are present in either the first or the second set, but not in both.
- **issubset(other_set) or set1 <= set2:** Checks if the first set is a subset of the second set.
- **issuperset(other_set) or set1 >= set2:** Checks if the first set is a superset of the second set.
- **len(set):** Returns the number of elements in the set.
- **clear():** Removes all elements from the set.

## Time Complexity (for common operations)

- **add(element):** Average case: O(1), Worst case: O(n)
- **remove(element):** Average case: O(1), Worst case: O(n)
- **contains(element):** Average case: O(1), Worst case: O(n)
- **union(other_set):** O(len(set1) + len(set2))
- **intersection(other_set):** O(min(len(set1), len(set2)))
- **difference(other_set):** O(len(set1))
- **symmetric_difference(other_set):** O(len(set1) + len(set2))

## Space Complexity

- O(n), where n is the number of elements in the set.

## Applications

- **Removing duplicates from a list or array.**
- **Checking for the presence of an element in a collection.**
- **Finding common elements between two collections (intersection).**
- **Finding unique elements in a collection (union, difference).**
- **Implementing algorithms that require tracking unique elements.**

## Related LeetCode Problems

- [349. Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)
- [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)
- [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)
- [2657. Find the Prefix Common Array of Two Arrays](https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/)
- [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)
