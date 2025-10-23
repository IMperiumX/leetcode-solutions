
# 322. Coin Change, Difficulty: Medium

## Problem Description

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the *fewest number of coins* that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.

You may assume that you have an *infinite* number of each kind of coin.

**Example 1:**

```

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

```

**Example 2:**

```

Input: coins = [2], amount = 3
Output: -1

```

**Example 3:**

```

Input: coins = [1], amount = 0
Output: 0

```

**Constraints:**

- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`
- `0 <= amount <= 10^4`

## Approach(es)

### Dynamic Programming (Bottom-Up/Tabulation)

**Algorithm:**

1. **Initialization:**
    - Create a `dp` array of size `amount + 1`.  `dp[i]` will store the minimum number of coins needed to make up amount `i`.
    - Initialize all elements of `dp` to infinity (or a large value like `amount + 1`). This signifies that we haven't found a way to make up those amounts yet.
    - Set `dp[0] = 0`.  We need 0 coins to make up an amount of 0.
2. **Iteration:**
    - Iterate through the `dp` array from `i = 1` to `amount`:
        - For each amount `i`, iterate through the available `coins`:
            - If `i - coin >= 0` (meaning we can use the current `coin` without going negative):
                - Update `dp[i]` with the minimum of its current value and `dp[i - coin] + 1`.  This means we're considering using the current `coin` and adding 1 to the minimum number of coins needed to make up the remaining amount (`i - coin`).
3. **Result:**
    - After the iterations, `dp[amount]` will contain the minimum number of coins needed to make up the target `amount`.
    - If `dp[amount]` is still infinity, it means we couldn't make up the amount, so return -1.  Otherwise, return `dp[amount]`.

**Data Structures:**

- `dp` array (list in Python)

**Time Complexity:**

- O(amount \* len(coins)).  We have nested loops iterating through amounts and coins.

**Space Complexity:**

- O(amount) to store the `dp` array.

**Trade-offs:**

- Efficient and the standard approach for this problem.
- Uses dynamic programming to avoid redundant calculations.

## Code

[Dynamic Programming (Bottom-Up)](./solution.py)

## Notes

- This is a classic dynamic programming problem, often used to illustrate the concept of bottom-up (tabulation) DP.
- The key idea is to build up solutions for smaller amounts and use them to find solutions for larger amounts.
- The initialization of `dp[0] = 0` is a crucial base case.
- The use of infinity (or a large value) as the initial value in `dp` allows us to easily track whether a particular amount can be made up or not.
- A top-down (memoized) recursive solution is also possible, but the bottom-up approach is generally preferred for its iterative nature and avoidance of recursion overhead.
