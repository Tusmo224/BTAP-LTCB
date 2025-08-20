"""5. Write a Python program to get a single string from two given strings, separated by a space and
swap the first two characters of each string.
Sample String : 'abc', 'xyz'
Expected Result : 'xyc abz"""

c1= input("Enter first string: ")
c2= input("Enter second string: ")
c3= c1[0:2] +c2[2:]
c4= c2[0:2] +c1[2:]
print( c4 +" " + c3)
