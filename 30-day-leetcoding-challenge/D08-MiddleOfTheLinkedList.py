class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return f"ListNode{{{self.val} next:{self.next}}}"

def generate_link_list(l):
    f_obj = None
    p_obj = None
    for x in reversed(l):
        x = ListNode(x)
        if f_obj is None:
            x.next = None
            f_obj = x
            p_obj = x
            continue
        else:
            x.next = p_obj
        f_obj = x
        p_obj = x
    return f_obj


# First method - brute force
def middleNode1(head):
    print("In method 1")

    OG = head
    nodeCount = 0
    while head:
        nodeCount += 1
        head = head.next
    
    middleNo = nodeCount // 2
    print(middleNo)
    
    for _ in range(middleNo):
        OG = OG.next
    
    return OG


# Second method
# Put every node into an array A in order. 
# Then the middle node is just A[A.length // 2], since we can retrieve each node by index.
def middleNode2(head):
    print("In method 2")

    temp = [head]

    while temp[-1].next:
        temp.append(temp[-1].next)
    
    middleNo = len(temp) // 2

    return temp[middleNo]


# Third method
# When traversing the list with a pointer slow, 
# make another pointer fast that traverses twice as fast. 
# When fast reaches the end of the list, slow must be in the middle.
def middleNode3(head):
    print("In method 3")

    normal = double = head
    while double and double.next:
        normal = normal.next
        double = double.next.next
    
    return normal


link_list = generate_link_list([1,2,3,4,5])
print(middleNode3(link_list))
            