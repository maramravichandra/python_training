add_10 = lambda x: x + 10
print(" Adding 10 : ", add_10(10) )

numbers = [1,2,3,4,5,7]
multiple_by2 = list(map(lambda x: x *2, numbers))
even_odd_list = list(map(lambda x: x%2 == 0, numbers))

print("Multiply by 2 : ", multiple_by2)
print("Even or Odd : ", even_odd_list)
print("True Or False : ", 2%2 == 0)

print("Even Or ODD with For loop :", [ x%2 == 0  for x in numbers] )
print("Multiply by 2 in list : ", [ x*2 for x in numbers])
print("Only even numbers : ", [x for x in numbers if x % 2 == 0] )
print("Only Odd numbers : ", [x for x in numbers if x % 2 != 0] )

print("Is number exists : ", 2 in numbers)
print("Is number exists : ", {1,2}.issubset(numbers))

#   [ x for x in numbers if x % 2 == 0 ]

# replace in numbers list if even number with True, odd Number with False
# output = [False,True,False,True,False,False]

nums = list(range(1, 10))

