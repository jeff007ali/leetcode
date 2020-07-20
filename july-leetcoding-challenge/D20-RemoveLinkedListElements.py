# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        temp = ListNode(-1)
        temp.next = head
        t = temp
        
        while t != None and t.next != None:
            if t.next.val == val:
                t.next = t.next.next
            else:
                t = t.next
                
        return temp.next
        