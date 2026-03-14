from itertools import permutations

def possible_permutations(lst):
    for p in permutations(lst):
        yield list(p)