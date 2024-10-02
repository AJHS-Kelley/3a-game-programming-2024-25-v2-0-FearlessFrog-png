# Rock, Paper, Scissors by Tegan Robinson, v0.1

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER 
playerScore = 0
playerName = "Test Player"
playerChoice = None

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name and press enter.\n")
print(f"Hello {playerName}!n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n").lower()

# .lower() can turn all inputs into lowercase.
# .upper() can turn all inputs into UPPERCASE.

if isCorrect == "yes":
  print(f"Ok {playerName}, let's play Rock, Paper, and Scissors.\n")
else:
  playerName = input("Please type your name and press enter,\n")

# THE RULES using MULTI-LINE STRINGS
print(f"""
Welcome, {playerName} to the Rock, Paper, and Scissors Robot!
It's time to play Rock, Paper, Scissors!

You will be playing against the CPU. The first player to score 5 poitns wins.
You will select from ROCK, PAPER, and SCISSORS.
THE CPU will select ROCK, PAPER AND SCISSORS at random.

1) ROCK BEATS SCISSORS
2) Scissors BEATS PAPER
3) PAPER BEATS ROCK
""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS.
''''''
Anything in between the sets of double quotesis just ignored.
If you need to write large comments, it's easier to use multi-line strings then
putting a # in front of 15 differnet lines.
""""""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
  print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
  playerChoice = input("Please enter a rock, paper and scissors and press enter.\n"). lower()
  if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
    playerChoice = input("Please enter rock, paper, or scissors and press enter.\n"). lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        print("You are not following directions. Please try again.\n")
        exit()
        print(f"You have choosen{playerchoice}.\n")
    else:
      print(f"You have choosen {playerName}.\n")

# let cpu select choice at random
cpuChoice = random.randiant(0,2) # randonly slect 0, 1, or 2
if cpuChoice == 0:
    cpuChoice = "rock"
elif cpuChoice == 1:
   cpuChoice == "scissors"
elif cpuChoice == 2:
   cpuChoice = "paper"
else:
  print("Unable to determine CPU choice.\nPlease restart.\n")
  exit()
# print(f"CPU choice: {cpuChoice}")

# compare player choice to cpu choice
if playerChoice == "rock" and cpuChoice == "paper"
  # CPU WINS
  print(f"The CPU choose {cpuChoice} adn you choose {playerChoice}.\n")
  print(f"The CPU wins a point")
  cpuChoice += 1
elif playerChoice == "rock" and cpuChoice == "scissors":
  # PLAYER WINS
  print(f"The CPU choose {cpuChoice} and you choose {playerChoice}.\n")
  print(f"You win a point")
  playerScore += 1
elif playerChoice == "rock" and cpuChoice == "rock":
  # DRAW
   print(f"The CPU chose {cpuChoice} and you choose {playerChoice}.\n")
   print(f"It's a draw.\n")
elif playerChoice == "scissors" and cpuChoice == "rock":
  # CPU WINS
   print(f"The CPU choose {cpuChoice} and you choose {playerChoice}.\n")
   print(f"The CPU wins a point")
   cpuScore += 1
elif playerChoice == "scissors" and cpuChoice == "paper":
# PLAYER WINS
   print(f"The CPU choose {cpuChoice} and you choose {playerChoice}.\n")
   print(f"You win a point.\n")
   playerScore += 1
elif playerChoice == "scissors" and cpuChoice == "scissors":
  # DRAW
  print(f"The CPU choose {cpuChoice} and you choose {playerChoice}.\n")
  print("It's a draw!".\n")
elif playerChoice == "paper" and cpuChoice == "rock"
  # PLAYER WINS        
  print(f"The CPU choose {cpuChoice} and you choose {playerChoice}.\n")
  print("You win a point".\n")
        playerScore += 1
elif playerChoice == "paper" and cpuChoice == "paper"
  # DRAW
  print(f"The CPU choose {cpuChoice} and the player choose {playerChoice}.\n")
  print("It's a draw".\n")
elif playerChoice == "paper" and cpuChoice == "scissors":
  # CPU WINS
  print(f"The CPU choose {cpuChoice} and you choose {playerChoice}.\n")
  print("The CPU wins a point.\n")
      cpuChoice += 1
  else:
  print("Unable to determine a winner. Please restart")
      exit()


print(f"Your Final Score: {playerScore}\nCPU Final Score: {cpuScore}\n")
if playerScore > cpuScore:
  print(f"Congratulations {playername}, a winner is you!".\n")
  elif cpuScore > playerScore:
  print(f"The CPU wins. You are a dissapoitment to all.\n")
  else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()