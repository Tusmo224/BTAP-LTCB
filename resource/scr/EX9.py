myString = input("Enter your string:")
if (len(myString) != 0):
    n = int(input("Enter the index you want to remove:"))
    myString = myString[0:n] + myString[n + 1:]
    print(myString)
else:
    print("The string is empty!")