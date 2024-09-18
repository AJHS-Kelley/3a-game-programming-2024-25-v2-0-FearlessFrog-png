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
     print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points .\n")
    playerChoice = input("Please enter rock, paper or siccors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        playerChoice = input("Please ebter rock, paper, or scissors and press enter.\n").lower()
        if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        print("You are bit following directions, Please try again.\n")
        exit()
    else:
      print(f"You have chosen {playerChoice}.\n")




    # let the cpu select choice at random.
    # compare player choice to cpu choice.
    # print the results to the screen.
    # award points to the winner and output results.