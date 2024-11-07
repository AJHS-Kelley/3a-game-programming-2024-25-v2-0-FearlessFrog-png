# Dragon Realm, <Tegan_Robinson>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

# Global varibales for Items
hasAxe = False
hasSheild = False
hasGraple = False
hasTorch = False

def displayIntro():

    print('You are in a land full of dragons. In front of you,')
    print('you see two caves. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print()

hasironSwword = False
damage = random.randint(1,20)
pickUpItem = input("Your walking along the trail when you see an iron sword on the ground, Do you wish to pick up the sword?, Type yes or no then press enter.\n")
if pickUpItem == "yes":
    hasironSword = True

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which cave will you go into? (1 or 2)')
        cave = input()
    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# Using Booleans for Items
hasSword = False
damage = random.randint(1,20)
pickUpItem = input("You see a iron sword on the ground, Do you pick it up? Type yes or no, then press enter")
if pickUpItem == "yes":
    hasSword = True

if hasSword:
    damage += 20
else:
    damage += 5        