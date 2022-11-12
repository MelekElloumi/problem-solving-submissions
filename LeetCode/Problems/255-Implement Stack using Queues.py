from collections import deque

class MyStack:

    def __init__(self):
        self.q1=deque()
        self.q2=deque()

    def push(self, x: int) -> None:
        if self.empty():
            self.q1.appendleft(x)
            return
        while not self.empty():
            self.q2.appendleft(self.q1.pop())
        self.q1.appendleft(x)
        while len(self.q2)!=0:
            self.q1.appendleft(self.q2.pop())

    def pop(self) -> int:
        return self.q1.pop()

    def top(self) -> int:
        return self.q1[-1]

    def empty(self) -> bool:
        return len(self.q1)==0