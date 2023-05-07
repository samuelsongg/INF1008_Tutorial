# Write an algorithm that output the smallest and the second smallest values in the
# array s[0],...s[n-1]. Assume that n>1 and the values in the array are distinct. You may
# array = [6,20,9,12,8,7,15,31,16] as an example.

a = []
array_size = int(input("Enter the array size: "))
for i in range(0, array_size):
    x = int(input("Enter array element: "))
    a.append(x)

s1 = a[0]  # assume smallest is at index 0
s1_index = 0

for i in range(0, array_size):
    if a[i] < s1:
        s1 = a[i]
        s1_index = i

# set 2nd smallest to be either index 0 or 1 depending on s1
if s1_index == 0:
    s2 = a[1]
else:
    s2 = a[0]

for i in range(0, array_size):
    if a[i] < s2 and s1_index != i:
        s2 = a[i]

print("The smallest value is: " + str(s1))
print("The 2nd smallest value is: " + str(s2))
