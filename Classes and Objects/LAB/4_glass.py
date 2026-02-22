class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0
    
    def fill(self, ml: int):
        self.ml = ml
        if self.content + self.ml >= self.capacity:
            return f"Cannot add {self.ml} ml"
        else:
            self.content += self.ml
            return f"Glass filled with {self.ml} ml"
    
    def empty(self):
        self.content = 0
        return "Glass is now empty"
    
    def info(self):
        return f"{self.capacity - self.content} ml left"

glass = Glass()

print(glass.fill(100))

print(glass.fill(200))

print(glass.empty())

print(glass.fill(200))

print(glass.info()) 
    