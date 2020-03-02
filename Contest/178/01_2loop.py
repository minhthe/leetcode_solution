'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number
'''
class Solution(object):
	def smallerNumbersThanCurrent(self, nums):
		n = len(nums)
		rst = [0] * (n)
		for i in range(n):
			for j in range(n):
				if(nums[i] > nums[j]): rst[i] += 1
		return rst