# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = dummy = ListNode()
        value,last = 0,0
        while l1 or l2 or last:
            value = last
            if l1: value += l1.val
            if l2: value += l2.val

            last , res.val = divmod(value,10)
            res.next = ListNode()
            pre = res
            res = res.next

            if l1:l1 = l1.next
            if l2:l2 = l2.next
            

        if res.val == 0:
            pre.next = None

        return dummy
