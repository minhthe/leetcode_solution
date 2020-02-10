'''
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/

This lcs approach will TLE result:
with test case: 1 <= s.length <= 50000 -> O(n^2)


***test case:
"bab"
"aba"
"leetcode"
"practice"
"anagram"
"mangaar"
"friend"
"family"

'''
def lcs(s, t, m ,n)		:
	rst = [[0 for i in range(n+1)] for j in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if(i == 0 or j == 0):
				rst[i][j] = 0
			elif(s[i-1] == t[j-1]):
				rst[i][j] = rst[i-1][j-1] + 1
			else:
				rst[i][j] = max( rst[i-1][j], rst[i][j-1])  
	return rst[m][n]
class Solution(object):
	def minSteps(self, s, t):
		s =  ''.join(sorted([x for x in s]))
		t = ''.join(sorted([x for x in t]))
		m , n = len(s), len(t)
		return m - lcs(s,t,m,n)