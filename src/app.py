# Basic Operations

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b 

def div(a,b):
    if b == 0:
        return "error: cannot divide by 0"
    return a/b 

import math

def log(a, base=math.e):
    if a <= 0:
        return("error: a must be > 0")
    if base <= 0 or base == 1:
        return("error: base must be > 1")
    return math.log(a, base) 

def square(a):
    return a*a

def sin(a):
    return math.sin(a)

def cos(a):
    return math.cos(a)

def sqrt(a):
    if a < 0:
        return ("error: value must be > 0")
    return math.sqrt(a)

def percent(a,b):
    return a * (b/100) 