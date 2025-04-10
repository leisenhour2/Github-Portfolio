import random as r #Imports the random module to use randomizer

#Function that allows user to put input words and then adds them to a random quote from the list
def adlib():
    print("Verbs are Actions or what you do.\nNouns are a person, place or thing.\nAdjectives(adj) are descriptive words.")
    
    #---User Input Variables---#
    verb1 = input("Verb #1: ")
    verb2 = input("Verb #2: ")
    verb3 = input("Verb #3: ")
    noun1 = input("Noun #1: ")
    noun2 = input("Noun #2: ")
    noun3 = input("Noun #3: ")
    adj1 = input("Adjective #1: ")
    adj2 = input("Adjective #2: ")
    adj3 = input("Adjective #3: ")
    #---Ends User Input Vars---#

    #List Of Quotes Used In AdLib Game With Each Item On A New Line For Readabilty
    quotes = [
    f"I used to {verb1} {noun1} when {noun2} was real {adj1}. {noun3}, not so much. But {noun1} I could {verb2}.",
    f"I {verb1} {noun1} at {noun2} with my {noun3}. They always had {noun1} dudes at the {noun2}, but I didn't {noun1} formally. I just {verb2} around a lot of {noun3}.",
    f"I'm a {noun1} of few {noun2}.",
    f"I'm a {adj1} {noun1}, I don't really get {verb1}.",
    f"{noun1} only know {noun2} for what they've {verb1}, but that only {adj1} about 10 percent of what {noun2} {verb2}.",
    f"I'll take two {noun1}'s off just to {verb1} to {noun2} and not do any {noun3} so {noun2} can {verb2} all {noun3} and then when {noun2} go do my {noun3}. It's all in me. I'll {verb1} to a different genre every two {noun1}'s or something, {verb3} it, 24 {noun1}'s straight.",
    f"I {verb1} it for {noun1} and for {noun2}. Half the time I don't know why I make what I {verb1}. I'd {verb1} this if no one was {verb2}. I'm {adj1}. I've got the {noun3}.",
    f"I've {verb1} about three or four {noun1}'s of {noun2}, and two {noun1}'s of {noun3}.",
    f"I {verb1} a few {noun1}'s every {noun2}, but I'm mostly at {noun3}, {verb2} music. Day and night.",
    f"It's not {adj1} to {verb1} like {noun1}, but you can {verb2} beats like {noun1} with your {noun2}, so that's why {noun3} {verb1}'s like {noun1}."
]
    
    print(r.choices(quotes)) #Uses random module to randomize what quote is used in AdLib Game






