# Dragon Realm, <Tegan_Robinson>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You awake to find yourself in a fantasy world. While you explore your surroundings,')
    print('you see two villages. In the first village, everything seems to be attacked or destroyed')
    print('and everyone is in dismay. In the second village,')
    print('everyone is happy, partying, drinking and seem to be unaware to the destruction. Which one will you choose?')
    print()

def chooseVillage():
    village = ''
    while village != '1' and village != '2':
        print('Which village will you enter? (1 or 2)') # PROVIDE A DESCRIPTION OF CHOICES #1 and #2.  
        village = input()
    return village

def checkVillage(chosenVillage):
    print('You approach the first village...')
    time.sleep(2)
    print('The residents seem to be distraught...')
    time.sleep(2)
    print('A man comes up to you with the look of fear in his eyes, he grabs you and says "The village has been atacked by a dragon!"...')
    print()
    time.sleep(2)

    destroyedVillage = random.randint(1, 2)

    if chosenVillage == str(destroyedVillage):
        print('You respond to him saying "W-what was the name of the dragon?')
    else:
        print('The man reponds looks at you with a look of fear as he says the dragons name, Rhaegal')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    villageNumber = chooseVillage()
    checkVillage(villageNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()


