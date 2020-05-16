# Method 1 - Using temp variable

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return None
        
        temp = odd = head
        temp1 = even = head.next
        
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            
            odd = odd.next
            even = even.next
            
            
        odd.next = temp1
        
        return temp

#TODO: try to find more efficient way, may be using (if index % 2 == 0)