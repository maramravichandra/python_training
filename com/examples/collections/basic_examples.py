print( str(100) )
print( int('10') )

print( int(2.35))
print( float(2.35))

import random
print( random.randint(1,10))
print( random.randint(1,10))
print( random.randint(1,10))
print( random.randint(1,10))
print( random.randint(1,10))

print( float(1))

num = 2.58974
print( round(num, 2))
print( round(num))
print(round(2.35))

import math

print( math.floor(2.35))
print( math.ceil(2.35))


def custom_func(num):
    floor_val = math.floor(num)
    ceil_val = math.ceil(num)
    random_num = random.randint(0, num)
    return floor_val, ceil_val, random_num

