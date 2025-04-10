 #Imports Random Module and Shortens it so we can call functions using r.<function_here> instead of random.<function_here>
import random as r


#Function That Starts The Game
def start():
    TOP_VALUE = 5 #CONSTANT VALUE THAT LETS THE COMPUTER KNOW WHAT THE MAXIMUM NUMBER IN RANGE IS TO CHOOSE

    #Number the computer randomly chooses that start from 0 and ends with Max Value/TOP_VALUE
    #The +1 is added because the way the range method works starts from 0 and ends with (Max # - 1) unless stated otherwise
    cpu = r.randrange(TOP_VALUE + 1) 

    #This is player's/user's guess
    guess = int(input(f"Enter any number that ranges 0-{TOP_VALUE}: "))

    #This compares our value with cpu's value to see if we got it correct and then executes commands below accordingly
    if guess == cpu: #If we answer correctly then cpu prints Player Wins
        print("Player Wins!!!")
    else: #If we guess incorrectly then cpu prints Player Loses and gives correct answer
        print("Player Loses!!!")
        print("Correct Answer:", cpu)

    #This asks if player/user wants to play again and then executes commands accordingly
    playagain = str(input("Play Again?(y/n): ")).lower() 

    if playagain == "y": #If yes, then recalls start function and we play againe
        start()
    else: #If no, then cpu thanks us for playing and ends program
        print("Thanks For Playing!!!")

start() #This calls start function at the beginning



