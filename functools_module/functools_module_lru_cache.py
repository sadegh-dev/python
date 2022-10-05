"""
    lru_cache
        - lru : list recently use
"""

#########################
## lru_cache ############
#########################

from functools import lru_cache



# default
#@lru_cache

# Set MaxSize
@lru_cache(maxsize=10)
def do_add (x,y):
    print(f'processing {x} + {y} ...')
    return x+y



do_add(5,3)
do_add(4,7)
do_add(5,3) # result from cache

# Cache Info
info = do_add.cache_info()
print(info)
# CacheInfo( hits=1, misses=1, maxsize=128, currsize=1)



# Clear Cache
#do_add.cache_clear()


#########################
## cache ################
#########################

from functools import cache


@cache
def do_multi (x,y):
    print(f'processing {x} * {y} ...')
    return x*y


do_multi(5,8)
do_multi(9,80)
do_multi(5,8)