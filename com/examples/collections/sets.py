#creating sets

set1 = {1,10,1,20,20,10,5,3,6}
print(set1)

set2 = set()
set2.add(1)
set2.add(1)
set2.add(10)
set2.add(10)
set2.add(15)
set2.add(15)

print("Set2 ", set2)

set3 = {num for num in set1 if num > 5}
print("Numbers greater then 5 ", set3)

A = {1,2,3,4,5}
B = {3,4,5,6,7}
print(" A - B : ", A - B)
print(" B- A : ", B-A)
print("A-B B-A : ", A^B)
print("A and B : ", A&B)
print("A or B : ", A|B)

A = {1,2,3}
B = {1,2,3,4,5}
print("A is subset of B ", A < B)
print("B is subset of A ", B < A)

# do the above examples with set methods


