import random

# Library that we use to choose random words from a list
name = input("What is your name? ")
print("Good Luck!", name)

# List of words for the game
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function to choose a random word from the list
word = random.choice(words)

print("Guess the characters")

# Initialize guesses to an empty string
guesses = ''

# Number of turns the player gets
turns = 12

# Main game loop
while turns > 0:

    # Count the number of times a user fails
    failed = 0

    # Loop through each character in the randomly chosen word
    for char in word:

        # If the character has been guessed correctly, display it
        if char in guesses:
            print(char, end=" ")
        else:
            # If the character has not been guessed, display a blank space
            print("_", end=" ")
            failed += 1  # Increment failure count

    # If there are no failed attempts, the user has guessed the word correctly
    if failed == 0:
        print("\nYou Win")
        print("The word is:", word)
        break  # Exit the loop since the user has won

    # Ask the user to guess a character
    print()
    guess = input("Guess a character: ")

    # Add the guessed character to guesses
    guesses += guess

    # Check if the guessed character is not in the word
    if guess not in word:
        turns -= 1  # Reduce the number of turns

        # Inform the user of the wrong guess
        print("Wrong guess")

        # Inform the user how many guesses are left
        print("You have", turns, 'more guesses')

        # If the user runs out of turns, they lose
        if turns == 0:
            print("You Lose. The word was:", word)
