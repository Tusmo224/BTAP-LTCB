def swap_commas_dots(s):
    s = s.replace(",", "#")
    s = s.replace(".", ",")
    s = s.replace("#", ".")
    return s;

my_string = input("Enter your string: ")
print(swap_commas_dots(my_string))