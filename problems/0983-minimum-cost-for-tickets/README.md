
# Problem Description

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array `days`. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

* a 1-day pass is sold for `costs[0]` dollars,
* a 7-day pass is sold for `costs[1]` dollars, and
* a 30-day pass is sold for `costs[2]` dollars.

The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of `days`.

**Example 1:**

**Input:** days = [1,4,6,7,8,20], costs = [2,7,15]
**Output:** 11
**Explanation:** For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

**Example 2:**

**Input:** days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
**Output:** 17
**Explanation:** For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.

**Constraints:**

* 1 <= days.length <= 365
* 1 <= days[i] <= 365
* days is in strictly increasing order.
* costs.length == 3
* 1 <= costs[i] <= 1000

## Approach(es)

Tips:-

Notice that the constraints are very small, thus we can figure out all possibilities and take the minimum of them , i.e. it's a dp problem.

For any day 'i', we can buy either of the 3 ticket and we are paid until ith, i+6th or i+29thday . Also keep in mind that the days are sorted so we can easily find the next unpaid day for each possibility. At each step we need to take minimum of these 3 possibilities

### Dynamic Programming Approach

* Algorithm:
  * We use an array `dp` of size 366, where `dp[i]` represents the minimum cost to travel up to day `i`.
  * We iterate through the days from 1 to 365.
  * If the current day `i` is not a travel day, the cost is the same as the previous day: `dp[i] = dp[i - 1]`.
  * If the current day `i` is a travel day, we consider three options:
        1. Buy a 1-day pass: `dp[i - 1] + costs[0]`
        2. Buy a 7-day pass: `dp[max(0, i - 7)] + costs[1]`
        3. Buy a 30-day pass: `dp[max(0, i - 30)] + costs[2]`
  * We take the minimum of these three options and store it in `dp[i]`.
  * Finally, `dp[365]` will contain the minimum cost to travel all days.
* Data Structures:
  * `dp`: An array to store the minimum cost up to each day.
  * `travel_days`: A set to efficiently check if a day is a travel day.
* Time Complexity:
  * O(N), where N is the maximum number of days (365 in this case). We iterate through each day once.
* Space Complexity:
  * O(N), due to the `dp` array.
* Trade-offs:
  * Using dynamic programming provides an optimal solution with a reasonable time complexity. The trade-off is the space complexity, which is linear with respect to the number of days.

### Recursion with Memoization

* Algorithm:
  * We use a recursive function `solve(i)` that calculates the minimum cost to travel from day index `i` onwards in the `days` array.
  * The base case is when `i` is greater than or equal to the number of travel days, in which case the cost is 0.
  * For each day index `i`, we iterate through the three types of passes (1-day, 7-day, and 30-day).
  * For each pass type `k`, we find the next day index `j` such that `days[j]` is the first day not covered by the current pass.
  * We recursively call `solve(j)` to get the minimum cost for the remaining days and add the cost of the current pass to it.
  * We take the minimum cost among all three pass types and memoize it to avoid redundant calculations.
* Data Structures:
  * `memo`: A dictionary to store the results of the recursive calls (memoization).
  * `days`: The input list of travel days.
  * `costs`: The input list of pass costs.
  * `durations`: A list representing the durations of the passes (1, 7, and 30 days).
* Time Complexity:
  * O(N), where N is the number of travel days. Due to memoization, each subproblem `solve(i)` is computed only once.
* Space Complexity:
  * O(N), due to the memoization dictionary and the recursion depth.
* Trade-offs:
  * Recursion with memoization provides a more intuitive top-down approach compared to dynamic programming. It can be easier to understand and implement for some.
  * The trade-off is that recursion might have a slightly higher overhead compared to the iterative nature of dynamic programming. However, memoization mitigates this by avoiding redundant computations.

## Code

[dynamic_programming.py](./solution.py)
[recursive_memoization.py](./solutions_recursion.py)
