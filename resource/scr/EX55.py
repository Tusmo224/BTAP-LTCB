def first_repeated_word(s):
    words = s.split(" ")
    words_dict = {}
    for w in words:
        if w not in words_dict:
            words_dict[w] = 1
        else:
            words_dict[w] += 1

    for w in words:
        if words_dict[w] == 2:
            return w

    return None


my_string = input("Enter your string: ")
print(first_repeated_word(my_string))