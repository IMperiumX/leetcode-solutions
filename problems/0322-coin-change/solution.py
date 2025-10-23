"""
322. Coin Change - Dynamic Programming (Bottom-Up)
"""


def coinChange(coins: list[int], amount: int) -> int:
    """
    Calculates the fewest number of coins needed to make up a given amount.

    Args:
      coins: A list of coin denominations.
      amount: The target amount.

    Returns:
      The minimum number of coins, or -1 if the amount cannot be made up.
    """
    dp = [float("inf")] * (amount + 1)  # Initialize dp array with infinity
    dp[0] = 0  # Base case: 0 coins are needed to make up amount 0

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1
