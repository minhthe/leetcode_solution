'''
https://leetcode.com/problems/linked-list-cycle/

***complexity:
time:  O(n)
space: O(1)
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        mp = {}
        while(head):
            if(head in mp): return True
            else: mp[head] = True
            head = head.next
        return False