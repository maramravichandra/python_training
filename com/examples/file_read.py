import sys
from utils.number_util import sum

#reading arguments
file_location = sys.argv[1]

#read the file
#print( open(file_location, 'r').read())

result = 0
file = open(file_location)
for line in file.readlines():
    numbers = line.split()
    result = result + sum(numbers)

print('Result ', result)


"""
Implement a method to find out given number is even or not
True - for even number
False - for Odd number

"""