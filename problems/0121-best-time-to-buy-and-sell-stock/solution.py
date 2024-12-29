# 121. Best Time to Buy and Sell Stock - One Pass Approach


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Finds the maximum profit that can be achieved by buying and selling a stock once.

        Args:
          prices: A list of integers representing the prices of a stock on different days.

        Returns:
          The maximum profit that can be achieved.
        """
        min_price = float("inf")  # Initialize the minimum price to a very large value
        max_profit = 0  # Initialize the maximum profit to 0
        print(f"prices: {prices}")
        print("-" * 20)

        for idx, price in enumerate(prices):
            print(f"day {idx}, price: {price}")
            # Update the minimum price if a lower price is found
            min_price = min(min_price, price)
            print(f"min_price: {min_price}")
            # Calculate the profit if selling at the current price
            profit = price - min_price
            print(f"profit: {profit}")
            # Update the maximum profit if a higher profit is found
            max_profit = max(max_profit, profit)
            print(f"max_profit: {max_profit}")
            print("-" * 20)
        return max_profit

    def maxProfit2(self, prices):
        """
        Kadane's Algorithm

        find a contiguous subarray giving maximum profit. If the difference
        falls below 0, reset it to zero.

        """
        cur = final = 0
        for i in range(1, len(prices)):
            # Calculate the profit if selling at the current price
            # track the maximum sum ending at each position.
            # I spent some time convincing myself about why we need to reset to zero.
            # By reseting maxCur to 0, essentially it means that we have found a
            # point i where the price[i] is lower than the time we bought, and that
            # we should then try to buy at point i to see if we can achieve a bigger gain.
            # Because maxCur is recording the difference, the difference between
            # price[i] and itself should be 0.
            cur = max(0, cur + prices[i] - prices[i - 1])
            # Update the maximum profit if a higher profit is found
            # will track the overall maximum sum.
            final = max(cur, final)

        return final


sol = Solution()
max_profit = sol.maxProfit([7, 3, 1, 6])
print(max_profit)
