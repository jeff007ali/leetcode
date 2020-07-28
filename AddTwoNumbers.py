# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = temp = ListNode(0)
        
        while l1 or l2 or carry:
            t1 = t2 = 0
            if l1:
                t1 = l1.val
                l1 = l1.next
            if l2:
                t2 = l2.val
                l2 = l2.next
            
            total = t1 + t2 + carry
            # carry = total // 10
            # val = total % 10

            carry, val = divmod(total, 10)
            
            temp.next = ListNode(val)
            temp = temp.next
            
        return root.next