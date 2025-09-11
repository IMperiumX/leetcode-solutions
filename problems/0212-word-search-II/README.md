```python
# 212. Word Search II - Trie + DFS

class TrieNode:
    def __init__(self):
        self.children = {}  # Map character to TrieNode
        self.is_word = False  # True if this node represents the end of a word
        self.word = None # keep track of the word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Finds all words from a list that can be formed on the board.
    """
    rows, cols = len(board), len(board[0])
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()  # Use a set to avoid duplicate results
    visited = set()

    def dfs(row, col, node):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or (row, col) in visited
            or board[row][col] not in node.children
        ):
            return

        visited.add((row, col))
        node = node.children[board[row][col]]

        if node.is_word:
            result.add(node.word)  # Add the word to the result set


        # Explore adjacent cells
        dfs(row + 1, col, node)
        dfs(row - 1, col, node)
        dfs(row, col + 1, node)
        dfs(row, col - 1, node)

        visited.remove((row, col))  # Backtrack: Remove from visited set

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root)

    return list(result)  # Convert set to list for the output

```

```markdown
# 212. Word Search II, Difficulty: Hard

## Problem Description

Given an `m x n` `board` of characters and a list of strings `words`, return *all words on the board*.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of `words` are unique.

## Approach(es)

### Trie + DFS

Algorithm:

1.  **Build a Trie:** Create a Trie data structure and insert all the words from the `words` list into the Trie.
2.  **DFS Search:**
    *   Iterate through each cell `(r, c)` of the `board`.
    *   For each cell, start a Depth-First Search (DFS) to explore possible words.
    *   The DFS function takes the current row `row`, column `col`, and the current Trie node `node` as input.
    *   **Base Cases (stopping conditions for DFS):**
        *   If the current row or column is out of bounds.
        *   If the current cell has already been visited (in the current word search).
        *   If the current character on the board (`board[row][col]`) is not a child of the current Trie node (meaning no word in the Trie can be formed starting from this path).
    * **Recursive step**:
        * Add current cell `(row, col)` to visited.
        *   If current Trie `node` correspond to a valid word:
            * Add it to result set.
        *   Recursively call dfs for all directions.
        * Backtrack (remove the last cell from visited).
3.  **Return Result:** Return the list of found words.

Data Structures:

*   Trie
*   Set (to store visited cells during DFS and to store unique words)

Time Complexity:

*   **Trie Construction:** O(W * L), where W is the number of words and L is the average length of a word.
*   **DFS:** O(M * N * 4^L), where M is the number of rows, N is the number of columns in the board, and L is the maximum length of a word.  In the worst case, for each cell, we explore 4 directions, and we might do this for up to L levels (the length of the longest word).  However, the Trie pruning significantly reduces the search space in practice.
* Overall: is dominated by the DFS, so the total time complexity would be O(M * N * 4^L) (but the Trie significantly reduces this in most practical scenarios).

Space Complexity:

*   **Trie:** O(W * L), where W is the number of words and L is the average length of a word.
*   **DFS Recursion Stack:** O(L) in the worst case (the depth of recursion is limited by the length of the longest word).
*  **Visited Set:** O(M*N)
* Overall space complexity is: O(WL + L + MN) = O(WL + MN)

Trade-offs:
* This approach requires good understanding for both Trie and DFS.
* The main advantage is the efficiency of the search due to pruning by Trie.

## Code

```python
# 212. Word Search II - Trie + DFS

class TrieNode:
    def __init__(self):
        self.children = {}  # Map character to TrieNode
        self.is_word = False  # True if this node represents the end of a word
        self.word = None # keep track of the word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word


