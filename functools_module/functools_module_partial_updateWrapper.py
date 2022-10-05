"""
    functools => partial
"""

from functools  import partial, update_wrapper


## Normal ##

def multi(x,y):
    return x*y

def double(x):
    return x*2

def triple(x):
    return x*3



## USE partial ##

def multi(x,y):
    """multi function"""
    return x*y

double = partial(multi, y=2)
triple = partial(multi, y=3)


print(double(8)) 
# 16

print(triple(7)) 
# 21



#################################
#### Update_Wrapper #############
#################################


## WithOut Update_Wrapper ##

print(double.__name__)
# AttributeError

print(double.__doc__)
# No support docstring



## USE Update_Wrapper ##

update_wrapper(double, multi)

print(double.__name__)

print(double.__doc__)
