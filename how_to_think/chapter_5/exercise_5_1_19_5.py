import string

tog_quote = """You could rattle the start, you could do anything, if only you dared."""


def remove_punctuation(quote):
    quote_sans_punct = ""
    for letter in quote:
        if letter not in string.punctuation:
            quote_sans_punct += letter
    return quote_sans_punct


words = tog_quote.split()


def count_words(quote):
    return len(remove_punctuation(quote).split())


def count_words_containing(quote, letter_to_count):
    count = 0
    for word in remove_punctuation(quote).split():
        if letter_to_count in word:
            count += 1
    return count


no_words = count_words(tog_quote)
letter = "e"
no_words_containing_e = count_words_containing(tog_quote, letter)
percentage = 100 * ( no_words_containing_e/no_words)

print("your text contains {} words, of which {} ({:.1f}%) contain an \"{}\"."
      .format(no_words, no_words_containing_e, percentage, letter))
