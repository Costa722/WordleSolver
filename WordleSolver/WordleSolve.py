potentialWords = []

with open("wordleDictionary.txt") as file:
    potentialWords = file.readlines()

def play(potentialWords : list) -> None:
    while len(potentialWords) > 1:
        lettersInWord = []
        for position in range(5):
            letter = input("What letter is in position " + str(position + 1) + "?: ").lower()
            color = input("What color is the word in position " + str(position + 1) + ", (g, y, b)?: ").lower()
            print("\n")
            if color != 'g' and color != 'y' and color != 'b':
                print("Invalid input")
                return
            words_to_remove = []
            for word in potentialWords:

                # if color is in the right spot
                if color == 'g':
                    if word[position] != letter:
                        words_to_remove.append(word)
                    if letter not in lettersInWord:
                        lettersInWord.append(letter)

                # if letter in word but not right spot
                elif color == 'y':
                    if word[position] == letter:
                        words_to_remove.append(word)
                    elif letter not in word:
                        words_to_remove.append(word)
                    if letter not in lettersInWord:
                        lettersInWord.append(letter)

                #if letter not in the word
                elif color == 'b':
                    if letter in word:
                        if letter not in lettersInWord:
                            words_to_remove.append(word)
                        elif word[position] == letter:
                            words_to_remove.append(word)
            
            

            # removing words from total words
            for word in words_to_remove:
                potentialWords.remove(word)

        print(*potentialWords)
        guess = input("Did you guess correctly (y/n)?: ").lower()
        if guess == 'y':
            print("YOU WIN!!!")
            return
    
play(potentialWords)
    
