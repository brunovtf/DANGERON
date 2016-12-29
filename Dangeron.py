import random
import sys
import time
from os import system


killCount = 0

def OpeningGame(): # Game opening
    system("title "+"DANGERON THE DUNGEON")
    system("COLOR "+"85")
    frontMessage1 = "\nDANGERON THE DUNGEON - HOW FAR CAN YOU GO?\n"
    for char in frontMessage1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.1)
    playerName = input("Who are you? ")
    time.sleep(1)
    return playerName
playerName = OpeningGame()
system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))


def MonsterCall(): # Summon the enemy and return its HP
    monsters = ["SPIDER", "SKELETON", "SERPENT", "GREAT BULL", "GOBLIN", "ICE GOLEM", "GHOST", "WITCH", "CURSED LION", "FOREST SPIRIT"]
    bosses = ["RED DRAGON", "SOLDIER CYCLOP", "GIANT TROLL", "FLYING ANACONDA", "MINDLESS ASSASSIN", "LION KING", "DEMONIC KNIGHT"]
    legion = monsters + bosses
    
    bossSumm = [] #Create a list from 5 to 5 numbers, that its the killCount to boss fights
    for i in range(5,35,5):
        bossSumm.append(i)
    
    #Code that consider the killCount to choose the monster that the player will fight
    if (str(killCount) in str(bossSumm) and (killCount > 4)):            #Boss fights
        enemy = (random.choice(bosses))
        enemyHP = random.randint((100+killCount*4), (175+killCount*4))
        print ("\n >>> A {} BOSS HAS APPEARED, AND NOW IT'S GOING AFTER YOU! <<<".format(enemy))
        print (" >>> It has {} HP <<<".format(int(enemyHP)))
        return enemy, enemyHP

    elif killCount > 30:                                                #Hardmode fights
        enemy = (random.choice(legion))
        enemyHP = random.randint((75+killCount*8), (150+killCount*8))
        print ("\n >>> THE ELITE {} HAS ARRIVED, AND NOW IT WANTS YOUR BLOOD! <<<".format(enemy))
        print (" >>> It has {} HP <<<".format(int(enemyHP)))
        return enemy, enemyHP

    else:                                                               #Normal fights
        enemy = (random.choice(monsters))
        enemyHP = random.randint((75+killCount), (150+killCount))
        print ("\n >>> {} HAS APPEARED! <<<".format(enemy))
        print (" >>> It has {} HP <<<".format(int(enemyHP)))
        return enemy, enemyHP


def UserUI(): # Game UI, where the player will choose what to do
    global killCount
    global playerName
    playerHP = 100
    potions = 0
    byeMessage = "THANKS FOR PLAYING DANGERON, {}\n".format(playerName)

    while True:
        enemy, enemyHP = MonsterCall()
        while enemyHP > 0:
            #Combat Menu
            print ("-------------------------------------------------------------")
            print ("[MY HP: {}] ------ [{}'S HP: {}]".format(playerHP, enemy, enemyHP))
            print ("[SCORE: {}] -------- [POTIONS: {}]\n".format(killCount, potions))
            print ("1 - ATTACK!    2 - RUN AWAY    3 - HEAL")
            print ("-------------------------------------------------------------")
            playerChoice = str(input("I will(Type the number): "))
            if playerChoice == "1":                                             #Attack
                values = Battle(enemyHP, playerHP, killCount)
                enemyHP += values[0]
                playerHP += values[1]
                if enemyHP < 1:
                    potionsDrop = random.randint(2,5)
                    print ("\nYOU KILLED IT! YOU ALSO EARNED {} HEALING POTIONS\n".format(potionsDrop))
                    print ("\n")
                    print ("\n")
                    potions += potionsDrop
                    killCount += 1
                    if playerHP < 1:
                        system("COLOR "+"48")
                        system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                        print ("YOU WAS KILLED TOO! YOUR SCORE WAS  {} POINTS".format(killCount))
                        for char in byeMessage:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(.2)
                        killCount = 0
                        potions = 0
                        system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                        time.sleep(3)
                        print ("\n")
                        print ("\n")
                        print ("\n")
                        while True:
                            print ("----------------------------------------")
                            print ("1 - Restart            2 - Exit")
                            print ("----------------------------------------")
                            choice = str(input("I will(Type the number): "))
                            if choice == "2":
                                exit()
                            elif choice == "1":
                                playerName = OpeningGame()
                                system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                                GameMenu()
                            else:
                                print ("That's not a valid choice\n")
                                print ("\n")
                                print ("\n")
                elif playerHP < 1:
                    system("COLOR "+"48")
                    print ("YOU WAS KILLED! YOUR SCORE WAS  {} POINTS".format(killCount))
                    for char in byeMessage:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(.2)
                    killCount = 0
                    potions = 0
                    system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                    time.sleep(3)
                    print ("\n")
                    print ("\n")
                    print ("\n")
                    while True:
                        print ("----------------------------------------")
                        print ("1 - Restart            2 - Exit")
                        print ("----------------------------------------")
                        choice = str(input("I will(Type the number): "))
                        if choice == "2":
                            exit()
                        elif choice == "1":
                            playerName = OpeningGame()
                            system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                            GameMenu()
                        else:
                            print ("That's not a valid choice\n")
                            print ("\n")
                            print ("\n")
                system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                time.sleep(.3)
                continue

            elif playerChoice == "2":                                          #Run
                system("COLOR "+"48")
                print(" >> You runned away and lose all your potions/score! <<\n")
                killCount = 0
                potions = 0
                system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                time.sleep(3)
                print ("\n")
                print ("\n")
                print ("\n")
                while True:
                        print ("----------------------------------------")
                        print ("1 - Restart            2 - Exit")
                        print ("----------------------------------------")
                        choice = str(input("I will(Type the number): "))
                        if choice == "2":
                            exit()
                        elif choice == "1":
                            playerName = OpeningGame()
                            system("title "+"DANGERON THE DUNGEON  -  {}  -  {} POINTS".format(playerName,killCount))
                            GameMenu()
                        else:
                            print ("That's not a valid choice\n")
                            print ("\n")
                            print ("\n")

            elif playerChoice == "3":                                          #Heal
                if potions <= 0:
                    print (" >> You got no potions! <<\n")
                    print ("\n")
                    print ("\n")
                    print ("\n")
                else:
                    playerHP += random.randint(25, 50)
                    if playerHP > (playerHP+killCount*2):
                        playerHP = (playerHP+killCount*2)
                    potions -= 1
                    print (" >> You got healed! <<\n")
                    print ("\n")
                    print ("\n")
                    print ("\n")
                    continue

            else:                                                              #Invalid choices
                print (" >> Not a valid choice <<\n")
                print ("\n")
                print ("\n")
                print ("\n")
                continue


