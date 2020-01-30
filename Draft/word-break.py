''' wrong answer

https://leetcode.com/problems/word-break/

***approach: using map pass these cases of example 

BUT wrong answer:

"aaaaaaa"
["aaaa","aaa"]


"aaaaaaab"
["a","ab"]

'''
class Solution(object):
	def wordBreak(self, s, wordDict):
		mp = {}
		for item in wordDict:
			mp[item]= True 
		i = 0
		pos = 1
		n = len(s)  # s = "leetcode", wordDict = ["leet", "code"]
		while(pos<=n):
			if(s[i:pos] not in mp):
				pos +=1
			else:
				print(s[i:pos])
				i = pos
				pos +=1
		print(i)
		if(i == n): return True
		else: return False	
