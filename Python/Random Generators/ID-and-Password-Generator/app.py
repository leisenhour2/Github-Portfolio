# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import random
import string as s

first_name = input('Enter First Name: ') #New Users First Name
last_name = input('Enter Last Name: ') #New Users Last Name
suffix = input('Enter Suffix(Jr.,Sr,II,III,etc.) if applicable else press enter: ').upper() #New Users Suffix (Optional)
print('') #Prints a Blank Newline before Username and Password is Printed For Easier Readability
vowels =('a','e','i','o','u')


#Function used to generate Username Based Off Users Input
def user_gen():
    global first_name
    global last_name
    global suffix
    user = '' #Blank String Variable that will be changed and assigned to this functions return statement
    user_add = [
        first_name[:random.randint(1,len(first_name))], #Chooses and random amount of letters to slice off your first name for a unique username
        '_',
        last_name[:random.randint(1,len(last_name))], #Chooses and random amount of letters to slice off your last name for a unique username
        suffix[:3]
        ]
    for i in user_add:
        user += i
        
    return user.replace(' ', '_') #Returns New Username
    
username = user_gen() #Assigns Username returned By user_gen function 

#Function Used To Generate Password Based Off User Input
def pass_gen():
    global username
    username = username.lower()
    pass_word = ''
    for i in username:  #For Loop Used To Alter Vowels With Empty Spaces For A Unique Temp Password
        if i in vowels:
            i.replace(i,'')
        else:
            pass_word += i
    pass_word = list(pass_word) #Converts Password To List For Shuffling
    for time in range(5,10000): #Randomize Shuffling 
        pass_word = random.sample(pass_word,len(pass_word))
        
    pass_word = ''.join(pass_word).title() #Merges Shuffled Password List To A String
        
    return pass_word #Returns New Password

###START OF INCOMP LIST CREATION
           
incomp = list(s.ascii_lowercase) #Creates a List named incomp with the alphabet in it
l2 = [i for i in range(10)] #Creates a list named l2 with numbers 0-9 in it
l3 = ['!','@','#','$','%','^','&','(',')','-','_','=','+'] #Creates a list named l3 with symbols in it

#Adds list l2 to incomp list by iterating through each item in l2 and appending/adding it to incomp list
for i in l2:
    incomp.append(i)

#Adds list l3 to incomp list by iterating through each item in l3 and appending/adding it to incomp list
for i in l3:
    incomp.append(i)

###END OF INCOMP LIST CREATION

password = pass_gen() #Assigns Password returned by pass_gen function

#While loop that makes password 8 Characters Long and randomly makes each character uppercase or lower by randomizing Booleans which
#change character case based on whether it is True/False 
while len(password) < 8:
    uplow = [True,False]
    if (random.choice(uplow)):
        password += str(random.choice(incomp)).upper()
    else:
        password += str(random.choice(incomp)).lower()
    


print('Username: ' + str(username).title()) #Prints Username to Console
print('Temp Password: ' + str(password)) #Prints Password to Console