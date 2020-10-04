numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# count how many odd numbers in the list
count_odd_numbers = 0
for number in numbers:
    if number % 2 == 1:
        count_odd_numbers += 1

print("The list contains", count_odd_numbers, "odd numbers")
