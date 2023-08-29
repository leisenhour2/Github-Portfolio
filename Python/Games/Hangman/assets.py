#Imports Random Module
import random as r

#List Of Words That Can Be Chosen. Feel Free To Add More, but They Must Be Letters Only("No Spaces, Dashes/Slashes/Numbers, Etc.")
wordlist = [
    "portrait",
    "glory",
    "delay",
    "contract",
    "easy",
    "colleague",
    "shorts",
    "faith",
    "staff",
    "hair",
    "enfix",
    "hobby",
    "demonstrate",
    "doll",
    "maximum",
    "quest",
    "hypothesize",
    "family",
    "average",
    "uniform",
    "disagree",
    "stick",
    "worry",
    "population",
    "deficiency",
    "prayer",
    "frown",
    "monopoly",
    "up",
    "discipline",
    "suburb",
    "telephone",
    "sale",
    "continuation",
    "efflux",
    "radiation",
    "invasion",
    "referral",
    "sequence",
    "stake",
    "econobox",
    "cover",
    "forbid",
    "exploration",
    "slave",
    "raid",
    "sympathetic",
    "dozen",
    "premature",
    "loot"
]

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
