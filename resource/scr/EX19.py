def last_part_before(string, char):
    string_split = string.split(char)
    return string_split[0]
myString = input("Enter your string: ")


specified_char = input("Enter your specified character to split: ")
print(last_part_before(myString, specified_char))