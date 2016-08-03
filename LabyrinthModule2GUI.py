# Labyrinth Module 2 GUI
# Cecily Tighe
# 2016

# contains display and small display related functions

from Tkinter import *
from displayNames import lstDisplayLBLNames
import LabyrinthModule2Function
import time

fn = LabyrinthModule2Function.Functions()


class GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Labyrinth Maze Solve")
        self.master.minsize(700, 550)
        self.master.maxsize(700, 550)
        self.fnCreateWidgets()

        lstDisplayLBLNames = []

#define the names of the labels that are used in both files and make them global


    def fnCreateWidgets(self):
        # set background color
        bg = '#b3c9d1'
        #set the default image for the display
        self.blank = PhotoImage(file = 'blank.gif')
        # set the font for the whole GUI
        font = 'Calibri'
        # Bold Font size, set fontsize for headings + buttons
        BfontSize = 16
        # set basic fontsize
        fontSize = 12
        # create the list of names for the labels in the display


        # create the frame
        self.frWindow = Frame(height=400, width=500, bg=bg)
        self.frWindow.pack(fill=BOTH, expand=1)

        #background image
        background_image=PhotoImage(file = 'background.gif')
        background_label = Label(self.frWindow, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        #menu bar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu = Menu(menubar)
        fileMenu.add_command(label='Return to Route Plotter', command=self.fnReturnModule1)
        fileMenu.add_command(label="Quit", command = self.fnQuit)
        menubar.add_cascade(label="File", menu=fileMenu)
        wdBaseWindow.config(menu=menubar)

        # label, will display the Sphero runtime
        self.lblTime = Label(self.frWindow, text = 'Time:')
        self.lblTime.grid(row=1, column =10, pady = (20,10))

        self.lblTimeElapsed = Label(self.frWindow, text='00:00')
        self.lblTimeElapsed.grid(row=1, column=11, pady=(20, 10))

        # button, starts the run
        self.btnStart = Button(self.frWindow, text="Start", command =self.fnStart,font=(font,16))
        self.btnStart.grid(row=10, column=3,columnspan=2, pady = (10,0))

        # button, stops the run completely - NOT pause
        self.btnStop = Button(self.frWindow, text="Stop", font=(font,16))
        self.btnStop.grid(row=10, column=10, columnspan =2, pady = (10,0))

        """DISPLAY Grid Arrangement:
        4x6

               0  1   2  3   4  5 ... 12
            0 |X||X| |X||X| |X||X|
            1 |X||X| |X||X| |X||X|

            2 |X||X| |X||X| |X||X|
            3 |X||X| |X||X| |X||X|
            ...8
        Labels that hold images of different route combinations

        Naming:
        Row 1, comumn 1 = disp00
        Row 2, column 4 = disp24
        etc.
        """
        # this loop creates the names of the image labels
        for each in range(96):
            #first the individual names are created and appended to the list 'lstDisplayLBLNames'
            if each < 12:
                name = 'disp' + '0' +str(each)
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
            print name

            # the list is used to create a set of labels
            lstDisplayLBLNames[each] = Label(self.frWindow,image = self.blank, width=47, height=47, relief = SUNKEN)

            # a length checker is necessary as labels in the 12th row are have 3 digits in their name
            # a length checker is necessary as labels in the 12th row are have 3 digits in their name
            if len(name) == 6:
                lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, padx=(1, 1), pady=(1, 1))
                if int(name[-1]) == 0:
                    lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, padx=(25, 1), pady=(1, 1))
            else:
                lstDisplayLBLNames[each].grid(row=int(name[-3]) + 2, column=int(name[-1]) + 12, padx=(1, 1), pady=(1, 1))



        self.frWindow.update()

# quits program, closes window
    def fnQuit(self):
        self.frWindow.destroy()
        self.master.destroy()

# when return is selected in menubar, the window closes and module 1 is opened
    def fnReturnModule1(self):
        pass

    def fnTimeElapsed(self):
        # starts the timer displayed in the time elapsed label

        now = time.time()
        time_elapsed = now - start
        self.lblTimeElapsed.config(text=round(time_elapsed,2))

        wdBaseWindow.update()

        

    def fnStart(self):
        # call the sphero start command in the functions file
        fn.fnUpdateDisplay()

        start = time.time()
        global start
        wdBaseWindow.after(1000, self.fnTimeElapsed)
        


wdBaseWindow = Tk()
appBasicGUI = GUI(wdBaseWindow)
wdBaseWindow.mainloop()

