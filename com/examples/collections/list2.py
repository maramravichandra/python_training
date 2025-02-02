nums = list(range(1,51))
print(nums)

dups = [1,1,1,1,2,2,5,5,10,10,5]
print(dups.count(1))
print("Size of the List ", len(dups))
print("Sum of all elements", sum(dups))

# retrieve elements
print("10Th element : ", nums[10])
# check element existed or not
print("15 value existed in index ", nums.index(15))

# to check element existed or not
print( nums.count(100))

#find out max element in a list
max = 0
for num in nums:
    if num > max:
        max = num

print("Max Value ", max)

dups.sort(reverse=True)
print("Max element sorted and reversed", dups[0])

dups.sort()
print("Max element sorted", dups[len(dups)-1])

list1 = ['Asdafdasf',1,3,4,5,True,'B']
#list1.sort() we can't sort the list if it contains alpha numberic values/different types

letters = ['A','B','A','C','B']
letters.sort()
print("Sorted ", letters)

list2 = ['Asdafdasf',1,3,4,5,True,'B',10]
#slicing list[start:stop:step]

print("Numbers ", list2[1:5:1])
print("Numbers with step ", list2[1:5:2])

list3 = []
for value in list2:
    if type(value) is int:
        list3.append(value)

print("Numbers only ", list3)

list2 = ['Asdafdasf',1,3,4,5,True,'B',10]
print("list only 3 elements from 0th index ", list2[0:3])
print("list only 3 elements from last index ", list2[-3:])

print("Numbers ", nums)
print("Odd numbers from nums ", nums[::2])
print("Even numbers from nums ", nums[1::2])

even_numbers = []
odd_numbers = []
for num in nums:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

print("Even Numbers ", even_numbers)
print("Odd Numbers ", odd_numbers)

dups = [1,1,1,1,2,2,5,5,10,10,5]

unique_list = []
for num in dups:
    if unique_list.count(num) == 0:
        unique_list.append(num)

print("Unique list ", unique_list)

print("Using set ", set(dups))

print("numbers greater then 5 ", [num for num in dups if num > 5 ] )