def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    """
    Finds all words from a list that can be formed on the board.
    """
    rows, cols = len(board), len(board[0])
    trie = Trie()
    for word in words:
        trie.insert(word)

    result = set()  # Use a set to avoid duplicate results
    visited = set()

    def dfs(row, col, node):
        if (
            row < 0
            or row >= rows
            or col < 0
            or col >= cols
            or (row, col) in visited
            or board[row][col] not in node.children
        ):
            return

        visited.add((row, col))
        node = node.children[board[row][col]]

        if node.is_word:
            result.add(node.word)  # Add the word to the result set


        # Explore adjacent cells
        dfs(row + 1, col, node)
        dfs(row - 1, col, node)
        dfs(row, col + 1, node)
        dfs(row, col - 1, node)

        visited.remove((row, col))  # Backtrack: Remove from visited set

    for r in range(rows):
        for c in range(cols):
            dfs(r, c, trie.root)

    return list(result)  # Convert set to list for the output
```

## Notes

* This problem combines the concepts of Trie (for efficient prefix checking) and Depth-First Search (for exploring the board).
* Using a Trie significantly optimizes the search by pruning branches that don't lead to valid words.  Without a Trie, we'd have to check every possible path on the board, which would be much less efficient.
* The `visited` set is crucial to prevent cycles and avoid using the same cell multiple times within a single word search.
* Using a `set` to store the results also handles duplicates and ensures the correct output format.

```

**Step 5: Topic Extraction and Files**

*Prompt:* Topic extraction.
*Analysis:* Relevant topics are "Array", "String", "Depth-First Search (DFS)", "Trie", and "Backtracking" (implicitly, since DFS with `visited` involves backtracking).

* `Arrays.md`: (already exists, reuse)
* `String.md`: (already exists, reuse)
* `Depth-First Search (DFS).md`: (already exists, reuse)
* Create `Trie.md`.

```markdown
# Trie (Prefix Tree)

A Trie, also known as a prefix tree, is a tree-like data structure used to store a dynamic set of strings, where the keys are usually strings.  Unlike a binary search tree, no node in the trie stores the key associated with that node; instead, its position in the tree defines the key with which it is associated.  All the descendants of a node have a common prefix of the string associated with that node, and the root is associated with the empty string.

## Key Features

*   **Nodes:** Each node in a Trie typically contains:
    *   A dictionary (or array) to store links to its children, where each child represents a possible next character in a string.
    *   A flag (e.g., `is_word`) to indicate whether the path from the root to this node represents a complete word.
*   **Root:** The root node represents the empty string.
*   **Edges:** Edges represent characters.
*   **Paths:** Paths from the root to other nodes represent prefixes of strings.

## Common Operations

*   **Insert(word):**  Adds a word to the Trie.
*   **Search(word):**  Checks if a word exists in the Trie.
*   **StartsWith(prefix):**  Checks if there is any word in the Trie that starts with the given prefix.
*   **Delete(word):** Removes a word from the Trie.

## Advantages of Tries

*   **Efficient Prefix Search:** Tries excel at finding all words with a given prefix, which is useful for autocompletion, spell checking, and other applications.
*   **Fast Lookup:** Searching for a word in a Trie takes O(L) time, where L is the length of the word. This is independent of the number of words stored in the Trie.
*   **Space Efficiency (for common prefixes):**  Tries can be space-efficient when storing many words with common prefixes, as the prefixes are shared among multiple words.

## Disadvantages of Tries

*   **Space Inefficiency (for few common prefixes):**  If the words have few common prefixes, the Trie can consume a lot of memory, as each node needs to store pointers to potential children (even if many of those children are null).
*   **Not as widely used as Hash Tables or Balanced Trees:** Tries are specialized for string-related operations and are not as general-purpose as other data structures.

## Python Implementation (Basic)

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # Map character to TrieNode
        self.is_word = False  # True if this node represents the end of a word


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

    def startsWith(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

```

## LeetCode problems related to Trie

*   [212. Word Search II](0212-word-search-ii/README.md)
*   [208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
*   [211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)
* [421. Maximum XOR of Two Numbers in an Array](https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/)

```
This completes the repository, including a Trie + DFS solution, a detailed README, and all necessary topic files (including a new "Trie.md").  The explanations are clear, the code is well-commented, and the solution correctly addresses the problem's requirements. The time and space complexities are analyzed, and relevant trade-offs are discussed.
