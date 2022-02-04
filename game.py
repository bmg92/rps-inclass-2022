# this is the "game.py" file...

import os

player_name = os.getenv("PLAYER_NAME", default="Player One")

# ...

print("Rock, Paper, Scissors, Shoot!")
print("Welcome " +player_name +" to this game of Rock-Paper-Scissors. Let's go")


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


# ASK FOR USER INPUT
userInput = input("Please enter your selection: 'rock', 'paper', 'scissors'").lower()

#the above .lower() function serves as part of the data validation as the below if statement only evaluates lowercase words
#VALIDATIONS
print("USER CHOSE:", userInput)

if userInput != "rock" and userInput != "paper" and userInput != "scissors":
    print("Unfortuantely your input is not an acceptable option for this game. Please check your input's spelling ensuring it corresponds to one of the aforementioned options and run the program again.")
    exit()
    
# COMPUTER CHOICE
import random # this is necessary to avoid a NameError when using the randint function below
computerChoice = ["rock", "paper", "scissors"]
computerChoice = random.choice(computerChoice)
print("The computer selected", computerChoice)

# DETERMINE THE WINNER

result = None
if userInput == computerChoice:
    result = "It's a tie"
elif userInput == "rock" and computerChoice == 'scissors':
    result = "You beat me"
elif userInput == "scissors" and computerChoice == 'rock':
    result = "I beat you"
elif userInput == "rock" and computerChoice == 'paper':
    result = "I beat you"
elif userInput == "paper" and computerChoice == 'rock':
    result = "You beat me"
elif userInput == "paper" and computerChoice == 'scissors':
    result = "I beat you"
elif userInput == "scissors" and computerChoice == 'paper':
    result = "You beat me"

# FINAL RESULTS
print(result)
print("Good game - thanks for playing.")