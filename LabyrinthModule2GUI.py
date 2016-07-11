# Labyrinth Module 2 GUI
# Cecily Tighe
# 2016

from Tkinter import *


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Labyrinth Maze Solve")
        self.master.minsize(700, 550)
        self.fnCreateWidgets()

    def fnCreateWidgets(self):
        # set background color
        bg = '#ccccff'
        #set the default image for the display
        self.blank = PhotoImage(file = 'blank.gif')
        # set the font for the whole GUI
        font = 'Calibri'
        # Bold Font size, set fontsize for headings + buttons
        BfontSize = 16
        # set basic fontsize
        fontSize = 12
        # create the list of names for the labels in the display
        self.lstDisplayLBLNames = []

        # create the frame
        self.frWindow = Frame(height=400, width=500, bg=bg)
        self.frWindow.pack(fill=BOTH, expand=1)

        #menu bar
        #self.menubar = Menu(self)
        #menu = Menu(self.menubar, tearoff=0)
        #self.menubar.add_cascade(label="Labyrinth", menu=menu)
        #menu.add_command(label="Return")
        #menu.add_command(label="Quit")

        # show the menubar
        #self.master.config(menu=self.menubar)

        # blank labels for spacing
        self.lbl1 = Label(self.frWindow, bg = bg)
        self.lbl1.grid(row =0)

        self.lbl2 = Label(self.frWindow, width = 2, bg =bg)
        self.lbl2.grid(column = 0)

        # label, will display the Sphero runtime
        self.lblTimeElapsed = Label(self.frWindow, text = 'Time:')
        self.lblTimeElapsed.grid(row=1, column =6)

        # button, starts the run
        self.btnStart = Button(self.frWindow, text="Start", font=(font,16))
        self.btnStart.grid(row=6, column=1)

        # button, stops the run completely - NOT pause
        self.btnStop = Button(self.frWindow, text="Stop", font=(font,16))
        self.btnStop.grid(row=7, column=1)

        """DISPLAY Grid Arrangement:
        4x6
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
        for each in range(24):
            #first the individual names are created and appended to the list 'lstDisplayLBLNames'
            if each < 6:
                name = 'disp' + '0' +str(each)
            elif each <12:
                name = 'disp' + '1' + str(each - 6)
            elif each < 18:
                name = 'disp' + '2' + str(each - 12)
            else:
                name = 'disp' + '3' + str(each - 18)

            self.lstDisplayLBLNames.append(name)

            # the list is used to create a set of labels
            self.lstDisplayLBLNames[each] = Label(self.frWindow, image=self.blank, width=80, height=80, relief=SUNKEN)

            # every second column has x direction padding to easily see which sector the Sphero is located in
            if (int(name[-1]) + 1)  % 2 == 0:
                self.lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, padx = (1,7.5))
            # every label in the second row has padding on the bottom to created 3 clear sectors
            if int(name[-2]) == 1:
                self.lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, pady=(1, 7.5))
            # labels not in columns 1 or 3 or in the second row are simply given a grid position
            else:
                self.lstDisplayLBLNames[each].grid(row = int(name[-2]) + 2, column= int(name[-1]) + 2)




        self.frWindow.update()
wdBaseWindow = Tk()
appBasicGUI = GUI(wdBaseWindow)
wdBaseWindow.mainloop()