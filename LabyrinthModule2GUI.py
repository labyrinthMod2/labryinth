# Labyrinth Module 2 GUI
# Cecily Tighe
# 2016

# contains display and small display related functions

from displayNames import lstDisplayLBLNames, lblTime
import LabyrinthModule2Function
import time
from Tkinter import *
import tkMessageBox
wdBaseWindow = Tk()



class GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Labyrinth Maze Solve")
        self.master.minsize(700, 550)
        self.master.maxsize(700, 550)
        self.fnCreateWidgets()


    def fnCreateWidgets(self):

        self.mode = StringVar()
        self.mode.set("Sphero Control")

        #set the default image for the display
        self.blank = PhotoImage(file = 'blank.gif')
        # set the font for the whole GUI
        font = 'Calibri'

        # create the frame
        self.frWindow = Frame(height=400, width=500)
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

        # label 'mode'
        self.lblMode = Label(self.frWindow, text='Mode:')
        self.lblMode.grid(row=1, column=2, columnspan =2,padx=(20, 0), pady = (20,10))

        #optionbox for simulation / sphero control modes
        self.optMenu = OptionMenu(self.frWindow, self.mode, "Simulation", "Sphero Control")
        self.optMenu.grid(row = 1,columnspan = 4 ,column = 3,pady = (20,10))

        # label, will display the Sphero runtime
        self.lblTime = Label(self.frWindow, text = 'Time:')
        self.lblTime.grid(row=1, column =10, pady = (20,10))

        lblTime[0] = Label(self.frWindow, text='00:00')
        lblTime[0].grid(row=1, column=11, pady=(20, 10))

        # button, starts the run

        self.btnStart = Button(self.frWindow, text="Start", command =self.fnStart,font=(font,16))
        self.btnStart.grid(row=10, column=3,columnspan=2, pady = (10,0))

        # button, stops the run completely - NOT pause
        self.btnStop = Button(self.frWindow, text="Stop", command = self.fnStop,font=(font,16))
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

            # the list is used to create a set of labels
            lstDisplayLBLNames[each] = Label(self.frWindow,image = self.blank, width=47, height=47, relief = SUNKEN)

            # a length checker is necessary as labels in the 12th row are have 3 digits in their name
            if len(name) == 6:
                lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2)
                if int(name[-1]) == 0:
                    lstDisplayLBLNames[each].grid(row=int(name[-2]) + 2, column=int(name[-1]) + 2, padx=(25, 0))
            else:
                lstDisplayLBLNames[each].grid(row=int(name[-3]) + 2, column=int(name[-1]) + 12)

        self.frWindow.update()
        self.fn = LabyrinthModule2Function.Functions()

# quits program, closes window
    def fnQuit(self):
        self.frWindow.destroy()
        self.master.destroy()

# calls the function stop, stops the display and disconnects from Sphero
    def fnStop(self):
        self.stop = True
        self.fn.fnSpheroStop()

# when return is selected in menubar, the window closes and module 1 is opened
    def fnReturnModule1(self):
        pass

    def fnStart(self):

        # calls a different function depending on the mode selected
        if self.mode.get() == "Sphero Control":
            tkMessageBox.showinfo("Sphero Check","Please ensure that your Sphero is on and placed in the centre of the start of the maze facing forwards.")
            self.fn.fnSpheroStart()
        elif self.mode.get() == "Simulation":
            self.fn.fnUpdateDisplay()

appBasicGUI = GUI(wdBaseWindow)
wdBaseWindow.mainloop()

