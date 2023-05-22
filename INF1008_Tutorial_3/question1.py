# Write a recursive function to add the first n terms of the series: 1 + 1/2 - 1/3 + 1/4 -1/5 ...
# Keep the answer to four decimal places.
# Example: Enter the number of terms to sum: 5 Sum of first 5 terms = 1.2167

def series_add(n):
    if n > 0:
        if n % 2 == 0 or n == 1:  # if index 0 or denominator is even, add to total result
            result = (1 / n) + series_add(n - 1)
        else:  # if denominator is odd, subtract from total result
            result = -(1 / n) + series_add(n - 1)
    else:
        result = 0
    return result.__round__(4)  # round results to 4 decimal place


if __name__ == '__main__':
    print(series_add(5))
