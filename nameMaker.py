# kyle anderson         anderky01
# giannis antetokounmpo antetgi01
# kostas antetokounmpo  antetko01
# Lebron James          jamesle01
# Pascal Siakam         siakapa01


def nameCreator(name):

    firstLetter = name.split(" ")[1][0]

    try:
        lastName = name.split(" ")[1][0:5]
    except:
        lastNameSize = len(name.split(" ")[1])
        lastName = name.split(" ")[1][len(lastNameSize)]

    firstName = name[0:2]

    return lastName+firstName + '0', firstLetter


playerReferenceName, letter = nameCreator("Larry Nance Jr".lower())

print(playerReferenceName)
print(letter)
