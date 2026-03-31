from math import floor
roman_nums = {
    'I': 1,
    'V': 5,
    'X': 10,
'L': 50,
'C': 100,
    'D': 500,
'M': 1000,}
class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return 'value is not a float'
        return cls(floor(float_value))

    @classmethod
    def from_roman(cls, value):
        int_value = 0
        for i in range(len(value)):
            if value[i] in roman_nums:
                if i + 1 < len(value) and roman_nums[value[i]] < roman_nums[value[i + 1]]:
                    int_value -= roman_nums[value[i]]
                else:
                    int_value += roman_nums[value[i]]
        return cls(int_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return 'wrong type'
        return cls(int(value))


