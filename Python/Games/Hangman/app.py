#Imports All Variables and Functions From Assets List
from assets import *
#Imports String 
import string

#Function Used To Play The Game
def playgame():

    #How Many Letters You Can Incorrectly. The "lives" Variable Is Used To Display Hangman Picture Stages
    lives = 6

    #Assigns and Empty Variable Named "word" That Will Be Filled In Later
    word = ""

    #Used For When You Play Multiple Games. If Words Are Still In List Then You Can Play Again. If Not, You Can't Play Again
    if len(wordlist) > 0:
        word = getword() #Executes "getword" Function From assets.py, To Randomly Select A Word From "wordlist" For You To Solve 
        wordlist.remove(word) #Removes Selected Word From List, So You Won't Have Same Word Again If You Try Again
    else:
        #If No More Words Are In "wordlist" Variable Then You Can't Play Again and Are Prompted That You Are Out Of Words.
        print("Out Of Words!!!")

    #This Is Variable That Shows How Many Characters Are In Word and Is Filled In When Guessed Correctly
    toguess = ["_" for c in word] #For Example: The Word Is "Mouse", This Displays _ _ _ _ _ . You Guess "u" Then This Displays _ _ U _ _

    print("Word:"," ".join(toguess)) #This Prints To Console, The Above Display("toguess" Variable)

    #This Prints To Console Hangman Picture At It's Default State(No Body Parts or Losses Yet)
    print(hangman[6])

    #This Variable "notguessed" Makes A List With The Letters Of The Alphabet That Haven't Been Used Yet
    notguessed = [i for i in string.ascii_uppercase]

    #This Breaks Word Into A List Of Characters In Word For Comparison Purposes
    word = list(word)

    #This While Loop Does Most Of The Work Allowing You To Guess Letters Until You Are Correct or You Lose
    while lives > 0: #Loop Continues Untils Lives Are Used Up

        #Prompts User For Input To Guess A Letter
        letter = str(input("Guess A Letter: ")).upper()

        #If Letter Is Not In Alphabet List Then It's Been Used Already Or Is Invalid
        if letter not in notguessed:
            print(letter, "has been used already")

        #If Letter Is In Alphabet List Then It Hasn't Been Used Yet and Will Be Removed From List 
        elif letter in notguessed:
            notguessed.remove(letter)

            #If Letter Is Not In Word, Then You Lose A Life
            if letter not in word:
                lives -= 1

        #For Loop That Compares If Letter Guessed Is In Word and If It Is, Then Assigns It To "toguess" Variable
        for i in range(len(word)):
            if word[i] == letter:
                toguess[i] = letter

        #Prints To Console The "toguess" Variable and Hangman Picture That Determines How Many Lives/Chances Are Left If Any
        print(f"Word: {'  '.join(toguess)}\n{hangman[lives]}")
        print(f"Letters Left: {notguessed}")

        #Compares If "toguess" Variable Is Equal To Word and Prints "You Win!!!" if Comparison Proves True As Well As Breaks Loop
        if "".join(word) == "".join(toguess):
            print("You Win!!!")
            break

    #If You Run Out Of Lives/Chances and Get Full Hangman Body, Console Then Prints The Word As Well As You Lose
    if lives == 0:
        print("Word Is:", "".join(word))
        print("You Lose!!!")

    #Console Prompts User To See If They Want To Play Again. If "Y" Then "playgame" Function Is Called and You Play Again, Else You Don't
    retry = str(input("Play Again(Y/N): ")).upper()
    if retry == "Y":
        playgame()
    else:
        print("Have A Good Day!!!")

        
playgame() #Calls/Executes "playgame" Function To Start Game

    
