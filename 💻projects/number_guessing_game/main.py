import random # Import the random module to generate random numbers

# Print a welcome message and game instructions to the user
print("Welcome to the Number Guessing Game!") # Greet the player and introduce the game
print("Guess a number between 50 and 100.") # Explain the range of numbers to guess from
print("You have 5 attempts.") # Tell the player the number of attempts they have
print("Let's start!") # Encourage the player to start the game

# Generate a random number between 50 and 100 (inclusive) for the user to guess
number_to_guess = random.randrange(50, 101) # The upper bound in randrange is exclusive, so we use 101 to include 100

max_attempts = 5 # Set the maximum number of attempts the user has

attempts_taken = 0 # Initialize a counter to keep track of the number of guesses made

# Start a loop that continues as long as the user has attempts left
while attempts_taken < max_attempts:
    
    attempts_taken += 1 # Increment the guess counter for each attempt
    user_guess = int(input("Please enter your guess: ")) # Prompt the user to enter their guess and convert it to an integer

    # Check if the user's guess matches the number to guess
    if user_guess == number_to_guess:
        print(
            f"The number is {number_to_guess} and you found it right!! in the {attempts_taken} attempt"
        ) # Congratulate the user if they guess correctly and show the number of attempts taken
        break # Exit the loop if the guess is correct

    # Check if the user has run out of attempts and still hasn't guessed correctly
    elif attempts_taken >= max_attempts and user_guess != number_to_guess:
        print(f"Oops sorry, the number is {number_to_guess} better luck next time!") # Inform the user they've run out of attempts and reveal the number

    # Provide hints to the user to guess higher or lower in the next attempt
    elif user_guess > number_to_guess:
        print("your guess is very high, try again!") # Tell the user their guess is too high

    elif user_guess < number_to_guess:
        print("your guess is very low, try again!") # Tell the user their guess is too low

