#Imports Path Method From PathLib Module
from pathlib import Path
#Imports Random Module
import random as r

#List Of Words That Can Be Chosen. Feel Free To Add More, but They Must Be Letters, Spaces, or Hypens(-) Only In Word Added
wordlist = []

#Imports Words From "wordlist.txt" File In This Directory. To Add More Words, Open Text File And Add Each New Word On A New Line
with open(Path(__file__).with_name("wordlist.txt")) as words:
    for line in words.readlines():
        wordlist.extend(line)

#Removes \n From Words So They Don't Seem To Have New Lines When Playing Game
wordlist = "".join(wordlist).split("\n")

#Converts "wordlist" To Set To Remove Duplicate Words
wordlist = set(wordlist)

#Converts "wordlist" Back Into A List So Game Will Work Right When Removing Words Already Used On Play Again Games
wordlist = list(wordlist)

#Prints Amount Of Words Currently In List
def wordcount():
    return f"Words Currently In WordList: {len(wordlist)}"

#Calls/Executes "wordcount" Function
wordcount()

#This Just Loops Through and Makes All Letters In The Words Capitalized
for index in range(len(wordlist)):
    wordlist[index] = wordlist[index].upper()

#Function That Randomly Picks A Word On The List For You To Guess
def getword():
    return r.choice(wordlist)

#Error Count As In Regular Hangman, For Each Letter You Guess Incorrectly, Another Body Part Is Drawn and You Lose When Body Is Complete
hangman= [
    """
    ___
   | | 
   | O
   |/|\\
   |/ \\
   ======
    """,
    """
    ___
   | | 
   | O
   |/|\\
   |/ 
   ======
    """,
    """
    ___
   | | 
   | O
   |/|\\
   |
   ======
    """,
    """
    ___
   | | 
   | O
   |/|
   |
   ======
    """,
    """
    ___
   | | 
   | O
   | |
   |
   ======
    """,
    """
    ___
   | | 
   | O
   | 
   |
   ======
    """,

    """
    ___
   | | 
   | 
   |
   |
   ======
    """    
]
