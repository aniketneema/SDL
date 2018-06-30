A=set([1,2,3,4])
B=set([3,4,5,6])

print (len(A))

print(2 in A)

print(5 in A)
print("union:",A | B)
print("intersection:",A & B)
print("Symmetric difference :", A ^ B)
print("Difference :", A - B)
A.add(41)
print(A)
A.discard(41)
print(A)
A.pop()
print(A)

