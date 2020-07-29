# SINGLE LINE FUNCTION DEFINITIONS
# <function> = lambda: <return_value>
# <function> = lambda <argument_1>, <argument_2>: <return_value>

# COMPREHENSIONS
# <list> = [i+1 for i in range(10)]                   # [1, 2, ..., 10]
# <set>  = {i for i in range(10) if i > 5}            # {6, 7, 8, 9}
# <iter> = (i+5 for i in range(10))                   # (5, 6, ..., 14)
# <dict> = {i: i*2 for i in range(10)}                # {0: 0, 1: 2, ..., 9: 18}

# EXAMPLE
# out = [i+j for i in range(10) for j in range(10)]

# Is the same as:

# out = []
# for i in range(10):
#     for j in range(10):
#         out.append(i+j)

### MAP, FILTER, REDUCE
# from functools import reduce
# <iter> = map(lambda x: x + 1, range(10))            # (1, 2, ..., 10)
# <iter> = filter(lambda x: x > 5, range(10))         # (6, 7, 8, 9)
# <obj>  = reduce(lambda out, x: out + x, range(10))  # 45

# Any, All

# <bool> = any(<collection>)                          # False if empty.
# <bool> = all(el[1] for el in <collection>)          # True if empty.

# If - Else

# <obj> = <expression_if_true> if <condition> else <expression_if_false>

# >>> [a if a else 'zero' for a in (0, 1, 2, 3)]
# ['zero', 1, 2, 3]

# Namedtuple, Enum, Dataclass

# from collections import namedtuple
# Point     = namedtuple('Point', 'x y')
# point     = Point(0, 0)

# from enum import Enum
# Direction = Enum('Direction', 'n e s w')
# direction = Direction.n

# from dataclasses import make_dataclass
# Creature  = make_dataclass('Creature', ['location', 'direction'])
# creature  = Creature(Point(0, 0), Direction.n)