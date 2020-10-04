numbers = [1, -2, 3, -4, 5, 6, -7, 8, 9, 10]

sum_negative_numbers = 0
for number in numbers:
    if number < 0:
        sum_negative_numbers += int(number)

print("the sum of the negative numbers is", sum_negative_numbers)
