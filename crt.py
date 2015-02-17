from operator import mul
from functools import reduce

def crt(array):
    mod_bases = [3, 5, 7, 11, 13]
    count, total = 0, 0
    for elem in array:
        if type(elem) != int:
            mod_bases.pop(count)
            array.pop(count)
        count += 1
    for i in range(len(array)):
        rest_product = rest(mod_bases, i)
        total += array[i] * rest_product * inverse(rest_product, mod_bases[i])
    return total % reduce(mul, mod_bases, 1)

def rest(mod_bases, num):
    index, length, product = 0, len(mod_bases), 1
    while index < length:
        if index != num:
            product *= mod_bases[index]
        index += 1
    return product

def inverse(x, y):
    """Compute x^-1 mod y"""
    for i in range(y):
        if x * i % y == 1:
            return i
    return 1 / 0
