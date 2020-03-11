'''
https://leetcode.com/problems/linked-list-cycle-ii/

***Complexity:
time: O(n)
space: O(n)
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        pos = 0
        mp = {}
        while(head):
            if(head in mp): return mp[head]
            else: mp[head] = head
            head = head.next
            pos = pos +1 
        return None
