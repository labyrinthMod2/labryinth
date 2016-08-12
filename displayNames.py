# Labyrinth Module 2
# Cecily Tighe
# 2016

# create label names to be imported in both documents to avoid having a double import

lstDisplayLBLNames = []

# define the names of the labels that are used in both files and make them global
for each in range(96):
        # first the individual names are created and appended to the list 'lstDisplayLBLNames'
    if each < 12:
        name = 'disp' + '0' + str(each)
    elif each < 24:
        name = 'disp' + '1' + str(each - 12)
    elif each < 36:
        name = 'disp' + '2' + str(each - 24)
    elif each < 48:
        name = 'disp' + '3' + str(each - 36)
    elif each < 60:
        name = 'disp' + '4' + str(each - 48)
    elif each < 72:
        name = 'disp' + '5' + str(each - 60)
    elif each < 84:
        name = 'disp' + '6' + str(each - 72)
    else:
        name = 'disp' + '7' + str(each - 84)

    lstDisplayLBLNames.append(name)

    lblTime = ['lblTimeElapsed']







