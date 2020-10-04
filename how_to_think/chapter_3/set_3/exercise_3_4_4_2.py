numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_even_numbers = 0
for number in numbers:
    if number % 2 == 0:
        sum_even_numbers += int(number)

print("The sum of all the even numbers is", sum_even_numbers)
