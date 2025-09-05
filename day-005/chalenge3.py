# Work out the total of the numbers between 1 and 100, inclusive of both 1 and 100.

print(range(1, 10))  # Doesn't do anything

for number in range(1, 10):  # Prints 1 to 9
    print(number)

for number in range(1, 11):  # Prints 1 to 10
    print(number)


# Gauss challenge
total = 0
for number in range(1, 101):
    total += number
print(total)
