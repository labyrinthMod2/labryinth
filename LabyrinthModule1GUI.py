# Eleni Cook
# 2016
# This is the GUI for Labyrinth Module 1 Software
# this GUI enables the user to implement the maze

from Tkinter import *
from PIL import Image, ImageTk


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Labyrinth")
        self.master.minsize(850, 550)
        self.fnCreateWidgets()

    def fnCreateWidgets(self):
        #background color
        backgroundColour = '#b3c9d1'
        #set the default image for the maze
        self.blank = PhotoImage(file = 'mikey.gif')
        size = 55,55
        imTransparent = Image.open("transparent1.png")
        imTransparent.thumbnail(size, Image.ANTIALIAS)
        photoTransparent = ImageTk.PhotoImage(imTransparent)



        # create the list of names for the labels in the display
        self.lstDisplayLBLNames = []

        # create the frame
        self.frWindow = Frame(height=400, width=500, bg=backgroundColour)
        self.frWindow.pack(fill=BOTH, expand=1)



        

        #menu bar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Quit")
        menubar.add_cascade(label="File", menu=fileMenu)


    
        wdBaseWindow.config(menu=menubar)
# create canvas
        # self.c = Canvas(self.frWindow, borderwidth=2, bg="black", width=50, height=50)
        # self.c.grid(row=2, column = 2, rowspan =12, columnspan =12)

        #self.frWindow.rowconfigure(0, weight=1)
        #self.frWindow.columnconfigure(0, weight=1)



        # blank labels for spacing
        self.lbl1 = Label(self.frWindow, bg = backgroundColour)
        self.lbl1.grid(row =0)

        self.lbl1 = Label(self.frWindow, bg = backgroundColour)
        self.lbl1.grid(row =6)


        self.lbl2 = Label(self.frWindow, width = 2, bg =backgroundColour)
        self.lbl2.grid(column = 0)

        self.lbl3 = Label(self.frWindow, width = 2, bg =backgroundColour)
        self.lbl3.grid(column = 1)

        """DISPLAY Grid Arrangement:
        8x12
                0      1     2
               0  1   2  3   4  5
         0  0 |X||X| |X||X| |X||X|
            1 |X||X| |X||X| |X||X|

         1  2 |X||X| |X||X| |X||X|
            3 |X||X| |X||X| |X||X|

        Labels that hold images of different route combinations

        Naming:
        Row 1, comumn 1 = disp00
        Row 2, column 4 = disp24
        etc.
        """
        # this loop creates the 15 labels
        for each in range(96):
            # first the individual names are created and appended to the list 'lstDisplayLBLNames'
            if each < 12:
                name = 'disp' + '0' +str(each)
            elif each <24:
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
            self.lstDisplayLBLNames.append(name)
            # the list is used to create a set of labels
            self.lstDisplayLBLNames[each] = Label(self.frWindow,image = self.blank, width=50, height=50, relief=SUNKEN)

            # every second column has x direction padding to easily see which sector the Sphero is located in
            if (int(name[-1]) + 1)  % 2 == 0:
                self.lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, padx = (1,5.5))
            # every label in the second row has padding on the bottom to created 3 clear sectors
            if (int(name[-2] ) + 1) % 2 == 0:
                self.lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, pady=(1, 5.5))
            # labels not in columns 1 or 3 or in the second row are simply given a grid position
            else:
                self.lstDisplayLBLNames[each].grid(row = int(name[-2]) + 2, column= int(name[-1]) + 2)



# add waypoints button
        self.btnAddWaypoints = Button(self.frWindow, text="Add Waypoints", font=("Calibri", 12), )
        self.btnAddWaypoints.grid(row=4, column=1, sticky = E)

# delete waypoints button
        self.btnDeleteWaypoints = Button(self.frWindow, text="Delete Waypoints", font=("Calibri", 12))
        self.btnDeleteWaypoints.grid(row=5, column=1, sticky = E)

