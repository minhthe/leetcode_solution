'''

https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

***Test case:
"bab"
"aba"
"leetcode"
"practice"
"anagram"
"mangaar"
"friend"
"family"

'''
class Solution(object):
	def minSteps(self, s, t):
		mp_s = {}
		mp_t = {}
		for c in s:
			if(c in mp_s): mp_s[c] += 1
			else: mp_s[c] = 1 

		for c in t:
			if(c in mp_t): mp_t[c] += 1
			else: mp_t[c] = 1
		rst = 0
		for item in mp_s:
			if(item in mp_t and mp_s[item] > mp_t[item]):
				rst += mp_s[item] - mp_t[item]
			elif(item not in mp_t):
				rst += mp_s[item]
		return rst