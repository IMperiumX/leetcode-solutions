# LeetCode Solutions

This repository contains my solutions to LeetCode problems, along with explanations and analysis of time/space complexity. The goal is to document my learning process, practice problem-solving skills, and build a reference for future study.

## Repository Structure

The repository is organized into the following directories:

- **[`problems/`](problems/):** Solutions categorized by problem number and name. Each problem has its own folder with solution files and a detailed `README.md`.
- **[`topics/`](topics/):** Solutions grouped by data structures and algorithms (e.g., arrays, linked lists, dynamic programming). Each topic has a Markdown file explaining relevant concepts and linking to related problems.
- **[`difficulties/`](difficulties/):** Solutions organized by difficulty level (Easy, Medium, Hard). This can be useful for focused practice.

## Progress Tracker

| Difficulty | Solved | Total | Percentage |
| :--------- | :----- | :---- | :--------- |
| Easy | 8 | 100 | 8.0% |
| Medium | 8 | 150 | 5.3% |
| Hard | 2 | 50 | 4.0% |
| **Total** | **20** | **300** | **6.7%** |

## Problems Solved

### By Number

| Problem Number | Problem Name | Difficulty | Solution |
| :------------- | :----------- | :--------- | :------- |
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | Easy | [py](problems/0001-two-sum/solution.py) |
| 15 | [3Sum](https://leetcode.com/problems/3sum/) | Medium | [py](problems/0015-3sum/solution_hashset.py), [py](problems/0015-3sum/solution_two_pointers.py) |
| 36 | [Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) | Medium | [py](problems/0036-valid-sudoku/solution.py) |
| 53 | [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/) | Hard | [py](problems/0053-maximum-subarray/solution_divide_conquer.py), [py](problems/0053-maximum-subarray/solution.py) |
| 78 | [Subsets](https://leetcode.com/problems/subsets/) | Medium | [py](problems/0078-subsets/solution_backtracking.py), [py](problems/0078-subsets/solution.py), [py](problems/0078-subsets/solution_bitwise.py) |
| 104 | [Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Easy | [py](problems/0104-maximum-depth-of-binary-tree/solution_recursive.py), [py](problems/0104-maximum-depth-of-binary-tree/solution_iterative_dfs.py), [py](problems/0104-maximum-depth-of-binary-tree/solution_iterative_bfs.py) |
| 121 | [Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | [py](problems/0121-best-time-to-buy-and-sell-stock/solution.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Easy | [py](problems/0125-valid-palindrome/solution_reverse_string.py), [py](problems/0125-valid-palindrome/solution_two_pointers.py) |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Medium | [py](problems/0128-longest-consecutive-sequence/solution.py) |
| 141 | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Easy | [py](problems/0141-linked-list-cycle/solution.py) |
| 167 | [Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Medium | [py](problems/0167-two-sum-ii-input-array-is-sorted/solution_binary_search.py), [py](problems/0167-two-sum-ii-input-array-is-sorted/solution_two_pointers.py) |
| 206 | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Easy | [py](problems/0206-reverse-linked-list/solution_iterative.py), [py](problems/0206-reverse-linked-list/solution.py) |
| 226 | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Easy | [py](problems/0226-invert-binary-tree/solution_iterative.py), [py](problems/0226-invert-binary-tree/solution_recursive.py) |
| 238 | [Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | Medium | [py](problems/0238-product-of-array-except-self/solution.py) |
| 271 | [Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) | Medium | [py](problems/0271-encode-and-decode-strings/solution.py) |
| 347 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Medium | [py](problems/0347-top-k-frequent-elements/solution.py) |
| 689 | [Maximum Sum Of 3 Non Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) | Hard | [py](problems/0689-maximum-sum-of-3-non-overlapping-subarrays/solution.py) |
| 983 | [Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/) | Unknown | [py](problems/0983-minimum-cost-for-tickets/solution.py), [py](problems/0983-minimum-cost-for-tickets/solutions_recursion.py) |
| 1422 | [Maximum Score After Splitting A String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) | Easy | [py](problems/1422-maximum-score-after-splitting-a-string/solution_one_pass.py), [py](problems/1422-maximum-score-after-splitting-a-string/solution_prefix_sum.py) |
| 2466 | [Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings/) | Unknown | [py](problems/2466-count-ways-to-build-good-strings/solution.py) |

### By Topic

| Topic | Problems |
| :---- | :------- |
| Union-Find | [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |
| Floyds_Cycle_Finding |  |
| Bucket-Sort | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Array | [1. Two Sum](https://leetcode.com/problems/two-sum/), [15. 3Sum](https://leetcode.com/problems/3sum/), [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/), [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [121. Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/), [238. Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [689. Maximum Sum Of 3 Non Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) |
| Dynamic Programming | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [121. Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [689. Maximum Sum Of 3 Non Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/), [2466. Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings/) |
| Breadth-First-Search | [104. Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| Two-Pointers | [1. Two Sum](https://leetcode.com/problems/two-sum/), [15. 3Sum](https://leetcode.com/problems/3sum/), [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/), [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [167. Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| Tree | [104. Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| Depth-First-Search | [104. Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) |
| Binary-Search | [167. Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) |
| Linked_List |  |
| String | [271. Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/) |
| Bit-Manipulation | [78. Subsets](https://leetcode.com/problems/subsets/) |
| Prefix-Sum | [238. Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) |
| Hash-Table | [1. Two Sum](https://leetcode.com/problems/two-sum/), [15. 3Sum](https://leetcode.com/problems/3sum/), [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/), [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/), [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Matrix | [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/) |
| Backtracking | [78. Subsets](https://leetcode.com/problems/subsets/) |

### By Difficulty

| Difficulty | Problems |
| :--------- | :------- |
| Easy | [1. Two Sum](https://leetcode.com/problems/two-sum/), [104. Maximum Depth Of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/), [121. Best Time To Buy And Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/), [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/), [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/), [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/), [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/), [1422. Maximum Score After Splitting A String](https://leetcode.com/problems/maximum-score-after-splitting-a-string/) |
| Hard | [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/), [689. Maximum Sum Of 3 Non Overlapping Subarrays](https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/) |
| Medium | [15. 3Sum](https://leetcode.com/problems/3sum/), [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/), [78. Subsets](https://leetcode.com/problems/subsets/), [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/), [167. Two Sum Ii Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/), [238. Product Of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/), [271. Encode And Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/), [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) |
| Unknown | [983. Minimum Cost For Tickets](https://leetcode.com/problems/minimum-cost-for-tickets/), [2466. Count Ways To Build Good Strings](https://leetcode.com/problems/count-ways-to-build-good-strings/) |

## How to Use (Optional)

- **Clone the repository:**

    ```bash
    git clone https://github.com/IMperiumX/leetcode-solutions
    ```

- **Navigate to a problem folder:**

    ```bash
    cd problems/0001-two-sum
    ```

- **Run solutions (example for Python):**

    ```bash
    python solution.py
    ```

## Contributing (Optional)

If you'd like to contribute, feel free to open a pull request. Please make sure to follow the existing directory structure and file naming conventions.

---

**Explanation of Sections**

1. **Header:** A brief introduction to the repository and its purpose.
2. **Repository Structure:** Explains the directory organization.
3. **Progress Tracker:**
    - Use a table or a visual chart to show your overall progress.
    - Update this section regularly.
4. **Problems Solved:**
    - **By Number:** A table listing problems in numerical order, with links to solutions in different languages.
    - **By Topic:** Groups problems by topic, providing links to topic files and problem folders.
    - **By Difficulty:** Similar to "By Topic," but grouped by difficulty level.
5. **How to Use (Optional):** Instructions for using the repository, running code, etc.
6. **Contributing (Optional):** Guidelines for contributors.

**Key Tips**

- **Keep it Updated:** Regularly update the `README.md` as you solve more problems.
- **Be Concise:** Keep descriptions clear and to the point.
- **Use Links Effectively:** Make it easy to navigate between different sections using Markdown links.
- **Automate (Optional):** Consider using scripting or tools to automate the updating of the `README.md` (e.g., generating the "Problems Solved" table automatically).

By following this comprehensive structure, your main `README.md` will be an excellent starting point for anyone visiting your LeetCode solutions repository, including your future self!
