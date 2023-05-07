# An algorithm for finding the maximum element of an array is in the following
#
#   def arrayMax(a,n):
#       currentMax = a[0]
#       for i in range(1,n):
#           if a[i] > currentMax:
#           currentMax = a[i]
#       return currentMax
#
# Determine the number of times that the statement “currentMax = a[i]” will be
# executed in the best case and in the worst case.

# Best case scenario would be that the maximum is at the start of the array.
# "currentMax = a[i]" would run 0 times.
# Worst case scenario would be that the maximum is at the end of the array.
# "currentMax = a[i]" would run n-1 times.
