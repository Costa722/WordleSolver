import os

# List that contains the words that may be the solution
potentialWords = []

# Opens the dictionary to populate the potential word list
with open("wordleDictionary.txt") as file:
    potentialWords = file.readlines()

# Function for finding the solution for wordle
def play(potentialWords : list) -> None:
    # Loop to go through each word guess until there are none left
    while len(potentialWords) > 1:
        # list to hold the letters that are in the word for the day
        lettersInWord = []
        for position in range(5):
            # gathers the letter in the position and the color
            letter = input("What letter is in position " + str(position + 1) + "?: ").lower()
            color = input("What color is the word in position " + str(position + 1) + ", (g, y, b)?: ").lower()
            print("\n")
            # if the input is wrong then return
            if color != 'g' and color != 'y' and color != 'b':
                print("Invalid input")
                return
            # list for the words that do not match the pattern
            words_to_remove = []
            # interates through all potential words taking account for color and position
            for word in potentialWords:

                # if color is in the right spot
                if color == 'g':
                    # if the letter is right but current word doesnt match remove word
                    if word[position] != letter:
                        words_to_remove.append(word)
                    # add letter to letters in word if not already in it
                    if letter not in lettersInWord:
                        lettersInWord.append(letter)

                # if letter in word but not right spot
                elif color == 'y':
                    # if the letter is in the current position in the word then remove
                    if word[position] == letter:
                        words_to_remove.append(word)
                    # if the letter is not in the current word then remove
                    elif letter not in word:
                        words_to_remove.append(word)
                    # if letter is not in letter list then add
                    if letter not in lettersInWord:
                        lettersInWord.append(letter)

                #if letter not in the word
                elif color == 'b':
                    # if the letter is in the word then remove word
                    if letter in word:
                        #if letter is not in the word letters then remove the word
                        if letter not in lettersInWord:
                            words_to_remove.append(word)
                        # if the letter is in word at current position then remove
                        elif word[position] == letter:
                            words_to_remove.append(word)
            
            

            # removing words from total words
            for word in words_to_remove:
                potentialWords.remove(word)

        # prints the potential words, each on own line
        print(*potentialWords)
        # ask if word was right if not then iterate through loop again
        guess = input("Did you guess correctly (y/n)?: ").lower()
        os.system('cls')
        # if word is right then game is over after message.
        if guess == 'y':
            print("YOU WIN!!!")
            return
# Call to the function to play the game
play(potentialWords)
    
