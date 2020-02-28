'''
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/
TLE
***test case:

[[1,2],[2,3],[3,4]]
[[1,2],[2,3],[3,4],[1,2]]
[[1,4],[4,4],[2,2],[3,4],[1,1]]
[[1,100000]]
[[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
[[1,5],[1,5],[1,5],[2,3],[2,3]]
'''

class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        rst = set()
        
        for event in sorted(events, key = lambda x : x[1]):
            start, end = event[0], event[1]
            for day in range(start, end+1):
                if(day not in rst):
                    rst.add(day)
                    break
        return len(rst)
        