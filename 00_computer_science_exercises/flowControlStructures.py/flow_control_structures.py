# Flow Control Structures, Tegan Robinson, v0.0
# Making Computer Programs Make Decisions

temperature = 78.96
color = "Purple"
height = 6
likesPineappleOnPizza = True

# SINGLE DECISION POINT - if Statment
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARISON OPERATOR 99% of the time
    # run this code IF the CONDITIONAL_EXPRESSION IS TRUE

if temperature > 100:
    print ("It is hot as the sun outside.\n")

if height < 8:
    print ("No thanks, I have a Girlfriend.\n")

#CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS
if likesPineappleOnPizza:
    print("Yummy")

# What if we want something different to happen?
if color == "Purple": # COMMON ERROR FOR STUDENTS IS USING = instead of ==
    print("Your shirt is the correct uniform color.\n")
else:   
    print("Your shirt is not the correct uniform color.\n")

# AMUSEMENT PARK HEIGHT CHECKER EXAMPLE
# Must be > min. height and < max. height to ride   

if height >= 3:
    print("You're tall enought to ride the Ferris Wheel!\n")
elif height >= 6:
    print("You're too tall to ride the Farris Wheel\n")
else: # "oh, no , something's wrong"
    print("Error, height not detected. Do not ride.\n")



# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height >= 3:
    print("You're not tall enough to ride.\n")
elif height < 6:
    print("You're tall enough to ride.\n")
else: # "oh, no, somethings wrong!"
    print("Error, height not detected. Do not ride.\n")

# Create an if-elif-else block that cheks the temperature.
# If the temperature is not at least 100, print that it's too hot outside.
# If the temperature is at least 50 degrees but less than 100, 
# If the temperature is less thatn 50 degreees but greater than 0, 
# If no temperature is detected, print an error message.
temperature = 99
if temperature >= 100:
    print("It's too hot, students cannot go to recess.\n")
elif temperature >= 50:
    print("Recess it allowed today.\n")
elif temperature >= 0:
    print("Recess is allowed today.\n")
elif temperature > 0:
    print("Recess will be in the gym.\n")
else:
    print("Error detecting temperature.\n")