# 232
# https://leetcode.com/problems/implement-queue-using-stacks/description/

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        # use two stack to simulate queue

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        self.dumpStackIn()
        return self.stack_out.pop()

    def peek(self) -> int:
        self.dumpStackIn()
        return self.stack_out[-1]       #do not use pop here, Return the last element without removing it

    def empty(self) -> bool:
        return not (self.stack_in or self.stack_out)

    # if stack_out is empty, move every element from stack_in to stack_out
    def dumpStackIn(self):
        if self.stack_out:
            return
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()