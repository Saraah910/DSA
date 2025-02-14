class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)
    
    def pop(self):
        if self.min_stack:
            top = self.stack.pop()
            if self.min_stack[-1] == top:
                self.min_stack.pop()

    def getTop(self):
        return self.stack[-1] if self.stack else None
    
    def minimum(self):
        return self.min_stack[-1] if self.min_stack else None
    
st = MinStack()
st.push(10)
st.push(6)
st.push(123)
st.pop()
print(st.minimum())
st.pop()
print(st.getTop())
