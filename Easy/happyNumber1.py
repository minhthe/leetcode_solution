'''
https://leetcode.com/problems/happy-number/

approach:  hash + recursion


'''

class Solution(object):
	def isHappy(self, n):
		mp = {}
		def check(n, mp):
			tmp = list(str(n))
			s= sum([ int(i) **2 for i in tmp ] )
			if(s == 1): return True
			if(s in mp): return False
			mp[s] = True
			return check(s, mp)
		if n == 0: return False
		return check(n, mp)