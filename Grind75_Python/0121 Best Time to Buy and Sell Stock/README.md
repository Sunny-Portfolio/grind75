# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->
Compare and find the minimum price as loop goes on
Find the differences between minimum price and the current price
# Complexity
- Time complexity:
<!-- Add your time complexity here, e.g. $$O(n)$$ -->
O(n)

- Space complexity:
<!-- Add your space complexity here, e.g. $$O(n)$$ -->
O(1)

# Code
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price

            if price - minPrice > profit:
                profit = price - minPrice

        return profit
```

Cleaner solution but slightly slower:
```python
  def maxProfit2(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)

        return profit
```