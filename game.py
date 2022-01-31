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
computerChoice = random.choice(computerChoice)
print("The computer selected", computerChoice)

# DETERMINE THE WINNER

result = "currentlyNull"
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