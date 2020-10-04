numbers = [1, 3, 4, 5, 6, 7, 8, 9, 10]


sum_of_numbers = 0  # excluding the first even number
for number in numbers:
    if number % 2 == 0:
        break
    sum_of_numbers += number

print("The sum of numbers up till the first even number is", sum_of_numbers)


