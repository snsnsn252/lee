# 225
# https://leetcode.com/problems/implement-stack-using-queues/description/

from collections import deque
class MyStack:

    def __init__(self):
        self.que = deque()

    def push(self, x: int) -> None:
        self.que.append(x)

    def pop(self) -> int:
        self.rePosition()
        return self.que.popleft()

    def top(self) -> int:
        #self.rePosition()
        return self.que[-1]

    def empty(self) -> bool:
        return not self.que

    def rePosition(self):
        size = len(self.que) - 1
        for _ in range (size):
            self.que.append(self.que.popleft())
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()