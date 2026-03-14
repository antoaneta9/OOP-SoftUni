class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >=self.number:
            raise StopIteration
        index = self.current % len(self.sequence)
        value = self.sequence[index]
        self.current += 1
        return value