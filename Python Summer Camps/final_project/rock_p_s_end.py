from random import randint

def playgame():

    print('')

    playerName = input('what is your name? ')

    welcome(playerName)

    play = "y"

    while play =="y" or play == "Y":

        playerChoice = input("enter a 1 for fire, 2 for ice, 3 for water or x to exit the program ")

        if playerChoice == "1" or playerChoice == "2" or playerChoice == "3":
            ZorChoice = getZorChoice()
            winnerMessage = getWinner(playerChoice, ZorChoice, playerName)
            print(winnerMessage)

        elif playerChoice == "x" or playerChoice == "X":

            print("Goodbye!")
            play = "n"

        else:
            print(playerChoice, " is not a valid choice!")
            print("you must enter 1, 2 or 3 to play the game or x to exit")
            print ('')

def welcome(name):

    print("****************************")
    print("Hello", name, "Welcome to the fire, ice and water game!")
    print("You will play this game against our champion computer Zor")
    print("To play, enter 1 for fire, 2 for ice and 3 for water")
    print("Your choice will be compared against the choice made by Zor")
    print("fire wins against ice")
    print("ice wins against water")
    print("water wins against fire")
    print("****************************")
    print(" ")

#Call the randint function to get a random integer between 1 and 3

def getZorChoice():
    choice = randint(1,3)
    return choice

#Compare player and Zor choices to determine winner

def getWinner(player, Zor, name):

    if int(player) == Zor:
        message = ("Draw game - no winner!")

    elif int(player) == 1 and Zor == 2:
        message = ("fire beats ice ... Zor wins!")

    elif int(player) == 1 and Zor == 3:
        message = "fire beats ice... " + name + " wins!"

    elif int(player) == 2 and Zor == 1:
        message = ("water beats fire... ", name, " wins!")

    elif int(player) == 2 and Zor == 3:
        message = ("ice beats water.... Zor wins!")

    elif int(player) == 3 and Zor == 1:
        message = ("water beats fire... Zor wins!")

    elif int(player) == 3 and Zor == 2:
        message = ("water beats ice... ", name, " wins!")

    print(" ")
    return message

playgame()