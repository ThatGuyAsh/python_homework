# Task 4

def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        display_word = ""

        for character in secret_word:
            if character in guesses:
                display_word += character
            else:
                display_word += "_"

        print(display_word)

        return all(character in guesses for character in secret_word)

    return hangman_closure


# Main program

secret_word = input("Enter the secret word: ")

hangman = make_hangman(secret_word)

guessed = False

while not guessed:
    letter = input("Guess a letter: ")
    guessed = hangman(letter)

print("You guessed the word!")