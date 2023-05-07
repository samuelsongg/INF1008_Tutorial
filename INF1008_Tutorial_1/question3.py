# Given an array s[0],...,s[n-1] such that n > 1 and s[i] ≤ s[i+1] for all i. Write an algorithm
# that inserts an input value x into the array so that s[i] ≤ s[i+1] for all i.- You may use
# array = [1,3,5,7,11,13,15], and then insert 9 as an example.

a = []
array_size = int(input("Enter the array size: "))
for i in range(0, array_size):
    x = int(input("Enter array element: "))
    a.append(x)

x = int(input("Enter a number to insert into the array: "))

for i in range(0, array_size):
    if a[i] > x:
        a.insert(i, x)

print(a)