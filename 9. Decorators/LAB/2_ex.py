def vowel_filter(function):
    def wrapper():
        vowels_list = ["a", "e", "i", "o", "u", "y"]
        result = function()
        filtered = [el.lower() for el in result if el in vowels_list]
        return filtered
    return wrapper

# test code
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]
print(get_letters())