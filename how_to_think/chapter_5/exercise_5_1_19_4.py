def count_letters(word, letter):
    count = 0
    first_occurrence = word.find(letter)
    while first_occurrence >= 0:
        first_occurrence = word.find(letter, first_occurrence +1)
        count += 1
    return count


print(count_letters("banana", "a"))
