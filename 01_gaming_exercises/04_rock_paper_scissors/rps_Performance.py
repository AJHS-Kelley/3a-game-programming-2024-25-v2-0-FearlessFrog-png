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
    if playerChoice