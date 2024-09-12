# Awarding Extra Lives, Tegan Robinson, v0.0


lives = 3
score = 25000
name = "Tegan"





# CHARACTER REFEREENCE
# CURLY BRACES {}
# BRACKETS []
# ANGLE-BRACKETS <>
# PARENTHESES ()

# Allow the user to input the score AS AN INTEGER.

# If score is 10000 or less
    # Lose a life
# If score is > 10000 but less than 100001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives

# Output the score and number of lives to the screen.
score = int(input("Please display your score")) # This is where the user types in their score

if score <= 10000:
    lives -= 1 # Lose a life
elif score < 1000001: 
    lives += 1 # Gain a lifes
elif score > 100000:
    lives += 2  # Gain 2 lifes


print(F"This is your current score {score} This is your current amount of lives {lives}") # This message displays your current score and your current amount of lives