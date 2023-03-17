# Guess-the-number
Guessing a random generated number


The program generates a random number between 0 and 9 using the randrange function from the random module.

The program prints the random number to the console.

The program initializes the count variable to 3, which represents the number of attempts the user has left to guess the number.

The program enters a while loop that will repeat until either the user correctly guesses the number or the user runs out of attempts.

Within the while loop, the program prints the number of attempts the user has left.

The program prompts the user to enter a number using the input function and converts the input to a integer using the int function.

The program checks whether the user's guess matches the random number. If so, it prints a message indicating that the user has correctly guessed the number and exits the while loop.

If the user's guess is not correct, the program provides feedback to the user by indicating whether the number is higher or lower than their guess.

The program decrements the count variable by 1.

If the count variable is equal to 0, the program exits the while loop and prints a message indicating that the user has run out of attempts.

If the count variable is not equal to 0, the program continues to the next iteration of the while loop to allow the user to guess again.

Once the while loop is complete, the program exits.
