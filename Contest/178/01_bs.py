'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
'''

import bisect		
class Solution(object):
	def smallerNumbersThanCurrent(self, nums):
		n = len(nums)
		rst = [0]  * (n)
		tmp = sorted(nums)
		for i in range(n):
			rst[i] = bisect.bisect_left(tmp, nums[i], 0, n)
		return rst