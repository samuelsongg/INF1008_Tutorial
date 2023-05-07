# Write an algorithm that returns the index of the first occurrence of the largest
# element in an array s[0],...,s[n-1]. You may use array = [6,12,7,5,3,20,10,5] as an
# example.

a = []
array_size = int(input("Enter the array size: "))
for i in range(0, array_size):
    x = int(input("Enter array element: "))
    a.append(x)

largest = a[0]  # assume largest is at index 0

for i in range(1, array_size):
    if a[i] > largest:
        largest = a[i]

print("The largest element in the array is: " + str(largest))
