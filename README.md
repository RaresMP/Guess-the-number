# Guess-the-number

Number Guessing Game
A simple number guessing game that generates a random number between 0 and 9 and allows the user to guess the number. The user has 3 attempts to guess the number correctly. If the user guesses the number correctly, the program prints a message indicating that the user has won. If the user runs out of attempts, the program prints a message indicating that the user has lost.

How to use
Clone or download this repository.
Open a terminal window in the repository's directory.
Run the following command to start the game:
python number_guessing_game.py

How it works
The game works by first generating a random number between 0 and 9 using the randrange function from the random module. The program then prints the random number to the console.

The program then initializes the count variable to 3, which represents the number of attempts the user has left to guess the number.

The program then enters a while loop that will repeat until either the user correctly guesses the number or the user runs out of attempts.

Within the while loop, the program prints the number of attempts the user has left.

The program then prompts the user to enter a number using the input function and converts the input to a integer using the int function.

The program then checks whether the user's guess matches the random number. If so, it prints a message indicating that the user has correctly guessed the number and exits the while loop.

If the user's guess is not correct, the program provides feedback to the user by indicating whether the number is higher or lower than their guess.

The program then decrements the count variable by 1.

If the count variable is equal to 0, the program exits the while loop and prints a message indicating that the user has run out of attempts.

If the count variable is not equal to 0, the program continues to the next iteration of the while loop to allow the user to guess again.

Once the while loop is complete, the program exits.


