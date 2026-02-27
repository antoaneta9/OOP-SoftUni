class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, element):
        if isinstance(element, str):
            self.data.append(element)
    
    def pop(self):
        if self.data:
            return self.data.pop()
        
        
    def top(self):
        if self.data:
            return self.data[-1]  
        
    
    def is_empty(self):
        if not self.data:
            return True
        return False
    
    def __str__(self):
        return "[" + ", ".join(reversed(self.data)) + "]"
    
ex1 = Stack()
ex1.push('love')
ex1.push('hey')
ex1.push('mine')
ex1.push('clear')
ex1.push('horror')
print(ex1.top())
print(ex1.is_empty())

print(ex1)
    
