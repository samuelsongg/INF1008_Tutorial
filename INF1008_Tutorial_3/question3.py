# Check recursively if the following objects are palindromes:
# 1. a word
# 2. a sentence
# Ignore blanks, lower-case and upper-case differences, and punctuation marks so
# that a word or a sentence that reads the same backward as forward.
# (1) “Madam, I’m Adam”
# (2) madam
# (3) nurses run.
# Example: Please enter a sentence: Madam, I'm Adam. Then check if "Madam, I'm
# Adam" is a palindrome. The answer is: True.
import re


def palindrome_checker(x):
    # if string is 1 or 0 characters long, it is considered a palindrome.
    if len(x) <= 1:
        return True

    # remove all characters except for the ones specified, and set string to lowercase.
    x = re.sub('[^A-Za-z0-9]+', '', x).lower()

    if x[0] == x[-1]:
        # calls function again with the prefix and suffix removed.
        return palindrome_checker(x.removesuffix(x[-1]).removeprefix(x[0]))
    else:
        return False


if __name__ == '__main__':
    print(palindrome_checker("nurses run"))