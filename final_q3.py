# Final Assessment
# Q3

import random

# Generates the score file for each player
def printScore(name, score):
    with open("%s.txt" % name, "w") as f:
        outputString = ""
        outputString += "-" * 40 + "\n"
        outputString += "\tPlayer name: %s\n" % name
        outputString += "\tScore: %d\n" % score
        outputString += "-" * 40
        f.write(outputString)

# Opens score.txt and allows read/write access
with open("score.txt", "r+") as f:
    # Reads the file, splits every record by newline then stores it in a variable
    data = f.read().split("\n")
    # Splits records by delimiter "|" and stores it in a variable
    splitData = []
    for i in range(len(data)):
        splitData.append(data[i].split("|"))
    players = []
    scores = []
    # Loops through the splitData variable and adds the player names and scores to respective lists
    for i in range(len(splitData)):
        players.append(splitData[i][0])
        scores.append(splitData[i][1])
    dictData = {}
    # Loops through the splitLibrary variable and adds the player names and scores to a dictionary
    for i in range(len(players)):
        dictData[players[i]] = int(scores[i])
    print(dictData)
    
    playStatus = True

    while playStatus == True:
        # Asks the user for a player name and stores it in a variable
        name = input("Enter player name: ")
        # Upper cases the player name
        name = name.upper()
        # Checks if the player name is in the dictionary
        if name in list(dictData.keys()):
            # Prints a welcome back message and the player's score
            print("Welcome back, " + name)
            print("Score: " + str(dictData[name]))
        else:
            # Prints a welcome message and the player's score
            print("Welcome, " + name)
            print("Score: 0")
            # Adds the player name and score to the dictionary
            dictData[name] = 0
        print("")
        # Asks five questions
        for i in range(5):
            # Obtains a random number between 1 and 10
            num = random.randint(1, 10)
            # Asks the user to guess whether the number is even or odd
            promptAns = input("Odd or even? : ")
            # Checks if the number is even or odd
            if num % 2 == 0:
                # Checks if the user's answer is even
                if promptAns.lower() == "even":
                    print("You guess it right! The number is %d" % num)
                    # Adds one to the player's score
                    dictData[name] += num
                else:
                    print("Oops! The number is %d" % num)
                    # Subtracts one from the player's score
                    dictData[name] -= num
                    # Prevents the player from getting negative scores
                    if dictData[name] < 0:
                        dictData[name] = 0
            else:
                # Checks if the user's answer is odd
                if promptAns.lower() == "odd":
                    print("You guess it right! The number is %d" % num)
                    # Adds one to the player's score
                    dictData[name] += num
                else:
                    print("Oops! The number is %d" % num)
                    # Subtracts one from the player's score
                    dictData[name] -= num
                    # Prevents the player from getting negative scores
                    if dictData[name] < 0:
                        dictData[name] = 0
            # Prints current score
            print("Score: " + str(dictData[name]))
        # Prints final score
        print("%s, your score is %d" % (name, dictData[name]))

        # Asks the user if they want to print a score file
        toPrint = input("Do you want to print your score? (yes/no): ")
        if toPrint.lower() == "yes":
            printScore(name, dictData[name])
        
        # Asks the user if they want to play again
        toPlayAgain = input("Play again? (yes/no): ")
        if toPlayAgain.lower() == "no":
            playStatus = False

    # Syncronises the dictionary with the file
    outputString = ""
    for i in range(len(list(dictData.keys()))):
        outputString += list(dictData.keys())[i] + "|" + str(dictData[list(dictData.keys())[i]]) + "\n"
    outputString = outputString[:-1]
    f.seek(0)
    f.write(outputString)
    f.truncate()
