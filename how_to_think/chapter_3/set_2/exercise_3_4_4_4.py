numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# each number on a new line
for number in range(len(numbers)):
    print("the number is", numbers[number])

# each number and its square
for number in range(len(numbers)):
    print("the number is", numbers[number], "and the square is", numbers[number] ** 2)

# total variable
total = sum(numbers)
print("the total of the numbers is", total)

# product of the list
import math

product = math.prod(numbers)
print("the product of the list is", product)
