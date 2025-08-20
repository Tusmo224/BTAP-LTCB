def count_repeated_chars(s):
    mp = {}
    for c in s:
        if c in mp:
            mp[c] += 1
        else:
            mp[c] = 1;
    for c in mp:
        print(f"{c} {mp[c]}")


my_string = input("Enter your string: ")
count_repeated_chars(my_string)