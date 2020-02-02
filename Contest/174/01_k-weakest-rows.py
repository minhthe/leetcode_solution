class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        a = []
        if(len(mat) == 0 or k == 0 ): return []
        id = -1
        for row in mat:
            id = id+1
            a.append((row.count(1), id))
        rst = []
    
        for item in sorted(a):
            if(k > 0):
                rst.append(item[1])
                k -= 1
            
        return rst
    