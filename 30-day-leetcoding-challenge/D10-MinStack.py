class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = [] 

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        p = self.stack.pop()
        self.push(p)
        return p

    def getMin(self) -> int:
        return min(self.stack)


# Different implememtation
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min) == 0 or self.min[-1] >= x:
            self.min.append(x)

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(1)
# obj.push(2)
# obj.push(3)
# obj.pop()
# print(obj.top())
# print(obj.stack)
# print(obj.getMin())

minStack = MinStack1()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())