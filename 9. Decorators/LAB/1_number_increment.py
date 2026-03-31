def number_increment(numbers):
    def increase():
        for el in range(len(numbers)):
            numbers[el] += 1
        return numbers
    return increase()
print(number_increment([1, 2, 3]))