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
  cpuChoice = "scissors"
 elif cpuChoice == 2:
   cpuChoice = "paper"
 else:
   print("Unable to determine CPU choice.\nPlease restart.\n")
   exit()
   return cpuChoice
 
 def pickWinner(playerChoice: str, cpuChoice: str) -> str:
  """Determines the winner using player and cpu choices. """
  if playerChoice == "rock" and cpuChoice == "paper":
# CPU WINS
    print(f"The CPU chose {cpuChoice} adn you chose {playerChoice}.\n")
    print(f"The CPU wins a point.\n")
    cpuScore += 1
    return "CPU WINS"
  elif playerChoice == "rock" and cpuChoice == "scissors":
    # PLAYER WINS
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print(f"You win a point.\n")
    playerScore += 1
    return "Player Wins"
  elif playerChoice == "rock" and cpuChoice == "rock":
    # DRAW
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}")
    print(f"It's a draw\n")
    return "Draw"
  elif playerChoice == "scissors" and cpuChoice == "rock":
    # CPU WINS
    print(f"The CPU chose {playerChoice} and you chose {playerChoice}.\n")
    print(f"You win a point!")
    playerScore += 1
    return "Player Wins"
  elif playerChoice == "scissors" and cpuChoice == "scissors":
    # DRAW
    print(f"The CPU {cpuChoice} and you chose {playerChoice}")
    print(f"It's a draw\n")
    return "Draw"
  elif playerChoice == "paper" and cpuChoice == "rock":
    # PLAYER WINS
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print(f"You win a point.\n")
    playerScore += 1
    return "Player Wins"
  elif playerChoice == "paper" and cpuChoice == "paper":
# DRAW
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print(f"It's a draw!\n")
    return "Draw"
  elif playerChoice == "paper" and cpuChoice == "scissors":
    # CPU WINS
    print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
    print(f"The CPU wins a point.\n")
    cpuScore += 1
    return "CPU Wins"
  else:
    print("Unable to determine a winner. Please restart.\n")
    exit()

def score( winner: str) -> int:
  """This function uses the winner to update the score for CPU, Num. Draws, and player score. """
  if winner == "Player Wins":
   score = 1
  elif winner == "CPU WINS":
   score = 1
  else: # This is a DRAW.
    socre = 0
    return score
  
# MAIN GAME LOOP
  while playerScore <5 and cpuScore < 5:
    print(f"{playerName} you have {playerScore}\n The CPU has {cpuScore} points.\n")



print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore\n}")
 if playerScore > cpuScore
  print(f"Congratulations {playerName}, a winner is you!\n")
  elif cpuScore > playerScore:
  print(f"The CPU wins. You are a dissapoitment to all.\n")
  else:
  print("Unable to determine a winner.\nPlease restart.\n")
  exit()