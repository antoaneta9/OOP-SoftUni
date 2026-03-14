class take_skip:
    def __init__(self, step:int, count: int):
        self.step = step
        self.count = count
        self.current = 0
        self.generated = 0

    def __iter__(self):
        return self
    def __next__(self):
        # from 0 with given count with step
        if self.generated >= self.count:
            raise StopIteration
        value = self.current
        self.current += self.step
        self.generated += 1
        return value