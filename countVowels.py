#word = input("Please enter a word: ")
#counter = 0

#if word.find('a'):
    #counter += 1
#elif word.find('e'):
    #counter += 1
#elif word.find('i'):
    #counter += 1
#elif word.find('o'):
    #counter += 1
#elif word.find('u'):
    #counter += 1
#print("Your word is ", len(word), "letters long.")
#print ("Your word has", counter, "vowels.")

word = input("Please enter a word: ")
counter = 0
vowels = ['a', 'e' 'i', 'o', 'u']
vcount = 0

while counter < len(word):
    if word[counter] in vowels:
        vcount += 1
    counter += 1
print("Your word has ", vcount, "vowels")