import random

# List of words to choose from
WORDSS = ["python", "hangman", "developer", "programming", "challenge", "computer", "algorithm"]

# Function to choose a random word
def choose_word():
    return random.choice(WORDSS)

# Function to display the word with guessed letters
def display_words(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

# Hangman game function
def play_hangman():
    word = choose_word()
    guessed_letters = set()
    attempts_remaining = 6  # Set the limit of incorrect guesses

    print("Welcome to Hangman!")
    print(display_words(word, guessed_letters))

    while attempts_remaining > 0:
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good job! That letter is in the word.")
        else:
            attempts_remaining -= 1
            print(f"Wrong guess! Attempts remaining: {attempts_remaining}")

        print(display_words(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Game over! The word was '{word}'.")

# Run the game
if __name__ == "__main__":
    play_hangman()
