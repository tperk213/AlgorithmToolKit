
class MinMaxStack():

    def __init__(self):
        self.stack = []
        self.curMin = float("inf")
        self.curMax = float("-inf")
        self.min = []
        self.max = []
    
    def peek(self):
        return self.stack[-1]
    
    def pop(self):
        self.min.pop()
        self.curMin = self.min[-1]
        self.max.pop()
        self.curMax = self.max[-1]
        return self.stack.pop()

    
    def push(self, val):
        self.stack.append(val)
        if val < self.curMin:
            self.curMin = val
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        if val > self.curMax:
            self.curMax = val
            self.max.append(val)
        else:
            self.max.append(self.max[-1])
    
    def getMin(self):
        return self.min[-1]
    
    def getMax(self):
        return self.max[-1]


if __name__ =="__main__":
    a = MinMaxStack()
    a.push(2)
    a.push(0)
    a.push(5)
    a.push(4)
    a.pop()
    a.pop()
    a.push(4)
    a.push(11)
    a.push(-11)
    a.pop()
    a.pop()
    a.pop()
    a.pop()
    a.pop()
    a.push(6)
    a.pop()
    print("done")
    
    