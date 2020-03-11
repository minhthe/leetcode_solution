'''
https://leetcode.com/problems/happy-number/

approach:  hash + recursion


*** learn more:

1) not using the power 2
https://leetcode.com/problems/happy-number/discuss/445373/Python-Dictionary-and-Set-beat-99-time-and-100-space

def isHappy(self, n: int) -> bool:
        dict = {'0':0,'1':1,'2':4,'3':9,'4':16,'5':25,'6':36,'7':49,'8':64,'9':81}
        sum_set = set()
        res = sum([dict[x] for x in str(n)])
        if res == 1: return True
        while res != 1:
            if res in sum_set:
                return False
            else:
                sum_set.add(res)
                res = sum([dict[x] for x in str(res)])
                if res == 1: return True

class Solution:
    def isHappy(self, n: int) -> bool:
        
        mp = {}
        
        arr = list(int(x) * int(x) for x in list(str(n)))
        
        tmp = sum(arr)
        
        while(tmp!=1):
            if(  tmp in mp): return False
            else: mp[tmp] = True
            arr =  list(int(x) * int(x) for x in list(str(tmp)))
            tmp = sum(arr)
        return True
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