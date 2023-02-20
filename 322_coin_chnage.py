class Solution:
    def coinChange(self, coins, amount) -> int:
        # Create a list of length `amount+1` to store the minimum number of coins needed to make each amount
    # Initialize all values to a very large number, except for the first value (0), which is 0
        dp = [0] + [float('inf')] * amount
        
        # Iterate through all amounts from 1 to `amount`, and calculate the minimum number of coins needed for each amount
        for i in range(1, amount+1):
            # Iterate through all coins
            for coin in coins:
                # If the current coin is less than or equal to the current amount, and using this coin results in a smaller number of coins than the current minimum, update the minimum
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        # If dp[amount] is still infinity, it means we could not make the amount using the given coins
        # Return -1 in this case, otherwise return dp[amount]
        return dp[amount] if dp[amount] != float('inf') else -1

coins = [1,2,5]
amount = 11
obj = Solution()
print(obj.coinChange(coins,amount))