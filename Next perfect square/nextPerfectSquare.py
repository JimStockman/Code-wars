import math

def find_next_square(sq):
  d = math.sqrt(sq)
  return (d + 1) ** 2 if d == int(d) else -1


def best_find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1

"""
4 ** 0.5 = 2
4 ** 1 = 4
4 ** 2 = 16
"""
