import os

# Variables
potentialWords = []
letter = 'a'
position = 1
wordList = []

#Dictionary
with open("wordleDictionary.txt") as w:
  potentialWords = w.readlines()

# Main Program
while letter != '':
  del wordList[:]

  #1. asking for guess information
  letter = input('What letter do you know: ')
  color = input("What is the color of that letter (y, g, b): ")

  #2. Got a letter in the word
  if color == 'g' or color == 'y':
    position = input('What position is the letter (1-5): ')
    print('\n')
    position = int(position)
    position -= 1

  #3. Add to possible word list
  for word in potentialWords:
    # Green letter
    if color == 'g':
      if word[position] == letter:
        wordList.append(word)

    #Yellow letter
    if color == 'y':
      if letter in word:
        if word[position] != letter:
          wordList.append(word)

    #Black letter
    if color == 'b':
      if letter not in word:
        wordList.append(word)

  #4. Print possible words
  os.system('cls')
  potentialWords = wordList.copy()
  print(*wordList)