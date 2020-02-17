'''
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix
'''

import bisect
class Solution(object):
	def countNegatives(self, grid):
		m = len(grid)
		if m==0: return 0
		n = len(grid[0])
		if n== 0: return 0
		cnt = 0 
		for arr in grid:
			arr.reverse()
			pos = bisect.bisect_left(arr, 0, 0, n)
			cnt += pos
		return cnt