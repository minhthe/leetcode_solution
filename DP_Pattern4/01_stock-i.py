'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
AC in 18 minutes

****Aproach: iteration the for loop

****Complexity:
Time : O(n)
Spae: O(1)
'''
class Solution(object):
	def maxProfit(self, prices):
		n = len(prices)
		if n <= 1 : return 0
		ans = prices[1] - prices[0] if prices[0] < prices[1] else 0
		min_val = min(prices[0], prices[1])
		for i in range(2, n):
			tmp = prices[i] - min_val
			ans = max(ans, tmp)
			min_val = min(min_val, prices[i])
		return ans