class MinStack:

    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((x, min(x,self.getMin()))) 
           
    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return math.inf