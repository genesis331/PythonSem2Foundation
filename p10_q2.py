# Practical 10
# Q2

import random

stateAndCapital = {
    "Johor": "Johor Bahru", 
    "Kedah": "Alor Setar", 
    "Kelantan": "Kota Bahru", 
    "Malacca": "Malacca City", 
    "Negeri Sembilan": "Seremban", 
    "Pahang": "Kuantan", 
    "Penang": "George Town", 
    "Perak": "Ipoh", 
    "Perlis": "Kangar", 
    "Sabah": "Kota Kinabalu", 
    "Sarawak": "Kuching", 
    "Selangor": "Shah Alam",
    "Terengganu": "Kuala Terengganu"
}
# Extracts the state names from the dictionary and stores it in a list
stateList = list(stateAndCapital.keys())

# Prepares 5 quiz files
for i in range(5):
    # Creates new quiz file and allows append-only access
    with open("quizfile" + str(i + 1) + ".txt", "a") as f:
        f.write("Name: \n")
        # Generates random numbers in a list
        numList = []
        while len(numList) < 10:
            num = random.randint(1, len(stateList))
            if num not in numList:
                numList.append(num)
        
        for i in range(len(numList)):
            # Writes a question
            f.write("\n" + str(i + 1) + ".\tWhat is the capital of " + stateList[numList[i] - 1] + "?\n")
            # Appends correct answer to the list
            selections = [stateAndCapital[stateList[numList[i] - 1]]]
            while len(selections) < 4:
                # Prepares a fake answer
                tempFakeAns = stateAndCapital[stateList[random.randint(1, len(stateList)) - 1]]
                # Appends the fake answer to the list
                if tempFakeAns not in selections:
                    selections.append(tempFakeAns)
            # Shuffles the selections
            random.shuffle(selections)
            # Writes the selections to the file
            f.write("\tA. " + selections[0] + "\n")
            f.write("\tB. " + selections[1] + "\n")
            f.write("\tC. " + selections[2] + "\n")
            f.write("\tD. " + selections[3] + "\n")
