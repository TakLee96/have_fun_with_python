__author__ = 'lijiahang'

def find_modular_coordinate(x, y, value):
    """Find such pair of numbers (a, b) such that
       value = a * x + b * y

    >>> find_modular_coordinate(5, 3, 2)
    [1, -1]

    >>> find_modular_coordinate(19, 12, 2)
    [2, -3]
    """
    assert gcd(x, y) == 1, "Error: the greatest common divisor must be 1"
    b = 1
    multiple_of_y = y

    while (multiple_of_y - value) % x != 0:
        multiple_of_y += y
        b += 1

    a = value // x - multiple_of_y // x

    new_a = a + y
    new_b = b - x

    if abs(new_a - new_b) < abs(a - b):
        return [new_a, new_b]
    else:
        return [a, b]

def gcd(x, y):
    """Find the greatest common divisor of x and y

    >>> gcd(12, 19)
    1

    >>> gcd(12, 15)
    3

    >>> gcd(18, 12)
    6
    """
    #assert x >= 0 and y >= 0 and type(x) == int and type(y) == int, "Error: invalid input"

    if y > x:
        return gcd(y, x)
    elif y == 0:
        return x
    else:
        return gcd(y, x % y)

def egcd(x, y):
    d = gcd(x, y)
    if y > x:
        return egcd(y, x)
    elif y == 0:
        return (x, 1, 0)
    else:
        d, a, b = egcd(y, x % y)
        return (d, b, a - (x // y) * b)

def solve(a, b, m):
    step = 1
    x = []
    while step < m:
        if step * a % m == b:
            x.append(step)
        step += 1
    return x

def crt(a, ra, b, rb, c, rc):
    step = 1
    while step < 10000:
        if step % a == ra % a and step % b == rb % b and step % c == rc % c:
            return step
        step += 1
    return "Not found"

def inverse(p, q):
    step = 0
    while step < 10000:
        if p * step % q == 1:
            return step
        step += 1
    return "Not found"