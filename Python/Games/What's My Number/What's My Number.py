import random as r #Imports Random Module


#Function That Starts The Game
def start():
    num = int(input("Enter A Number Between 0-100: ")) #The Number The User/Player Chooses For CPU To Guess

    #Conditional Statements Toggled For Difficulty

    #If Player Chose A Number Between 51-100 Then Computer Can Guess Within The Range Of 2 Off(Ex. Player: 51, Computer: Low= 49 & High = 53)
    if num <= 100 and num > 50:
        cpu = r.randrange(num - 2, num + 2)

    #If Player Chose A Number Between 26-50 Then Computer Can Guess Within The Range Of 4 Off(Ex. Player: 26, Computer: Low= 22 & High = 30)
    elif num <= 50 and num > 25:
        cpu = r.randrange(num-4, num + 4)

    #If Player Chose A Number Between 11-25 Then Computer Can Guess Within The Range Of 6 Off(Ex. Player: 11, Computer: Low= 5 & High = 17)
    elif num <= 25 and num > 10:
        cpu = r.randrange(num-6, num + 6)

    #If Player Chose A Number Between 0-10 Then Computer Can Guess Within The Range Of 8 Off(Ex. Player: 9, Computer: Low= 1 & High = 17)
    elif num <= 10:
        cpu = r.randrange(num-8, num + 8)

    #Fail Safe If Computer Guesses Below 0 Then CPU's Number Is 0
    elif cpu < 0:
        cpu = 0

    #Fail Safe If Computer Guesses Above 100 Then CPU's Number Is 100    
    elif cpu > 100:
        cpu = 100

    #Conditional Statement To Tell If Computer Guessed Right

    #If CPU Guessed Right Number, Computer Wins
    if cpu == num:
        print(f"Computer Wins!!! Computer Chose: {cpu} and Number was {num}")

    #Else If CPU Guessed Wrong, Then Player Wins
    else:
        print(f"Player Wins!!! Computer Chose: {cpu} and Number was {num}")

    #Checks To See If You Want To Play Again, If y/Y Then Recalls Function and Starts Game Again, Else Wishes Player A Good Day and Ends
    again = input("Play Again(y/n): ").lower()
    if again == "y":
        start()
    else: 
        print("Have A Good Day!!!")

start() #Calls start Function Which Begins Game


