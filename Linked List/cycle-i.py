'''
https://leetcode.com/problems/linked-list-cycle/

***refer:
https://hoangdinhquang.me/a-note-on-detecting-cycle-floyd-algorithm/

***Complexity:
space: O(n)
time: O(n)
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        tmp = head
        fst = tmp
        snd = tmp
        while(fst and snd and snd.next):             
            fst = fst.next
            snd = snd.next.next
            if(fst == snd): return True
        return False