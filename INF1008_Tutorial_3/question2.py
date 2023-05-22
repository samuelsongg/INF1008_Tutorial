# Write a recursive function GCD(n, m) that returns the greatest common divisor of two integer n and m.
# Example:
# Enter the first number: 54
# Enter the second number: 24
# The GCD of 54 and 24 is 6

# Euclidian algorithm
def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


if __name__ == '__main__':
    print(gcd(54, 24))