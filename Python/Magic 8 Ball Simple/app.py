import random as r

answers = (
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes, definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful" )
    
def start():
    str(input("What is your question?: "))
    print(r.choice(answers))
    play_again = str(input("Play Again(y/n): ")).lower()
    if play_again == "y":
        start()
    else: 
        print("Have A Good Day!!!")

start()