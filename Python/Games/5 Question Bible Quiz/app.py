#Constant Variables
MAX_SCORE = 100 #Total Score That Player Can Gain
POINTSPERQUESTION = 20 #How many Points Each Question Is Worth

#Questions and Answers Are In A Specific Order.
#List Of Questions
QUESTIONS = ["_____'s Ark. ",
             "Who led people out of Egypt? ",
             "Who threw a stone with a sling and took out a giant? ",
             "Famous Bible Verse - John _:16. ",
             "Cain and ____: "]

#List Of Answers 
ANSWERS = ("Noah",
           "Moses",
           "David",
           "3",
           "Abel")
#End Constant Variables

#Variable(s)
score = 0 #Score That The Player Has Currently


#Loops Through The Questions And Asks For User Input For Each One.
for i in range(len(QUESTIONS)):
    print("Question #", i+1, ": ")
    val = input(QUESTIONS[i])

    #Compares Answers To Questions
    #i = Question Player Is On
    if i == 0 and val == ANSWERS[0]:
        score += POINTSPERQUESTION
    elif i == 1 and val == ANSWERS[1]:
        score += POINTSPERQUESTION
    elif i == 2 and val == ANSWERS[2]:
        score += POINTSPERQUESTION
    elif i == 3 and val == ANSWERS[3]:
        score += POINTSPERQUESTION
    elif i == 4 and val == ANSWERS[4]:
        score += POINTSPERQUESTION


print(f"{score}/{MAX_SCORE}") #Prints Current Score/ Max Score
