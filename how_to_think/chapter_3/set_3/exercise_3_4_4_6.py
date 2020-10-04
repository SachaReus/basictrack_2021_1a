names = ["liam", "noah", "oliver", "sam", "james"]

number_of_names = 0
for name in names:
    if name == "sam":
        break
    number_of_names += 1

print("There are", number_of_names, " names in the list until the first occurence of the word sam")


