# The program generates a random number between 0 and 9 using the randrange function from the random module.
import random

number = random.randrange(10)
# The program prints the random number to the console.
print("The number from the random choice is", str(number))
# The program initializes the count variable to 3, which represents the number of attempts
# the user has left to guess the number.
count = 3
# The program enters a while loop that will repeat until either the user correctly
# guesses the number or the user runs out of attempts.
while count > 0:
    # Within the while loop, the program prints the number of attempts the user has left.
    print("You have", str(count), "try/ies !")
    try:
        # The program prompts the user to enter a number using the input function
        # and converts the input to a integer using the int function.
        user_number = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input! Please enter a valid number!")
        continue
    # The program checks whether the user's guess matches the random number.
    # If so, it prints a message indicating that the user has correctly guessed the number and exits the while loop.
    if number == user_number:
        print("You've guessed the number!")
        break
    # If the user's guess is not correct, the program provides feedback
    # to the user by indicating whether the number is higher or lower than their guess.
    elif number > user_number:
        print("Try again please! The number is higher than your guess!")
    elif number < user_number:
        print("Try again please! The number is lower than your guess!")
    # The program decrements the count variable by 1.
    count -= 1
# If the count variable is equal to 0, the program exits the while loop and prints
# a message indicating that the user has run out of attempts.
if count == 0:
    print("You're out of tries!")
# If the count variable is not equal to 0, the program continues to the next iteration
# of the while loop to allow the user to guess again.
#
# Once the while loop is complete, the program exits.
