'''
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number

###overide method bisect -> AC but need to check again the condion l==r
class Solution(object):
	def smallerNumbersThanCurrent(self, nums):
		arr = []
		nums_sorted = sorted(nums)
		def bisect_left(a, p, l ,r ):
			while(l <=r):
				mid = ( int(r - l)/2 + l )
				if(a[mid] == p and (a[mid-1] < p or  l==r  )): return mid 
				if(a[mid] >= p): r = mid - 1
				else: l = mid + 1 
				
			return l
				
		for i in range(len(nums)):
			arr.append(  bisect_left( nums_sorted, nums[i] , 0 , len(nums) )  )
		return arr
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