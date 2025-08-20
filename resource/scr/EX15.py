def add_tags(tag, s):
    return f"<{tag}>{s}</{tag}>"

myString = input("Enter your string: ")
htmlTag = input("Enter your HTML tag: ")
print(add_tags(htmlTag, myString))