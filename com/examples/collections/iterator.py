from distributed.utils_test import throws

my_range = range(1,4)
my_iter = my_range.__iter__()
print( my_iter.__next__() )
print( my_iter.__next__() )
print( my_iter.__next__() )

# even as start value = even + 2
# odd as start value = next even is odd + 1
"""
user gave 1 as start value 
next is 2 

start value  = 0 + 2 = 2 

"""

"""
This class is a iterator and it gives even numbers
We can create this object like below 
even_numbers = EvenNumbers(1,10) # here 1 is start value and 10 is end value
this iterator will print even numbers with in 1 to 10 range.
"""
class EvenNumbers:
    start = 0
    end = 0

    """
    This is constructor
    start is start value of the iterator
    end is end value of the iterator
    """
    def __init__(self, start, end):
        if start % 2 == 0 :
            self.start = start
        elif start <= 1:
            self.start = 0
        else:
            self.start = start - 1
        self.end = end

    def __iter__(self):
        return self

    """
    """
    def __next__(self):
        self.start = self.start + 2
        if self.start > self.end:
            throws("Limit exceeded")
        return self.start

even_iter = EvenNumbers(0,10)
print(even_iter.__next__())
print(even_iter.__next__())
print(even_iter.__next__())
print(even_iter.__next__())
print(even_iter.__next__())
