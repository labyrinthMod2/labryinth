# Eleni Cook
# 2016
# this creates the button names for the buttons in the GUI, so they can be accessed in both the GUI and fucntion files



# this list is a list of the button names
listBtnName = []

# this list creates the list of button names
for btnNames in range(1,97):
    names = "btnMaze" + str(btnNames)
    listBtnName.append(names)
