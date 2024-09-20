# THE RULES using MULTI_LINE STRINGS
print(""""
Welcome,{Tegan Robinson} to the Rock, Paper, Scissors Robot!      
It's time to Play Rock, Paper, Scissors!
      
You will be going up against the CPU. The first player to score 5 points wins.
You can select from ROCK, PAPER and SCIRRORS.
The CPU will select ROCK, PAPER or Scissors at random.

1) PAPER BEATS ROCK
2) SCISSORS BEAT PAPER
3) ROCK BEATS SCISSORS                                    
""")

# MULTI_LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything is between the sets of double-quotes is just ignored
If you need to write large comments, it's easier to us multi-line strings than putting a # in front of 15 different lines
"""

# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
  print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
  playerChoice = input("Please enter rock, paper or siccors and press enter.\n").lower()
  if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
     playerChoice = input("Please enter rock, paper, or scissors and press enter.\n").lower()
     playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
  print("You are bit following directions, Please try again.\n")
exit() 
else:
print(f"You have chosen {playerChoice}.\n")
else:
print(f"You have chosen {playerChoice}.\n")




  # let the cpu select choice at random.
  cpuChoice = random.randint(0,2) # randomly select 0, 1 , or 2.
  if cupChoice == 0:
    cpuChoice = "rock"
  elif cpuChoice == 1:
  cupChoice = "scissors"
  elif cpuChoice == 2:
    cpuChoice = "paper"
  else:
    print("Unable to determine CPU choice.\nPlease restart.\n ")
    exit()
# print(f"CPU Choice: (cpuChoice)"")

# compare player choice to cpu choice
if playerChoice == 'rock' and cpuChoice == "paper":
    print("The CPU choose(cpuChoice) and you choose (playerChoice)")
    print("The CPU wins a point.\n")
    cpuScore += 1
  elif playerChoice ==  "rock" and cpuChoice = "scissors":
    # PLAYER WINS
    print(f"The Cpu chose {cpuChoice} and you choose {playerChoice}.\n")
  print("You win a point.\n")
    playerScore += 1
  elif playerChoice == "rock" and cpuChoice == "rock":
    # DRAW
    print(f"The Cpu choose {cpuChoice} and you choose {playerChoice}")
    print("It's a draw!\n.")
  elif playerChoice == "scissors" and cpuChoice == "rock":
  # CPU WINS
    print(f"THE CPU choise {cpuChoice} and you choose {playerchoice}.\n")
    print('The Cpu wins a point')
  cpuScore += 1
  elif playerChoice == "scissors" and the cpuChoice = "paper":
    # PLAYER WINS
  print(f"The Cpu chose {cpuChoise} and you choose {playerChoice}.\n")
  print("You win a point.\n")
  playerScore += 1 
  elif playerScore == "scissors" and cpuChoice 