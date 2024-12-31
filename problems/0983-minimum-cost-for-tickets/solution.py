# 983. Minimum Cost For Tickets - Dynamic Programming Approach

def mincostTickets(days, costs):
    """
    Calculates the minimum cost to travel on the given days with different ticket options.

    Args:
      days: A list of days (integers) when you need to travel.
      costs: A list of costs for 1-day, 7-day, and 30-day passes.

    Returns:
      The minimum cost to travel on all specified days.
    """
    dp = [0] * 366  # dp[i] stores the minimum cost to travel up to day i

    travel_days = set(days)

    for i in range(1, 366):
        if i not in travel_days:
            dp[i] = dp[i - 1]  # No travel needed, cost is the same as the previous day
        else:
            dp[i] = min(
                dp[i - 1] + costs[0],  # 1-day pass
                dp[max(0, i - 7)] + costs[1],  # 7-day pass
                dp[max(0, i - 30)] + costs[2],  # 30-day pass
            )

    return dp[365]
