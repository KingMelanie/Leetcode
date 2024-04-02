class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for p in prices:
            if p < min_price:
                min_price = p
            elif max_profit < p - min_price:
                max_profit = p - min_price
        return max_profit
    

# Step 1: Test maxProfit() with 
# prices = [7, 1, 5, 3, 6, 4]
prices = [7, 1, 5, 3, 6, 4]
ob1 = Solution()
print("The First case result is: ", ob1.maxProfit(prices))

# Step 2: Test maxProfit() with 
# prices = [7,6,4,3,1]
prices = [7,6,4,3,1]
ob1 = Solution()
print("The second case result is: ", ob1.maxProfit(prices))