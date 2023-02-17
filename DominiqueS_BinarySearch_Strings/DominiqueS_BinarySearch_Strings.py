
# This python program was written using:
#  -Visual Studio 2022
#  -Python v3.11
# !! Text files must be in same directory as .py file !!

# Array = Dataset being used (In this case a list of numbers)
# Query = Whatever number the user inputed to search
# Length = Current high range of list
# Start = Current low range of list

def check(array, query, length, start):                  # Passing through values from previous function (I probably could have used 1 instead of 2)

    global numberNotFound
    global previousIndex

    index = int(length + (start - length) // 2)                     # Index is set to half of the current range

    if (index != previousIndex):                                    # Fallback in case program gets stuck on the value closest to the query
        if (array[index] == query):

            endangermentLevel = endangerment(query)
            creatureType = identity(query)
            firstLetter = query[0]

            if (firstLetter == "a" or firstLetter == "e" or firstLetter == "i" or firstLetter == "o" or firstLetter == "u"):
                preface = "An"
            else:
                preface = "A"
            return print(f"Your creature has been found. {preface} {query} is a {creatureType}, and it's endangerment status is {endangermentLevel}.\n")
      
        elif (array[index] > query):                                # Since the array is sorted in order from highest to lowest, it checks the values of
            previousIndex = index                                   # whatever number is at the current index and sets the current floor or ceiling of the range
            return check(array, query, index, start)    # in accordance to whatever the case may be.
                                                                    
        elif (array[index] < query):                                # eg. query = 70, dataset = [55, 60, 71, 75], it would start at 60, due to rounding, then
            previousIndex = index                                   # it would see that 70 is larger than 60 and would move the floor upwards.
            return check(array, query, length, index)             
    else:
        return print("Sorry, that creature or input does not seem to be in the list, please try again.\n")

def endangerment(query):                                            # Simple conditional ladder to check for endangerment status and species

    global categories

    if (query == "chinese paddlefish"):
        severity = 0
    elif (query == "kunimasu"):
        severity = 1
    elif (query == "axolotl"):
        severity = 2
    elif (query == "whale shark" or query == "spotted eagle ray"):
        severity = 3
    elif (query == "walrus"):
        severity = 4
    elif (query == "spotted eagle ray"):
        severity = 5
    elif (query == "ghost crab" or query == "candy nudibranch" or query == "vampire squid" or query == "blobfish"):
        severity = 6

    return categories[severity]
        
def identity(query):

    global species

    if (query == "chinese paddlefish"):
        type = 0
    elif (query == "walrus"):
        type = 1
    elif (query == "kunimasu" or query == "blobfish"):
        type = 2
    elif (query == "axolotl"):
        type = 3
    elif (query == "vampire squid"):
        type = 4
    elif (query == "whale shark"):
        type = 5
    elif (query == "ghost crab"):
        type = 6
    elif (query == "spotted eagle ray"):
        type = 7
    elif (query == "candy nudibranch"):
        type = 8

    return species[type]

def removal(data):                                                  # Checks the list after it's been parsed from the file and removes
                                                                    # any invalid or unwanted characters
    invalidChars = ".><?';:[]{}\/=+-_()*&^%$#@!`~1234567890"    
   
    for x in data:
        if x in invalidChars:
            data.remove(x)
            removal(data)                                           # Recurses on itself so that the removal doesnt skip over an index
    else:                                                           # if two invalid characters are beside eachother in the list
        return data

# ------------------------------------------------------------------------------------------------------------------------ #
                                                                    # The start of the program (in terms of code run)
categories = [
                "extinct", # chinese paddlefish
                "extinct in the wild", # kunimasu
                "critically endangered", # axolotl
                "endangered", # whale shark (eagle ray as a species)
                "vulnerable", # walrus
                "near threatened", #spotted eagle ray
                "least concern", # Ghost crab, candy nudibranch, vampire squid, blobfish
               ]

fileNotFound = True

while fileNotFound:                                                                        # Seperate loop for file request
    creatureFileName = input("Enter the name of the creature database you wish to open: ") # Requests the file name of the data to be read
    speciesFileName = input("Enter the name of the species database you wish to open: ")

    try:
        creatureFile = open(f"{creatureFileName}.txt", "r")
        speciesFile = open(f"{speciesFileName}.txt", "r")

        creatures = creatureFile.read().replace('\n', '').split(',')                        # Converts large string of text in the file to a list,
        species = speciesFile.read().replace('\n', '').split(',')                           # separating at commas

        creatures = removal(creatures)
        species = removal(species)

        fileNotFound = False

    except:
        print("Oops! it looks like the file(s) you're looking for does not exist! Please try again.") # Errors if file fails to be read

creatures.sort()                                                     # Sorts dataset (important for later in program)
length = len(creatures)

numberNotFound = True
previousIndex = -1

while numberNotFound:
    query = input(f"Input a creature from the list below to check its status, or type 'exit' to exit the program.\n{creatures}\n ")
    query.lower()

    if (query == "exit"):
        quit()
    else:
        check(creatures, query, length, 0)

# Apologies, I did not submit this assignment in parts because the requirements are fairly tied together and I was all over the place
# with trying to implement everything simultaneously.

