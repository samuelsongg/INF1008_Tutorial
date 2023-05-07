# Write an algorithm that reverses the array s[0],...,s[n-1]. You may use array =
# [10,9,8,7,6,5,4,3,2,1] as an example.

a = []  # to store original array
array_size = int(input("Enter the array size: "))
for i in range(0, array_size):
    x = int(input("Enter array element: "))
    a.append(x)
print(a)

# easy way
# reverse_a = a[::-1]
# print(reverse_a)

# harder way
b = []  # to store reversed array
for i in range(0, array_size):
    b.append(a[-i-1])
print(b)
