number = 0
result = 0
sample_addition = 10
max_addition = 100

#  select * from emp limit 10

# select * from emp

while number <= sample_addition:
    result = result + number
    number = number + 1
    if number == 10:
        print("Since this logic is working for {} number, we are continuing till {}".format(sample_addition, max_addition))
        sample_addition = max_addition

print( "Sum of 1 to {}  is {}".format(number - 1, result))

number = 0
while True:
    print("Number is ", number)
    number = number + 1
    if number > 10:
         break