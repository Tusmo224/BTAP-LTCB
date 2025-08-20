def inset_sting_middle(string1, string2):
    return string1[:len(string1)//2] + string2 + string1[len(string1)//2:]


myString1 = input("Enter your first string: ")
myString2 = input("Enter your second string: ")
print("Insert the second string into the middle of the first string: ", inset_sting_middle(myString1, myString2))