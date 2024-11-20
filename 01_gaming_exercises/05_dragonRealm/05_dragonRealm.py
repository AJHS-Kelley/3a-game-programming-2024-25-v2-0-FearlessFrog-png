# Dragon Realm, <Tegan_Robinson>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time
import datetime

# SAVING DATA TO A FILE
# STEP 1 -- Create the file name to use.
logFileName = "dragonRealmLog.txt"
# logFileName = "dragonRealmLog.txt"
# Examples: dragonRealmLog1132Am.txt

# STEP 2 -- Crate / Open the file to save the data.
saveData = open(logFileName, "a")
#FILE MODES
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE.
# "w" CREATES FILE, IF FILE EXISTS, ERASE AND OVERRIDE FILE CONTENTS.
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED" + " " +str(datetime.datetime.now()) + "\n")

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
    # FIX THE SECOND VILLAGE CODE.  
    if chosenVillage == str(destroyedVillage):
        print('You respond to him saying "W-what was the name of the dragon?')
    else:
        print('The man reponds looks at you with a look of fear as he says the dragons name, Rhaegal, Press y or n to accept the offer')
        




playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    # ITEM SELECTION
    print("You begin to prepare for you quest, you realize you need items that will be crucial in defeating the dragon\n")
    print("You check your inventory, you have: a clean glass bottle , an iron sword, a shield, bandages, and a torch\n")
    # You need to tell the playe what NUMBER represents each ITEM. 
    time.sleep(4)
    numItems = 0
    while numItems < 2:
        selectedItem = int(input("Pick your item wisley, which 2 items wil you take?"))
        if selectedItem == 1:
            hasbottle = True
        elif selectedItem == 2:
            hasIronSword = True
        elif selectedItem == 3:
            hasShield = True
        elif selectedItem == 4:
            hasBandages = True
        elif selectedItem == 5:
            hastorch = True   
    villageNumber = chooseVillage()
    checkVillage(villageNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()

     

    





# CLOSE THE FILE
saveData.close("END OF GAME LOG\n\n")
saveData.close()








