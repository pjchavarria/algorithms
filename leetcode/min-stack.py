# https://leetcode.com/problems/min-stack/
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.stack:
            self.min = x
            self.stack.append(0)
        else:
            self.stack.append(x - self.min)
            if x < self.min:
                self.min = x
        

    def pop(self):
        """
        :rtype: nothing
        """
        x = self.stack.pop()
        if x < 0:
            self.min = self.min - x


    def top(self):
        """
        :rtype: int
        """
        x = self.stack[-1]
        if x > 0:
            return x + self.min
        else:
            return self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min

stack = MinStack()

stack.push(30)
stack.push(10)
stack.push(20)
stack.push(1)
print stack.pop(), 1
stack.top()
print stack.getMin(), 10