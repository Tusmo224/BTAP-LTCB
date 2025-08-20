"""6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If
the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is
less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'"""

ing= input("Enter a string (bt6): ")
if len(ing) < 3:
    print(ing)
if len(ing) >= 3 and ing.endswith("ing") :
    print(ing +"ly")
else:
    print(ing +"ing")
