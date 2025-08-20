def ceasar_encryption(plaintext, key):
    key = key % 26
    ciphertext = ""
    for c in plaintext:
        if c.isalpha():
            if c.islower():
                ciphertext += chr((ord(c) - ord('a') + key) % 26 + ord('a'))
            if c.isupper():
                ciphertext += chr((ord(c) - ord('A') + key) % 26 + ord('A'))
        else:
            ciphertext += c
    return  ciphertext

plaintext = input("Enter your plaintext: ")
key = int(input("Enter your key: "))
print(ceasar_encryption(plaintext, key))