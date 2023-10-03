word = input("Please enter a word: ")
counter = 0
print(len(word))
if word.find('a'):
    counter += 1
elif word.find('e'):
    counter += 1
elif word.find('i'):
    counter += 1
elif word.find('o'):
    counter += 1
elif word.find('u'):
    counter += 1
print ("Your word has", counter, "vowels")