def reverse_word(x):
    return x[::-1]


word_original = input("please give me a word")
word_reversed = reverse_word(word_original)

mirror_word = print(word_original+word_reversed)

# other option
word = input("please give me a word")
mirror_word = word + word[::-1]
print(mirror_word)
