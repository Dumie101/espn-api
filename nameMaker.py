def nameCreator(playerName):
    firstLetter = playerName.split(" ")[1][0]

    try:
        lastName = playerName.split(" ")[1][0:5]
    except:
        lastNameSize = len(playerName.split(" ")[1])
        lastName = playerName.split(" ")[1][len(lastNameSize)]

    firstName = playerName[0:2]

    return lastName + firstName + '0', firstLetter
