#Modules Imported
import random as r 
import string as s

#String Generated By Using 2 Different Methods Of STRING Module and String Concat
char_list = s.ascii_lowercase + s.ascii_uppercase + "0123456789!@#$%^&*()-_++`~[]{}\|;:'\",<.?/"

#List That Will Have Passwords Added
passwords = []

#Amount Of Passwords Generated
total_passwords = int(input("How many passwords do you want to generate?: "))

#While Loop That Asks For Length Of Each Password and Creates password Variable For Later Use
while total_passwords > 0:
    password = ""
    pw_length = int(input(f"What is the length of password #{total_passwords}?: "))

    #While Loop Used To Alter Length Of Each Password, Choose Random Character From char_list
    while pw_length > 0:
        password += str(r.choice(char_list))
        pw_length -= 1 #Decrements pw_length Variable, So Proper Length Will Be Assigned To Each Password And While Loop Will Be Finite
    
    #Decrements total_passwords Variable, So You Don't Have Infinite While Loop and You'll Have Right Amount Of Passwords
    total_passwords -= 1

    #Adds Randomly Generated Passwords To passwords List
    passwords.append(password)

#For Loop That Prints Each Password From password List To A New Line
for word in range(len(passwords)):
    print("Password #", f"{word + 1}:", passwords[word])