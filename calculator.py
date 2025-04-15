import math

def square_root(a):
    if a < 0:
        raise ValueError("square_root: a must be non-negative")
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero: the divisor 'a' must not be zero.")
    return b / a

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm: require a > 0, a != 1, and b > 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b
