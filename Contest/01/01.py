'''
https://leetcode.com/problems/first-unique-character-in-a-string/
'''
class Solution(object):
	def firstUniqChar(self, s):
		n = len(s)
		if n == 1: return 0 
		if n == 0: return -1 
		mp = {}
		for i in range(n):
			if( s[i] in mp ):
				cnt, pos_latest = mp[ s[i] ][0] + 1 , i
				mp[s[i]] = ( cnt,   pos_latest )
			else:
				cnt, pos_latest = 1, i
				mp[s[i]] = ( cnt,   pos_latest )
		for i in range(n):
			if( mp[s[i]][0] == 1 and mp[s[i]][1]  == i  ):
				return i 
		return -1