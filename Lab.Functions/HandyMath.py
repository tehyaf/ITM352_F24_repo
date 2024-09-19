def squareroot(x):
     return x**0.5

def midpoint(x1, x2):
     return (x1+x2) / 2
def exponent(x, y):
     return x**y 
def max(x, y):
     return (x>y) * x + (y>x) * y
def min(x, y): 
     return (x<y) * x + (y<x) * y

def apply_function(x, y, func):
    return f"The function {func.__name__}({x}, {y}) = {func(x, y)}"
