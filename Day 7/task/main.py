import random, hangman_words, hangman_art

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
word_list = hangman_words.word_list
print(word_list)
lives = 6
stages = hangman_art.stages
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(f"{hangman_art.logo}\n")
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
letters_entered = []
while not game_over:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    if len(letters_entered) > 0:
        letters_entered.sort()
        print(f"Letter's entered are: {letters_entered}")
    guess = input("Guess a letter: ").lower()


    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.


    if guess in letters_entered:
        print(f"You already used {guess}!")
    else:
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        #  e.g. You guessed d, that's not in the word. You lose a life.

        if guess not in chosen_word:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1

            if lives == 0:
                game_over = True

                # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
                print(f"***********************YOU LOSE**********************")
                print(f"The word was {chosen_word}")

        if "_" not in display:
            game_over = True
            print("****************************YOU WIN****************************")

    # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
    print(stages[lives])
    if guess not in letters_entered:
        letters_entered.append(guess)
