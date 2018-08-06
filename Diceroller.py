import re #This is how we inport regular expressions
import random

#This is a function that takes in a line from the dicetext file and searches for the numerical value in it
def workroll(dies): #Passing in the line from down below
    p = re.search('\d+', dies) #Scans through a string, looking for any location where the condition of \d+ matches. \d maches any decimal digit. + allows use to find a decimal digit more than one time. dies is the line we are searching through.
    if p: #This should be the main loop the program runs
        return(int(p.group())) #We assign what we found to p, then return it to the script. .group() returns the string matched above, without us receiving a lot of unneccisary information: <_sre.SRE_Match object; span=(1, 4), match='123'>. Using int() allows us to treat the returned value as an integer.
    elif p == None: #This will take care of any Nonetype returns
        print("This program cannot accept dice that aren't technically numerical in nature.")
        Script()

#This function will generate the actual values from the dice roll
def roller(diceline):
    die = diceline.readline()

    if die:
        value = workroll(die) #This will give me how many sides the dice has

        if value == None: #Exception handle
            quit()

        try: #This will help prevent any errors in case someone were to put a string as the equivalent to how_many
            how_many = int(input("How many d{} would you like to roll? ".format(value))) #This will tell me know many dice we are rolling (how many random numbers to generate)

            #Generate the random values
            print("Your values are: ")
            for x in range(how_many):
                print(random.randint(1, value))

            #Will keep running the file until the file is clear
            return roller(diceline)

        #This is a way to handle an error, such as if someone pu in "hi" as a dice type
        except ValueError:
            print("This program will not accept such a silly request.")
            Script()

#This is the actual program to run
def Script():
    dicetext = open("dicetext.txt", 'w')

    dice = input("What dice would you like to roll? ").split() #Splits up multiple inputs so that we can analyze them individually

    for value in dice:
            dicetext.write(value + '\n')

    dicetext.close()

    dice2 = open("dicetext.txt", "r")

    roller(dice2)

#This is what you will see when you first run the program
print("Hello! You must be having some fun if you're using me!")

Script()
