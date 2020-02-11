'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
'''
class Solution(object):
	def maxProfit(self, prices):
		a = prices
		rst = 0
		if len(a) <= 1: return 0
		max_cur = a[-1]
		for i in range(len(a)-1, -1,-1):
			if( a[i] > max_cur  ):
				max_cur = a[i]
			rst = max(rst,  max_cur - a[i] )
		return rst