def Battle(enemyHP, playerHP, killCount): # Return new playerHP and enemyHP (generate damage)
    minplayerdmg = int(40 +(killCount*2))
    maxplayerdmg = int(70 +(killCount*5))

    minenemydmg = int(10 +(killCount*2))
    maxenemydmg = int(20 +(killCount*3))

    while enemyHP > 0: #change the difficult of the game based on the killCount
        if (killCount <= 10) and (playerHP >= 1):
            playerDmg = random.randint(minplayerdmg, maxplayerdmg)
            print (" >> You caused {} damage to the enemy <<".format(playerDmg))
            enemyHP = -playerDmg

            enemyDmg = random.randint(minenemydmg, maxenemydmg)
            print (" >> suffered {} damage in return <<\n".format(enemyDmg))
            print ("\n")
            print ("\n")
            playerHP = -enemyDmg
            return enemyHP, playerHP

        elif (killCount > 10) and (playerHP >= 1):
            minplayerdmg = int(60 +(killCount*2))
            maxplayerdmg = int(105 +(killCount*5))

            minenemydmg = int(20 +(killCount*2))
            maxenemydmg = int(30 +(killCount*3))

            playerDmg = random.randint(minplayerdmg, maxplayerdmg)
            print (" >> You caused {} damage to the enemy <<".format(playerDmg))
            enemyHP = -playerDmg

            enemyDmg = random.randint(minenemydmg, maxenemydmg)
            print ("  >> You suffered {} damage in return <<\n".format(enemyDmg))
            print ("\n")
            print ("\n")
            playerHP = -enemyDmg
            return enemyHP, playerHP

        else:
            return enemyHP, playerHP


def GameMenu(): # Game menu
    system("COLOR "+"85")
    print ("\n")
    print ("\nWelcome, " + playerName + ".")
    print ("----------------------------------------")
    print ("1 - Play      2 - Credits      3 - Exit")
    print ("----------------------------------------")
    choice = str(input("I will(Type the number): "))
    if choice == "1":
        frontMessage2 = "* You step into the Dungeon, already listening a strange noise...* \n"
        for char in frontMessage2:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.1)
        print (str(playerName) + ": What is this???\n")
        print ("\n")
        time.sleep(2)
        UserUI()

    elif choice == "2":
        print ("The game was fully created by: Bruno V. Freitas\n")
        print ("\n")
        time.sleep(2)
        GameMenu()
    elif choice == "3":
        exit()

    else:
        print ("That's not a valid choice.\n")
        print ("\n")
        time.sleep(2)
        GameMenu()
GameMenu()
