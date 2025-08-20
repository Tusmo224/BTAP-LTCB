myString = input("Enter your string")
newString = ""
for i in range(len(myString)):
    if (i % 2 == 0):
        newString += myString[i]
print(newString)