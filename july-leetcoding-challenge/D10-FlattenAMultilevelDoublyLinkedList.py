# Method - 1 ---- using DFS

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def dfs(node):
            if not node:
                return None, None
            trav = node
            head = node
            tail = node
            while trav:
                if trav.child:
                    nex = trav.next
                    insert, last = dfs(trav.child)
                    trav.next = insert
                    insert.prev = trav
                    if nex:
                        last.next = nex
                        nex.prev = last
                    trav.child = None
                    trav = last
                tail = trav
                trav = trav.next
            return head, tail
        
        return dfs(head)[0]







# Method - 2

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while p:
            if not p.child:
                p = p.next
            else:
                q = p.child
                while q.next:
                    q = q.next
                q.next = p.next
                if p.next:
                    p.next.prev = q
                p.next = p.child
                p.child.prev = p
                p.child = None
        return head