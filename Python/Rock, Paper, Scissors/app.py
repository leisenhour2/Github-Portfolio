#Imported Random Module
import random as r 

#Prints Rules To Console
print("""
    -------------------------
    ==========RULES==========
    -------------------------
    Player & AI Choose Rock, 
    Paper, or Scissors.

    To Win:
        Choose Correctly:
            Rock > Scissors,
            Scissors > Paper,
            Paper > Rock
    -------------------------        
      """)

#Function That Determines The Winner
def winner(ai, user):

    #Conditional Statement That Determines Losing Choices
    if ai == "Paper" and user == "Rock" or ai == "Rock" and user == "Scissors" or ai == "Scissors" and user == "Paper":
        print("AI Wins!!!")

    #Conditional Statement That Determines Winning Choices
    if ai == "Paper" and user == "Scissors" or ai == "Rock" and user == "Paper" or ai == "Scissors" and user == "Rock":
        print("Player Wins!!!")

    #Conditional Statement That Determines Tie Game
    elif ai == user:
        print("Tie Game!!!")

    #User Input Asking Player If They Would Like To Play Again
    replay = str(input("Play Again(Y/N): ")).upper()

    #Conditional Statements That Determine If Player Is Playing Again Or Not
    if replay == "Y":
        play()
    else:
        print("Have A Good Day!!!")

#Function That Makes AI Randomly Choose Rock/Paper/Scissors and Makes Player Choose By Their Input
def play():

    #Rock/Paper/Scissors Randomly Chosen By AI
    ai_choice = r.choice(("Rock", "Paper", "Scissors"))

    #User Input For Player To Choose Rock/Paper/Scissors
    user_choice = str(input("Rock, Paper, or Scissors: ")).capitalize()

    #Console Prints What Player and AI Chose
    print(f"Player's Choice: {user_choice}, AI's Choice: {ai_choice}")

    #Calls winner Function With AI and Player's Choices As Arguments
    return winner(ai_choice, user_choice)

#Executes/Calls Play Function
play()
