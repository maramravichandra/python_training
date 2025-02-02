# initialization
l = list([1,2,3,5,10])
print(l)

l = list( (1,2,3,6,5,10))
print(l)

l = list( range(1, 51) )
print(l)
print( l[0], l[10], l[49])

# append elements/ adding
l.append("Ravi")
print(l)

#change/update/replace the value at specific index
l[10] = 100
print(l[10])

#removing element
l.remove(100)
print(l)
print( len(l), l[10])

print( "Pop element ", l.pop() )
print("List after pop ", l)

print( "Pop element at 20 ", l[20], l.pop(20) )
print("List after pop ", l)

del l[0]
print("After del l[0] : ", l)

l1 = list( range(1,5) )
l2 = ["r",'0']

l3 = l1 + l2
print("L3 : ", l3)

l1.extend(l2)
print("L1 after extend : ", l1)

del l1
print("Remove everything from L ", l)

# l.clear()
# print("After clear ", l)
# l = []

print("Length of list ", len(l))







