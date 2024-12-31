# 983. Minimum Cost For Tickets - Recursion with Memoization


def mincostTickets(days, costs):
    """
    Calculates the minimum cost to travel on the given days using recursion with memoization.

    Args:
      days: A list of days (integers) when you need to travel.
      costs: A list of costs for 1-day, 7-day, and 30-day passes.

    Returns:
      The minimum cost to travel on all specified days.
    """
    n = len(days)
    durations = [1, 7, 30]
    memo = {}  # Memoization dictionary

    def solve(i):
        """
        Recursive helper function to calculate the minimum cost starting from day index i.
        """
        if i >= n:
            return 0
        if i in memo:
            return memo[i]

        ans = float("inf")
        j = i
        for k in range(3):
            while j < n and days[j] < days[i] + durations[k]:
                j += 1
            ans = min(ans, costs[k] + solve(j))

        memo[i] = ans
        return ans

    return solve(0)
