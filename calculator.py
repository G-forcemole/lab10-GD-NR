#https://github.com/G-forcemole/lab10-GD-NR/blob/main/test_calculator.py
# Partner 1: Gabriel Dos Santos
# Partner 2: Noah Robinson


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

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm: require a > 0, a != 1, and b > 0.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

import math

def add(a, b):

    return a + b

def sub(a, b):

    return a - b

def mul(a, b):

    return a * b

def div(a, b):

    if a == 0:
        raise ZeroDivisionError("Denominator 'a' cannot be zero")
    return b / a

def log(a, b):

    if a <= 0 or a == 1:
        raise ValueError("Base 'a' must be positive and not equal to 1")
    if b <= 0:
        raise ValueError("Argument 'b' must be positive")
    return math.log(b, a)

def exp(a, b):

    return a ** b