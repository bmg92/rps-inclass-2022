# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT
userInput = input("Please enter your selection: 'rock', 'paper', 'scissors'").lower()


#VALIDATIONS
print("USER CHOSE:", userInput)

if userInput != "rock" and userInput != "paper" and userInput != "scissors":
    print("Unfortuantely your input is not an acceptable option for this game. Please check your input's spelling ensuring it corresponds to one of the aforementioned options and run the program again.")
    exit()
    
# COMPUTER CHOICE
import random # this is necessary to avoid a NameError when using the randint function below
computerChoice = ["rock", "paper", "scissors"]
print("The computer selected", random.choice(computerChoice))

# DETERMINE THE WINNER

# FINAL RESULTS