# add barriers and terrain button
        self.btnTerrain = Button(self.frWindow, text="Add Barriers & Terrain", font=("Calibri", 12),)
        self.btnTerrain.grid(row=8, column=1, sticky =E )

# delete barriers and terrain button
        self.btnDeleteTerrain = Button(self.frWindow, text=" Delete Barriers & Terrain", font=("Calibri", 12),)
        self.btnDeleteTerrain.grid(row=9, column=1, sticky =NE)

# open picture
        self.btnOpenPicture = Button(self.frWindow, text=" Open Picture", font=("Calibri", 12))
        self.btnOpenPicture.grid(row=2, column=1, sticky =SE)

# solve button calls a funtion to find all the possible routes
        self.btnSolve = Button(self.frWindow, text=" Solve",font=("Calibri", 12),)
        self.btnSolve.grid(row=10, column=3)

# quit button
        self.btnQuit = Button(self.frWindow, text=" Quit", font=("Calibri", 12),)
        self.btnQuit.grid(row=10, column=8,sticky = E)


    # buttons for the grid of the maze
        self.btnMazeGrid1 = Button(self.frWindow, text= "1", font=("Calibri", 12), image = photoTransparent)
        self.btnMazeGrid1.grid(row=2, column=2, sticky = W+E+N+S )
        self.btnMazeGrid1.Image = photoTransparent

        self.btnMazeGrid2 = Button(self.frWindow, text= "2", font=("Calibri", 12))
        self.btnMazeGrid2.grid(row=2, column=3, sticky = W+E+N+S )

        self.btnMazeGrid3 = Button(self.frWindow, text= "3", font=("Calibri", 12))
        self.btnMazeGrid3.grid(row=2, column=4, sticky = W+E+N+S )

        self.btnMazeGrid4 = Button(self.frWindow, text= "4", font=("Calibri", 12))
        self.btnMazeGrid4.grid(row=2, column=5, sticky = W+E+N+S )

        self.btnMazeGrid5 = Button(self.frWindow, text= "5", font=("Calibri", 12))
        self.btnMazeGrid5.grid(row=2, column=6, sticky = W+E+N+S )

        self.btnMazeGrid6 = Button(self.frWindow, text= "6", font=("Calibri", 12))
        self.btnMazeGrid6.grid(row=2, column=7, sticky = W+E+N+S )

        self.btnMazeGrid7 = Button(self.frWindow, text= "7", font=("Calibri", 12))
        self.btnMazeGrid7.grid(row=2, column=8, sticky = W+E+N+S )

        self.btnMazeGrid8 = Button(self.frWindow, text= "8", font=("Calibri", 12))
        self.btnMazeGrid8.grid(row=2, column=9, sticky = W+E+N+S )

        self.btnMazeGrid9 = Button(self.frWindow, text= "9", font=("Calibri", 12))
        self.btnMazeGrid9.grid(row=2, column=10, sticky = W+E+N+S )

        self.btnMazeGrid10 = Button(self.frWindow, text= "10", font=("Calibri", 12))
        self.btnMazeGrid10.grid(row=2, column=11, sticky = W+E+N+S )

        self.btnMazeGrid11 = Button(self.frWindow, text= "11", font=("Calibri", 12))
        self.btnMazeGrid11.grid(row=2, column=12, sticky = W+E+N+S )

        self.btnMazeGrid12= Button(self.frWindow, text= "12", font=("Calibri", 12))
        self.btnMazeGrid12.grid(row=2, column=13, sticky = W+E+N+S )

        self.btnMazeGrid13 = Button(self.frWindow, text= "13", font=("Calibri", 12))
        self.btnMazeGrid13.grid(row=3, column=2, sticky = W+E+N+S )

        self.btnMazeGrid14 = Button(self.frWindow, text= "14", font=("Calibri", 12))
        self.btnMazeGrid14.grid(row=3, column=3, sticky = W+E+N+S )

        self.btnMazeGrid15 = Button(self.frWindow, text= "15", font=("Calibri", 12))
        self.btnMazeGrid15.grid(row=3, column=4, sticky = W+E+N+S )

        self.btnMazeGrid16 = Button(self.frWindow, text= "16", font=("Calibri", 12))
        self.btnMazeGrid16.grid(row=3, column=5, sticky = W+E+N+S )

        self.btnMazeGrid17 = Button(self.frWindow, text= "17", font=("Calibri", 12))
        self.btnMazeGrid17.grid(row=3, column=6, sticky = W+E+N+S )

        self.btnMazeGrid18 = Button(self.frWindow, text= "18", font=("Calibri", 12))
        self.btnMazeGrid18.grid(row=3, column=7, sticky = W+E+N+S )

        self.btnMazeGrid19 = Button(self.frWindow, text= "19", font=("Calibri", 12))
        self.btnMazeGrid19.grid(row=3, column=8, sticky = W+E+N+S )

        self.btnMazeGrid20 = Button(self.frWindow, text= "20", font=("Calibri", 12))
        self.btnMazeGrid20.grid(row=3, column=9, sticky = W+E+N+S )

        self.btnMazeGrid21 = Button(self.frWindow, text= "21", font=("Calibri", 12))
        self.btnMazeGrid21.grid(row=3, column=10, sticky = W+E+N+S )

        self.btnMazeGrid22 = Button(self.frWindow, text= "22", font=("Calibri", 12))
        self.btnMazeGrid22.grid(row=3, column=11, sticky = W+E+N+S )

        self.btnMazeGrid23 = Button(self.frWindow, text= "23", font=("Calibri", 12))
        self.btnMazeGrid23.grid(row=3, column=12, sticky = W+E+N+S )

        self.btnMazeGrid24 = Button(self.frWindow, text= "24", font=("Calibri", 12))
        self.btnMazeGrid24.grid(row=3, column=13, sticky = W+E+N+S )

        self.btnMazeGrid25 = Button(self.frWindow, text= "25", font=("Calibri", 12))
        self.btnMazeGrid25.grid(row=4, column=2, sticky = W+E+N+S )

        self.btnMazeGrid26 = Button(self.frWindow, text= "26", font=("Calibri", 12))
        self.btnMazeGrid26.grid(row=4, column=3, sticky = W+E+N+S )

        self.btnMazeGrid27 = Button(self.frWindow, text= "27", font=("Calibri", 12))
        self.btnMazeGrid27.grid(row=4, column=4, sticky = W+E+N+S )

        self.btnMazeGrid28 = Button(self.frWindow, text= "28", font=("Calibri", 12))
        self.btnMazeGrid28.grid(row=4, column=5, sticky = W+E+N+S )

        self.btnMazeGrid29 = Button(self.frWindow, text= "29", font=("Calibri", 12))
        self.btnMazeGrid29.grid(row=4, column=6, sticky = W+E+N+S )

        self.btnMazeGrid30 = Button(self.frWindow, text= "30", font=("Calibri", 12))
        self.btnMazeGrid30.grid(row=4, column=7, sticky = W+E+N+S )

        self.btnMazeGrid31 = Button(self.frWindow, text= "31", font=("Calibri", 12))
        self.btnMazeGrid31.grid(row=4, column=8, sticky = W+E+N+S )

        self.btnMazeGrid32 = Button(self.frWindow, text= "32", font=("Calibri", 12))
        self.btnMazeGrid32.grid(row=4, column=9, sticky = W+E+N+S )

        self.btnMazeGrid33 = Button(self.frWindow, text= "33", font=("Calibri", 12))
        self.btnMazeGrid33.grid(row=4, column=10, sticky = W+E+N+S )

        self.btnMazeGrid34 = Button(self.frWindow, text= "34", font=("Calibri", 12))
        self.btnMazeGrid34.grid(row=4, column=11, sticky = W+E+N+S )

        self.btnMazeGrid35 = Button(self.frWindow, text= "35", font=("Calibri", 12))
        self.btnMazeGrid35.grid(row=4, column=12, sticky = W+E+N+S )

        self.btnMazeGrid36 = Button(self.frWindow, text= "36", font=("Calibri", 12))
        self.btnMazeGrid36.grid(row=4, column=13, sticky = W+E+N+S )

        self.btnMazeGrid37 = Button(self.frWindow, text= "37", font=("Calibri", 12))
        self.btnMazeGrid37.grid(row=5, column=2, sticky = W+E+N+S )

        self.btnMazeGrid38 = Button(self.frWindow, text= "38", font=("Calibri", 12))
        self.btnMazeGrid38.grid(row=5, column=3, sticky = W+E+N+S )

        self.btnMazeGrid39 = Button(self.frWindow, text= "39", font=("Calibri", 12))
        self.btnMazeGrid39.grid(row=5, column=4, sticky = W+E+N+S )

        self.btnMazeGrid40 = Button(self.frWindow, text= "40", font=("Calibri", 12))
        self.btnMazeGrid40.grid(row=5, column=5, sticky = W+E+N+S )

        self.btnMazeGrid41 = Button(self.frWindow, text= "41", font=("Calibri", 12))
        self.btnMazeGrid41.grid(row=5, column=6, sticky = W+E+N+S )

        self.btnMazeGrid42 = Button(self.frWindow, text= "42", font=("Calibri", 12))
        self.btnMazeGrid42.grid(row=5, column=7, sticky = W+E+N+S )

        self.btnMazeGrid43 = Button(self.frWindow, text= "43", font=("Calibri", 12))
        self.btnMazeGrid43.grid(row=5, column=8, sticky = W+E+N+S )

        self.btnMazeGrid44 = Button(self.frWindow, text= "44", font=("Calibri", 12))
        self.btnMazeGrid44.grid(row=5, column=9, sticky = W+E+N+S )

        self.btnMazeGrid45 = Button(self.frWindow, text= "45", font=("Calibri", 12))
        self.btnMazeGrid45.grid(row=5, column=10, sticky = W+E+N+S )

        self.btnMazeGrid46 = Button(self.frWindow, text= "46", font=("Calibri", 12))
        self.btnMazeGrid46.grid(row=5, column=11, sticky = W+E+N+S )

        self.btnMazeGrid47 = Button(self.frWindow, text= "47", font=("Calibri", 12))
        self.btnMazeGrid47.grid(row=5, column=12, sticky = W+E+N+S )

        self.btnMazeGrid48 = Button(self.frWindow, text= "48", font=("Calibri", 12))
        self.btnMazeGrid48.grid(row=5, column=13, sticky = W+E+N+S )

        self.btnMazeGrid49 = Button(self.frWindow, text= "49", font=("Calibri", 12))
        self.btnMazeGrid49.grid(row=6, column=2, sticky = W+E+N+S )

        self.btnMazeGrid50 = Button(self.frWindow, text= "50", font=("Calibri", 12))
        self.btnMazeGrid50.grid(row=6, column=3, sticky = W+E+N+S )

        self.btnMazeGrid51 = Button(self.frWindow, text= "51", font=("Calibri", 12))
        self.btnMazeGrid51.grid(row=6, column=4, sticky = W+E+N+S )

        self.btnMazeGrid52 = Button(self.frWindow, text= "52", font=("Calibri", 12))
        self.btnMazeGrid52.grid(row=6, column=5, sticky = W+E+N+S )

        self.btnMazeGrid53 = Button(self.frWindow, text= "53", font=("Calibri", 12))
        self.btnMazeGrid53.grid(row=6, column=6, sticky = W+E+N+S )

        self.btnMazeGrid54 = Button(self.frWindow, text= "54", font=("Calibri", 12))
        self.btnMazeGrid54.grid(row=6, column=7, sticky = W+E+N+S )

        self.btnMazeGrid55 = Button(self.frWindow, text= "55", font=("Calibri", 12))
        self.btnMazeGrid55.grid(row=6, column=8, sticky = W+E+N+S )

        self.btnMazeGrid56 = Button(self.frWindow, text= "56", font=("Calibri", 12))
        self.btnMazeGrid56.grid(row=6, column=9, sticky = W+E+N+S )

        self.btnMazeGrid57 = Button(self.frWindow, text= "57", font=("Calibri", 12))
        self.btnMazeGrid57.grid(row=6, column=10, sticky = W+E+N+S )

        self.btnMazeGrid58 = Button(self.frWindow, text= "58", font=("Calibri", 12))
        self.btnMazeGrid58.grid(row=6, column=11, sticky = W+E+N+S )

        self.btnMazeGrid59 = Button(self.frWindow, text= "59", font=("Calibri", 12))
        self.btnMazeGrid59.grid(row=6, column=12, sticky = W+E+N+S )

        self.btnMazeGrid60 = Button(self.frWindow, text= "60", font=("Calibri", 12))
        self.btnMazeGrid60.grid(row=6, column=13, sticky = W+E+N+S )

        self.btnMazeGrid61 = Button(self.frWindow, text= "61", font=("Calibri", 12))
        self.btnMazeGrid61.grid(row=7, column=2, sticky = W+E+N+S )

        self.btnMazeGrid62 = Button(self.frWindow, text= "62", font=("Calibri", 12))
        self.btnMazeGrid62.grid(row=7, column=3, sticky = W+E+N+S )

        self.btnMazeGrid63 = Button(self.frWindow, text= "63", font=("Calibri", 12))
        self.btnMazeGrid63.grid(row=7, column=4, sticky = W+E+N+S )

        self.btnMazeGrid64 = Button(self.frWindow, text= "64", font=("Calibri", 12))
        self.btnMazeGrid64.grid(row=7, column=5, sticky = W+E+N+S )

        self.btnMazeGrid65 = Button(self.frWindow, text= "65", font=("Calibri", 12))
        self.btnMazeGrid65.grid(row=7, column=6, sticky = W+E+N+S )

        self.btnMazeGrid66 = Button(self.frWindow, text= "66", font=("Calibri", 12))
        self.btnMazeGrid66.grid(row=7, column=7, sticky = W+E+N+S )

        self.btnMazeGrid67 = Button(self.frWindow, text= "67", font=("Calibri", 12))
        self.btnMazeGrid67.grid(row=7, column=8, sticky = W+E+N+S )

        self.btnMazeGrid68 = Button(self.frWindow, text= "68", font=("Calibri", 12))
        self.btnMazeGrid68.grid(row=7, column=9, sticky = W+E+N+S )

        self.btnMazeGrid69 = Button(self.frWindow, text= "69", font=("Calibri", 12))
        self.btnMazeGrid69.grid(row=7, column=10, sticky = W+E+N+S )

        self.btnMazeGrid70 = Button(self.frWindow, text= "70", font=("Calibri", 12))
        self.btnMazeGrid70.grid(row=7, column=11, sticky = W+E+N+S )

        self.btnMazeGrid71 = Button(self.frWindow, text= "71", font=("Calibri", 12))
        self.btnMazeGrid71.grid(row=7, column=12, sticky = W+E+N+S )

        self.btnMazeGrid72 = Button(self.frWindow, text= "72", font=("Calibri", 12))
        self.btnMazeGrid72.grid(row=7, column=13, sticky = W+E+N+S )

        self.btnMazeGrid73 = Button(self.frWindow, text= "73", font=("Calibri", 12))
        self.btnMazeGrid73.grid(row=8, column=2, sticky = W+E+N+S )

        self.btnMazeGrid74 = Button(self.frWindow, text= "74", font=("Calibri", 12))
        self.btnMazeGrid74.grid(row=8, column=3, sticky = W+E+N+S )

        self.btnMazeGrid75 = Button(self.frWindow, text= "75", font=("Calibri", 12))
        self.btnMazeGrid75.grid(row=8, column=4, sticky = W+E+N+S )

        self.btnMazeGrid76 = Button(self.frWindow, text= "76", font=("Calibri", 12))
        self.btnMazeGrid76.grid(row=8, column=5, sticky = W+E+N+S )

        self.btnMazeGrid77 = Button(self.frWindow, text= "77", font=("Calibri", 12))
        self.btnMazeGrid77.grid(row=8, column=6, sticky = W+E+N+S )

        self.btnMazeGrid78 = Button(self.frWindow, text= "78", font=("Calibri", 12))
        self.btnMazeGrid78.grid(row=8, column=7, sticky = W+E+N+S )

        self.btnMazeGrid79 = Button(self.frWindow, text= "79", font=("Calibri", 12))
        self.btnMazeGrid79.grid(row=8, column=8, sticky = W+E+N+S )

        self.btnMazeGrid80 = Button(self.frWindow, text= "80", font=("Calibri", 12))
        self.btnMazeGrid80.grid(row=8, column=9, sticky = W+E+N+S )

        self.btnMazeGrid81 = Button(self.frWindow, text= "81", font=("Calibri", 12))
        self.btnMazeGrid81.grid(row=8, column=10, sticky = W+E+N+S )

        self.btnMazeGrid82 = Button(self.frWindow, text= "82", font=("Calibri", 12))
        self.btnMazeGrid82.grid(row=8, column=11, sticky = W+E+N+S )

        self.btnMazeGrid83 = Button(self.frWindow, text= "83", font=("Calibri", 12))
        self.btnMazeGrid83.grid(row=8, column=12, sticky = W+E+N+S )

        self.btnMazeGrid84 = Button(self.frWindow, text= "84", font=("Calibri", 12))
        self.btnMazeGrid84.grid(row=8, column=13, sticky = W+E+N+S )

        self.btnMazeGrid85 = Button(self.frWindow, text= "85", font=("Calibri", 12))
        self.btnMazeGrid85.grid(row=9, column=2, sticky = W+E+N+S )

        self.btnMazeGrid86 = Button(self.frWindow, text= "86", font=("Calibri", 12))
        self.btnMazeGrid86.grid(row=9, column=3, sticky = W+E+N+S )

        self.btnMazeGrid87 = Button(self.frWindow, text= "87", font=("Calibri", 12))
        self.btnMazeGrid87.grid(row=9, column=4, sticky = W+E+N+S )

        self.btnMazeGrid88 = Button(self.frWindow, text= "88", font=("Calibri", 12))
        self.btnMazeGrid88.grid(row=9, column=5, sticky = W+E+N+S )

        self.btnMazeGrid89 = Button(self.frWindow, text= "89", font=("Calibri", 12))
        self.btnMazeGrid89.grid(row=9, column=6, sticky = W+E+N+S )

        self.btnMazeGrid90 = Button(self.frWindow, text= "90", font=("Calibri", 12))
        self.btnMazeGrid90.grid(row=9, column=7, sticky = W+E+N+S )

        self.btnMazeGrid91 = Button(self.frWindow, text= "91", font=("Calibri", 12))
        self.btnMazeGrid91.grid(row=9, column=8, sticky = W+E+N+S )

        self.btnMazeGrid92 = Button(self.frWindow, text= "92", font=("Calibri", 12))
        self.btnMazeGrid92.grid(row=9, column=9, sticky = W+E+N+S )

        self.btnMazeGrid93 = Button(self.frWindow, text= "93", font=("Calibri", 12))
        self.btnMazeGrid93.grid(row=9, column=10, sticky = W+E+N+S )

        self.btnMazeGrid94 = Button(self.frWindow, text= "94", font=("Calibri", 12))
        self.btnMazeGrid94.grid(row=9, column=11, sticky = W+E+N+S )

        self.btnMazeGrid95 = Button(self.frWindow, text= "95", font=("Calibri", 12))
        self.btnMazeGrid95.grid(row=9, column=12, sticky = W+E+N+S )

        self.btnMazeGrid96 = Button(self.frWindow, text= "96", font=("Calibri", 12))
        self.btnMazeGrid96.grid(row=9, column=13, sticky = W+E+N+S )


        self.frWindow.update()
wdBaseWindow = Tk()
appBasicGUI = GUI(wdBaseWindow)
wdBaseWindow.mainloop()
