def first_three(string):
    if (len(string) < 3):
        return string
    return string[:3]


myString = input("Enter your string: ")
print(first_three(myString))