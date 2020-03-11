'''
https://leetcode.com/problems/linked-list-cycle-ii/
***Complexity
Time: O(n)
Space: O(1)
'''
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        first = head
        second = head
        while(first and second and second.next):
            first = first.next
            second = second.next.next
            if(first == second):
                first = head
                while(second!=first):
                    second = second.next
                    first = first.next
                return first
        return None