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


numItems = 0

def displayIntro():

    print('You awake to find yourself in a fantasy world. While you explore your surroundings,')
    print('You see two villages. In the first village, everything seems to be attacked or destroyed')
    print('and everyone is in dismay. In the second village,')
    print('everyone is happy, partying, drinking and seem to be unaware to the destruction. Which one will you choose?')
    print()

def chooseVillage():
    village = ''
    while village != '1' and village != '2':
        print('Which village will you enter? (1 or 2)')
        village = input()
    return village

def checkVillage(chosenVillage):
    print('You approach the first village...')
    time.sleep(2)
    print('The residents seem to be distraught...')
    time.sleep(2)
    print('A man comes up to you with the look of fear in his eyes, he grabs you and says "The village has been atacked by a dragon!"...')
    time.sleep(2)
    print()
    time.sleep(2)

    destroyedVillage = random.randint(1, 2)
    partyingVillage = random.randint(1,2)
def checkVillage (destroyedVillage):
    print("You approach the second village...")
    time.sleep(2)
    print("The villagers welcome you with open arms, and they point you towards their celebration")
    time.sleep(2)
    print("Your distratced, when you realize a dragon has shown up uninvited")
    time.sleep(2)
    print("The dragon uses his fire to scorch the entire village, including the residents and you")
    print()
    time.sleep(2)
playAgain ='yes'
 

while playAgain == 'yes' or playAgain == 'y':
    # ITEM SELECTION

    displayIntro()
    print("You begin to prepare for you quest, you realize you need items that will be crucial in defeating the dragon\n")
    print("You check your inventory, you have: a clean glass bottle , an iron sword, a shield, bandages, and a torch\n")
    villageNumber = chooseVillage()
    checkVillage(villageNumber)
    numItems = 0
    while numItems < 2:
        selectedItem = input("Pick your item wisley, press 1 for the bottle, 2 for the iron sword, press 3 for the shield, press 4 for the bandages, and press 5 for the torch")
        if selectedItem == '1':
            hasbottle = True
        elif selectedItem == '2':
            hasIronSword = True
        elif selectedItem == '3':
            hasShield = True
        elif selectedItem == '4':
            hasBandages = True
        elif selectedItem == '5':
            hasTorch = True
        numItems += 1    
    print('Do you want to play again? (yes or no)')
    playAgain = input()


    





# CLOSE THE FILE
saveData.close("END OF GAME LOG\n\n")
saveData.close()




