'''


https://leetcode.com/problems/rank-teams-by-votes/

'''

class Solution(object):
	def rankTeams(self, votes):
		p = len(votes[0])
		print(p)
		mp = {}
		
		for vote in votes:
			for i, v in enumerate(vote):
				if(v in mp):
					mp[v][i] += 1 
				else:
					mp[v] = [0]*p
					mp[v][i] += 1 
		for key in mp:
			tmp = mp[key]
			tmp.append(  (-1) * ( ord(key) ) )			
			mp[key] = tmp
		print(mp)
		
		rst = ''

		for item in sorted(mp.items(), key = lambda  x: (x[1]), reverse = True):
			rst = rst + item[0]
		return rst