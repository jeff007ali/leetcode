from collections import OrderedDict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.d = OrderedDict()
        self.s = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int:
        if len(self.d) == 0:
            return -1
        else:
            for i in self.d:
                return i

    def add(self, value: int) -> None:
        if value not in self.s:
            self.s.add(value)
            self.d[value] = None
        else:
            self.d.pop(value, None)
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)