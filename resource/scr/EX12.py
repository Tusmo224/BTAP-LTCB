myString = input("Enter your string: ")
wordList = myString.split(" ")
wordFreq = {}
for word in wordList:
    wordFreq[word] = wordFreq.get(word, 0) + 1
print("The occurrence of each word in your string:", wordFreq)