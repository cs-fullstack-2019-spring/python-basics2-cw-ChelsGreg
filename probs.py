def main():
    prob1()
     prob2()
    prob4()
    prob4()



#Create a random number. Print the number.

def prob1():

    import random
    randomNum = random.randint(7, 50)
    print(randomNum)


#
#
# #Create a function that has a loop that quits with ‘q’.
# # If the user doesn't enter 'q', ask them to input another string.
#
def prob2():

    userInput = input("Enter a sentence, or q")
    while(userInput != "q"):
        userInput = input("Enter another string")






#Create a function that will loop until the user enters '0'.
# Ask the user to enter a positive integer number.
# Print 0 to that number and ask them again to enter a number until they enter '0'. Repeat.
#
def prob3():

    untilZero =int(input("Enter a positive number"))
    while(untilZero != 0):
        for i in range(0, untilZero):
            print(i)
        untilZero = int(input("Enter another number"))





#Create a function that creates a random number. Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
# If they don't get it right, tell them if their next guess has to be higher or lower.

def prob4():


    import random

    guessNum = random.randint(0,10)
    userInput = int(input("Guess the number!"))


    while(userInput > guessNum):
            print("Too high")
            userInput = int(input("Guess the number again!"))

    while(userInput < guessNum):
            print("Too low")
            userInput = int(input("Guess the number again!"))








if __name__ == '__main__':
    main()