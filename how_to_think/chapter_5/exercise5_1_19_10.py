# palindrome implicates word is reversed the same

def reverse_word(x):
    return x[::-1]


def is_palindrome():
    return word == reverse_word()


word = reverse_word(input("please give me a word"))

print(is_palindrome)
