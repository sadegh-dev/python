"""
    functools => partial
"""

from functools  import partial


# Normal

def multi(x,y):
    return x*y

def double(x):
    return x*2

def triple(x):
    return x*3



# USE partial

def multi(x,y):
    return x*y

double = partial(multi, y=2)
triple = partial(multi, y=3)


print(double(8)) #16
print(triple(7)) #21


