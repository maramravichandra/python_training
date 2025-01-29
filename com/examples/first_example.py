import sys
from utils.number_util import sum

numbers = sys.argv[1:]
print(numbers)

result = sum(numbers)

print("Sum of numbers is ", result)

sum(numbers)


