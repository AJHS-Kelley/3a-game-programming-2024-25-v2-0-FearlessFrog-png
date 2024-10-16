# Rock, Paper, Scissors by Ryan Kelley, v3.0

# MODULE IMPORTS
import random

#DATA STRUCTURES
player_name = "test player"
player_score = 0
player_choice = None

      
# PlAYER NAME IMPUT
def playerName() -> str:# Function Signature -- name of function, (arguments if any)
  """Gets the name form the player and returns it. """
  # The line is a DOCSTRING, it gives a breif example of what the function does.
  playerName = input("Please type your name here and press enter.\n")
  print(f"Hello{playerName}!\n")
  isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()
if isCorrect == "yes":
  print(f"okay{player_choice}, let's play Rock, Paper, Scissors")
else:
  player = input("Please type your name and press enter.\n")
  return playerName

 # CALLING THE FUNCTION
player_name = playerName()

# THE RULES using MULTI-LINE STRINGS
def rules() -> None:
 """This function prints the rules for rock, paper, scissors. """  
print(f"""
Welcome. {playerName} to the Rock, Paper, Scissors Robot!
It's time to play Rock, Paper, and Scissors!

You will play against the CPU. The first player to score 5 points wins.
You will pick from ROCK, PAPER, and Scissors.
The CPU will select Rock, Paper, and Scissors at random.

1) ROCK OBLITERATES SCISSORS
2) SCISSORS SLICES PAPER
3) PAPER KIDNAPS ROCk
""")
# Does another part of this program need to access this information?
# IF YES, YOU MUST HAVE A return STATEMENT
# IF NO, A return STATEMENT IS NOT REQUIRED

def playerChoice() -> str:
 """Allows the CPU to choose rock, paper scissors. """
 cpuChoice = random.randint(0,2)# randomly select 0, 1, or 2.
 if cpuChoice == 0:
   cpuChoice = "rock"
 elif cpuChoice == 1:
   cpuChoice = "paper"
 elif cpuChoice == 2:
   cpuChoice = "scissors"
 elif cpuChoice == 3: