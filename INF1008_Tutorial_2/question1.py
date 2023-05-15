# Write a program that reads in a sequence of characters, and determines whether its
# parentheses, braces, and curly braces are "balanced." Your program should read one
# line of input containing what is supposed to be a properly-formed expression in
# algebra and tells whether it is in fact legal. The expression could have several sets of
# grouping symbols of various kinds, e.g., ( ), [ ] and { }. Your program needs to make
# sure that these grouping symbols match up properly.

expression = list(input("Enter your expression: "))

symbol_array = []  # array for storing all the symbols.
matching_symbols = True  # assume that all the symbols are properly matched.

# add all the symbols to a new array.
for i in range(len(expression)):
    if expression[i] in ["(", ")", "[", "]", "{", "}"]:
        symbol_array.append(expression[i])

x = 0  # let x be 1st symbol.
y = -1  # let y be corresponding bracket (to match with x).

# check whether the opening and closing brackets are the same type.
# by mathematical logic, the outer brackets must always be the same type.
# e.g. {4 + [2 + (1 + 1)]}
# after checking the outer bracket is the same, we can move into the "next outer" bracket.
for i in range(int(len(symbol_array) / 2)):
    if symbol_array[x] == "(" and symbol_array[y] == ")":
        x += 1  # increment x to check "next outer" bracket.
        y -= 1  # decrement y to check corresponding bracket.
    elif symbol_array[x] == "[" and symbol_array[y] == "]":
        x += 1
        y -= 1
    elif symbol_array[x] == "{" and symbol_array[y] == "}":
        x += 1
        y -= 1
    else:
        matching_symbols = False

if not matching_symbols:
    print("The grouping symbols do not match up properly.")
else:
    print("The grouping symbols match up properly.")
