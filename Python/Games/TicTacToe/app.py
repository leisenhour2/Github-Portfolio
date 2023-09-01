#Imports Random Module
import random as r

turn = r.choice(["O","X"]) #Randomly Chooses Whose Turn It Is At The Start 
rows = ["O O O", "X X X"] #Winning Letters For Rows 
board = "" #Creates an Empty String Variable That Is Filled Later
beenUsed = ["A","B","C","D","E","F","G","H","I"] #Creates A List With What Cells Haven't Been Used Yet

#Function Used To Create Board and Display Board
def create_board():
    global board
    board = "A B C\nD E F\nG H I"
    print(f"\n{board}\n")

#Function Called To Check If Winning Plays Are In The Board
def checkBoard():
    global turn
    print(f"\n{board}\n") #Prints Updated Board After Every Turn

    #Checks If There Are Rows Of "O" or "X" and Then Prints If Any Rows Are Completed and Then Exits Code
    if rows[0] in board: # "O O O"
        print("O Wins")
        exit()
    if rows[1] in board: #"X X X"
        print("X Wins")
        exit()

    #Checks If There Are Columns Of "O" or "X" and Then Prints If Any Columns Are Completed and Then Exits Code 
    #Column1
    if board[0] and board[6] and board[12] == "X":
        print("X Wins")
        exit()
    if board[0] and board[6] and board[12] == "O":
        print("O Wins")
        exit()
    
    #Column2
    if board[2] and board[8] and board[14] == "X":
        print("X Wins")
        exit()
    if board[2] and board[8] and board[14] == "O":
        print("O Wins")
        exit()

    #Column3
    if board[4] and board[10] and board[16] == "X":
        print("X Wins")
        exit()
    if board[4] and board[10] and board[16] == "O":
        print("O Wins")
        exit()

    #Checks If There Are Diagonals Of "O" or "X" and Then Prints If Any Diagonals Are Completed and Then Exits Code 
    #Diagonal1
    if board[0] and board[8] and board[16] == "X":
        print("X Wins")
        exit()
    if board[0] and board[8] and board[16] == "O":
        print("O Wins")
        exit()

    #Diagonal2
    if board[4] and board[8] and board[12] == "X":
        print("X Wins")
        exit()
    if board[4] and board[8] and board[12] == "O":
        print("O Wins")
        exit()

    #If All The Above Statements Prove False and They're No More Items In BeenUsed List Then Cat Wins
    if len(beenUsed) < 1:
        print("Cat Wins")
        exit()

    #Next Turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"    

    #If None Of The Above Statements Are Resolved Then Game Resumes Until One Condition Above Proves True 
    play()

#Function That Starts The Game
def play():
    global board #Calls "board" Variable From Outside This Function So It May Be Updated

    #Prints To Console Whose Turn It Is
    print(f"{turn}'s Turn")

    #User Input To Select A Cell From The Unused Cells On Board
    cell = str(input("Enter Cell Letter: ").upper())
    #Conditional Statement That Shows Checks Which Cells Have Been Used and Places "X" or "O" In Unused Selected Cell
    if cell in beenUsed:
       if turn == "X":
            board = board.replace(str(cell), "X")
       else:
            board = board.replace(str(cell), "O")
    else: #If Cell Is Used Then Prints To Console Which Has Been Chosen and Allows For You To Select Again
        print(f"Cell# {cell} has been used already!")
        play()

    #Calls/Executes "checkBoard()" Function To See If Any Winners Have Been Decided
    checkBoard()
    

#Calls/Executes "create_board" Function To Create and Print New Board
create_board()
#Calls/Executes "play" Function To Start The Game
play()