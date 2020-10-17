def remove_letter(letter, word):
    stripped = ""
    for letter_in_word in word:
        if letter_in_word != letter:
            stripped += letter_in_word
    return stripped


print(remove_letter(input("please give me the letter"), input("please give me the word")))
