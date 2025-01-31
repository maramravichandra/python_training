tpl = (1,10,5,3) #immutable - can't change like you can't add or remove elements from collection
print( len(tpl) )
print("0th Element : ", tpl[0])

tpl2 = 1,10,5,3 # Another way of defining/initialising tuple
print( tpl2[1] )

tpl3 = (1, "Hello", True)
print(tpl3)

print("Iterating all elements")
for element in tpl:
    print(element)

i = 0
while i < len(tpl):
    print( tpl[i])
    i = i+1

print( tuple([1,2.5,10,50]) )

print( (*tpl, *tpl2, *tpl3 ) )

def get_employee_data():
    return "Emp Name", 35, 1000000

name, age, sal = get_employee_data()
print("Name : ", name)
print("age : ", age)
print("sal : ", sal)

tpl_result = (*tpl, 100)
print(tpl_result)
print("6Th Element : ", tpl_result[5])