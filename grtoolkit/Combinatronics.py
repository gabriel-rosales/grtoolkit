# from itertools import *

# >>> product([0, 1], repeat=3)
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1),
#  (1, 0, 0), (1, 0, 1), (1, 1, 0), (1, 1, 1)]

# >>> product('ab', '12')
# [('a', '1'), ('a', '2'),
#  ('b', '1'), ('b', '2')]

# >>> combinations('abc', 2)
# [('a', 'b'), ('a', 'c'),
#  ('b', 'c')]

# >>> combinations_with_replacement('abc', 2)
# [('a', 'a'), ('a', 'b'), ('a', 'c'),
#  ('b', 'b'), ('b', 'c'),
#  ('c', 'c')]

# >>> permutations('abc', 2)
# [('a', 'b'), ('a', 'c'),
#  ('b', 'a'), ('b', 'c'),
#  ('c', 'a'), ('c', 'b')]

from grtoolkit.Storage import File
from grtoolkit.Decorators import timer
import itertools

@timer
def generateAllStringCombinations(comboLength, chars='default', fileName=None):
    if chars == 'default':
        chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    ci = iter(itertools.product(chars,repeat=comboLength))
    # combinations = []
    sFile = File(fileName)
    
    while True:
        try:
            # combinations.append(''.join(next(ci)))
            sFile.write_and_append(''.join(next(ci)) + ',')
        except StopIteration:
            break

if __name__ == "__main__":
    print(len('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-_0123456789'))