
# 1769. Minimum Number of Operations to Move All Balls to Each Box, Difficulty: Medium

## Problem Description

You have `n` boxes. You are given a binary string `boxes` of length `n`, where `boxes[i]` is '0' if the `i`th box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box `i` is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be more than one ball in some boxes.

Return an array `answer` of size `n`, where `answer[i]` is the minimum number of operations needed to move all the balls to the `i`th box.

Each `answer[i]` is calculated considering the initial state of the boxes.

**Example 1:**

```
Input: boxes = "110"
Output: [1,1,3]
Explanation: The answer for each box is as follows:
1) First box: you will have to move one ball from the second box to the first box in one operation.
2) Second box: you will have to move one ball from the first box to the second box in one operation.
3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
```

**Example 2:**

```
Input: boxes = "001011"
Output: [11,8,5,4,3,4]
```

**Constraints:**

- `n == boxes.length`
- `1 <= n <= 2000`
- `boxes[i]` is either '0' or '1'.

## Approach(es)

### Brute Force Approach

**Algorithm:**

1. Iterate through each box `i` (from 0 to `n-1`).
2. For each box `i`, iterate through all other boxes `j` (from 0 to `n-1`).
3. If box `j` contains a ball (`boxes[j] == '1'`), calculate the distance between `i` and `j` (`abs(i - j)`) and add it to the total operations count for box `i`.
4. Store the total operations count for box `i` in the `answer` array.

**Data Structures:**

- A list `answer` to store the minimum operations for each box.

**Time Complexity:**

- O(n^2), where n is the number of boxes. We have nested loops iterating through all pairs of boxes.

**Space Complexity:**

- O(n) to store the `answer` array.

**Trade-offs:**

- This approach is simple to understand and implement.
- It is not very efficient for larger inputs due to the quadratic time complexity.

### Optimized Approach

**Algorithm:**

1. Initialize an `answer` array of size `n` with all elements set to 0.
2. Calculate the initial operations needed to move all balls to the first box (index 0) using a single pass from left to right.
3. Iterate from the second box to the last box (index 1 to `n-1`).
    - Maintain a `left_count` (number of balls to the left) and `left_cost` (cost to move balls from the left).
    - Update `left_count` and `left_cost` in each iteration.
    - The operations for the current box are calculated based on the `left_cost`.
4. Similarly, iterate from the second last box to the first box (index `n-2` to 0).
    - Maintain a `right_count` (number of balls to the right) and `right_cost` (cost to move balls from the right).
    - Update `right_count` and `right_cost`.
    - Add the `right_cost` to the operations for the current box (which was calculated in the previous step).

**Data Structures:**

- A list `answer` to store the minimum operations for each box.

**Time Complexity:**

- O(n), where n is the number of boxes. We have two separate linear passes.

**Space Complexity:**

- O(n) to store the `answer` array.

**Trade-offs:**

- This approach is more complex to implement compared to the brute force approach.
- It is significantly more efficient for larger inputs due to the linear time complexity.

## Code

- [Brute Force Approach](./solution_bruteforce.py)
- [Optimized Approach](./solution_optimized.py)

## Notes

The optimized approach utilizes the concept of prefix sums (or in this case, prefix costs) to efficiently calculate the minimum operations. By leveraging the calculations from the previous box, we avoid redundant computations, leading to a linear time solution.
