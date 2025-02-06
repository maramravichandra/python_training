# 2 numbers 5 and 10 . swap these numbers and print
# Print actual numbers then print swapped numbers
import datetime


def swap(x,y):
    print(f"Before Swapping x,y = {x},{y}")
    temp = x
    x = y
    y = temp
    print(f"After swapping x,y = {x},{y}")

swap(5,10)
swap(10,20)

#Prime numbers 2,3,5,7,11....
#A number which is dividable with 1 or itself is called Prime number
#Write a method to find out given number is Prime number or not.
print( list(range(1,3)))
def is_prime_number(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for n in range(3, num):
            if num % n == 0:
                return False
        return True

print("5 is prime or not : ", is_prime_number(5))
print("7 is prime or not : ", is_prime_number(7))
print("9 is prime or not : ", is_prime_number(9))

#List the prime numbers with in the range . (5,20)
start = 1
end = 10
prime_numbers = list()
start_time = datetime.datetime.now()
print(start_time)
for i in range(start,end+1):
    if is_prime_number(i):
        prime_numbers.append(i)

print(f"Prime numbers in the range({start},{end}) : ", prime_numbers)
print("Time Taken : ", datetime.datetime.now() - start_time)

# cumulative sum for given range (5,10) [ 1+2+3+4 , 1+2+3+4+5, 1+2+3+4+5+6 ...]

start = 90000
end = 100000
sums = list()
start_time = datetime.datetime.now()
print("Start Time", start_time)

def cal_sum(num):
    sum = 0
    l = len(sums)
    if  l == 0:
        for n in range(1,num+1):
            sum = n + sum
    else:
        sum = num + sums[l-1]
    return sum

for i in range(start,end):
    sums.append(cal_sum(i))

print("Sum : ", sums)
print("Time Taken : ", datetime.datetime.now() - start_time)




