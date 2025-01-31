def custom_print(message):
    print("Printing Message : {}".format(message))

custom_print("Hi")
custom_print("Hello")
custom_print("How are you?")

# Mandatory Parameters
def add(num1, num2):
    result = num1 + num2
    print("Result : ", result)
    return result

result1 = add(10,10)
result2 = add( result1 , 10)
print("Result 2 ", result2)

# Using optional parameter
def add_optional( num1:int, num2:int, num3:int=10):
    result = num1 + num2 + num3
    return result

print("Add Optional Result 1 ", add_optional(100,100,100))
print("Add Optional Result 2", add_optional(100,100))

# Allowing unlimited parameters to the function
def add_unlimited( *numbers ):
    result = 0
    for number in numbers:
        if type(number) is int:
            result = result + number
        else:
            #print("Ignoring value as it is not integer type ", number)
            print("Since we got non integer value we no longer performing this function.")
            return

    return result

print("Print Unlimited values result ", add_unlimited(10,10,10,10,10,10,20,20,100,100,800,500, "Hi", True, ["a", "b"], 100, 500, 1000))

"""
Implement function using naming parameters 
"""
def just_say_hello( name = "", message="Greeting!!", param1=0, param2=1):
    print( "Hi {0} , {1}" .format(name, message, param1, param2) )

just_say_hello(name="Ravi", message="How are you?")

just_say_hello(message="How are you?")
just_say_hello(name="Ravi")


globals()
def add(num1, num2):
    result = num1 + num2

print("Result")





