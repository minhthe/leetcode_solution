class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        
        n2 = n //2 
        
        tmp = {}
        
        for item in arr:
            if(item in tmp):
                tmp[item] += 1
            else:
                tmp[item] = 1
    
        cnt = 0
        for item in sorted(tmp.items(), key = lambda x : x[1], reverse = True):
            if(n2 > 0):
                cnt+=1
                n2 = n2 - item[1]
        return cnt
        