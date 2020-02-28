j'''
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

***Brute force
'''
class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        cnt = 0
        m = len(grid)
        if m == 0 : return 0
        n = len(grid[0])
        if n == 0 : return 0
        for i in range(m):
            for j in range((n)):
                if(grid[i][j]<0):
                    cnt+=1
        return cnt