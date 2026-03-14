class vowels:
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'y']
    def __init__(self, string):
        self.string = string
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        while self.index < len(self.string):
            char = self.string[self.index]
            self.index += 1
            if char.lower() in self.vowels_list:
                return char
        raise StopIteration