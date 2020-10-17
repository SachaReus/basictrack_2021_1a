def remove(substring, word):
    return word.replace(substring, "", 1)


print(remove("an", "banana"))
