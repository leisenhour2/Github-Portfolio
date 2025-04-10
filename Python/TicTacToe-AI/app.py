import random as r

user = str(input("X's or O's: ")) #This Asks The Player If They's Rather Be X's or O's

pturn = False #This Determines If It's Players Turn. DEFAULT: False

#This Is Lists That Deletes Items From Itself Once Used So We Don't Overwrite Other Player's Turn
cells = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

#This Is The Board That Is Printed and Will Update Itself Every Turn
board = "|A|B|C|\n|D|E|F|\n|G|H|I|"

#This Randomly Picks Who Starts The Game 
turn = r.choice(["O", "X"])

#This Determines If It's Player's or AI's Turn
if turn != user:
    pturn = True
elif turn == user:
    pturn = False

#Function That Initializes and Starts The Game
def play():

    #Variables Pulled From Outside Function So That They May Be Updated
    global board, turn, cells, user, pturn
    print(f"{turn}'s Turn") #Print To Console Whose Ever Turn It Is
    cell = ""
    #Player Can Choose What Cells On Board To Place an "X" or "O" If It's Player's Turn, Otherwise AI Chooses Randomly From What's Left
    if pturn:
        cell = str(input("Enter Cell Letter: ").upper())
    elif not pturn:
        cell = r.choice(cells)
    #Turn Sequence For "X" That Replaces Cell That Hasn't Been Chosen Yet With "X"
    if turn == "X":
        if cell in cells: #Checks If Cell Is Available
            board = board.replace(cell, "X") #If Cell's Available Then Replaces Value With "X"
            cells.remove(cell) #Cell Is Removed So It Can't Be Used or Overwritten By Other Player
        else: #If Cell Not Available Then Prints Statement Saying So and Goes Back To Function To Start Again
            print("Cell Entry Invalid or Used Already!")
            play()
    #Turn Sequence For "O" That Replaces Cell That Hasn't Been Chosen Yet With "O"
    else:
        if cell in cells:
            board = board.replace(cell, "O")
            cells.remove(cell)
        else:
            print("Cell Entry Invalid or Used Already!")
            play()

    #Changes Player When Turn Is Over
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    if pturn:
        pturn = False
    else:
        pturn = True
print(f"\n{board}\n") #Prints Board


#While Loop That Determines If Winning Plays Have Been Found
while len(cells) > 0:
    #WINNING WITH ROWS
    if "O|O|O" in board:
        print("O Wins!!!")
        break
    elif "X|X|X" in board:
        print("X Wins!!!")
        break
    #COLUMNS
    #C1
    elif board[1] == "X" and board[9] == "X" and board[17] == "X":
        print("X Wins!!!")
        break
    elif board[1] == "O" and board[9] == "O" and board[17] == "O":
        print("O Wins!!!")
        break
    #C2
    elif board[3] == "X" and board[11] == "X" and board[19] == "X":
        print("X Wins!!!")
        break
    elif board[3] == "O" and board[11] == "O" and board[19] == "O":
        print("O Wins!!!")
        break
    #C3
    elif board[5] == "X" and board[13] == "X" and board[21] == "X":
        print("X Wins!!!")
        break
    elif board[5] == "O" and board[13] == "O" and board[21] == "O":
        print("O Wins!!!")
        break

    #DIAGONALS
    #D1
    elif board[1] == "X" and board[11] == "X" and board[21] == "X":
        print("X Wins!!!")
        break
    elif board[1] == "O" and board[11] == "O" and board[21] == "O":
        print("O Wins!!!")
        break
    #D2
    elif board[5] == "X" and board[11] == "X" and board[17] == "X":
        print("X Wins!!!")
        break
    elif board[5] == "O" and board[11] == "O" and board[17] == "O":
        print("O Wins!!!")
        break
    else:
        play()
    print(f"\n{board}\n")

#After Iterating Through Winning Plays, If It Is Last Play Then Winner or Cat/Tie Is Presented, Then Prints "Thanks For Playing!!!"
if len(cells) == 0:
    #WINNING WITH ROWS
    if "O|O|O" in board:
        print("O Wins!!!")
    elif "X|X|X" in board:
        print("X Wins!!!")
    #COLUMNS
    #C1
    elif board[1] == "X" and board[9] == "X" and board[17] == "X":
        print("X Wins!!!")
    elif board[1] == "O" and board[9] == "O" and board[17] == "O":
        print("O Wins!!!")
    #C2
    elif board[3] == "X" and board[11] == "X" and board[19] == "X":
        print("X Wins!!!")
    elif board[3] == "O" and board[11] == "O" and board[19] == "O":
        print("O Wins!!!")
    #C3
    elif board[5] == "X" and board[13] == "X" and board[21] == "X":
        print("X Wins!!!")
    elif board[5] == "O" and board[13] == "O" and board[21] == "O":
        print("O Wins!!!")

    #DIAGONALS
    #D1
    elif board[1] == "X" and board[11] == "X" and board[21] == "X":
        print("X Wins!!!")
    elif board[1] == "O" and board[11] == "O" and board[21] == "O":
        print("O Wins!!!")
    #D2
    elif board[5] == "X" and board[11] == "X" and board[17] == "X":
        print("X Wins!!!")
    elif board[5] == "O" and board[11] == "O" and board[17] == "O":
        print("O Wins!!!")
    

    #If All Plays Are Done and There Is No Winner, Then Console Prints "Cat Wins!!!" Which Means It's A Draw
    else:
        print("Cat Wins!!!")
#Ending Statement That Thanks User For Playing
else:
    print("Thanks For Playing!!!")
    exit()