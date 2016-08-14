# Labyrinth Module 2 GUI
# Cecily Tighe
# 2016

# contains display and small display related functions

from displayNames import lstDisplayLBLNames, lblTime, lblStatusUpdate
from Tkinter import *
import sphero_driver
import tkMessageBox
import LabyrinthModule2Function

sphero = sphero_driver.Sphero()
wdBaseWindow = Tk()



class GUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Labyrinth Maze Solve")
        self.master.minsize(700, 550)
        self.master.maxsize(700, 550)
        self.mode = StringVar()
        self.slide = IntVar()
        self.status = StringVar()
        self.fnCreateWidgets()

    def fnCreateWidgets(self):

        self.status = ''
        self.mode.set("Sphero Control")

        #set the default image for the display
        self.blank = PhotoImage(file = 'blank.gif')
        # set the font for the whole GUI
        font = 'Calibri'

        # create the frame
        self.frWindow = Frame(height=400, width=500,bg ="#b3c9d1")
        self.frWindow.pack(fill=BOTH, expand=1)

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

        #the label to hold status messages
        lblStatusUpdate[0] = Label(self.frWindow,anchor = W, text=self.status, bg='white', fg='black', width = 80)
        lblStatusUpdate[0].grid(row = 11,columnspan = 30,sticky = E +W,  pady = (5,0))

        lblStatusExtend = Label(self.frWindow, width = 8,bg = 'white')
        lblStatusExtend.grid(row=11, column = 16, sticky = W, pady=(5, 0))

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
            self.fnSetHeadingWindow()
        elif self.mode.get() == "Simulation":
            self.fn.fnUpdateDisplay()


# create the set heading window
    def fnSetHeadingWindow(self):
        # message box to show status
        lblStatusUpdate[0].config(text ='Connecting to Sphero...')
        self.frWindow.update()
        try:
            # bluetooth sphero connection is activated
            sphero.connect()
            # raw values set
            sphero.set_filtered_data_strm(40, 1, 0, True)
            # sphero is ready
            sphero.start()
            # notify user of connection success
            lblStatusUpdate[0].config(text='Sphero connection successful')
            #update the window to display the status update
            self.frWindow.update()

            self.setHeadingWindow = Toplevel()
            self.setHeadingWindow.wm_title("Set Heading")

            # create the widgets to go inside the new window
            # lblInfo contains instructions on how to operate the set heading operation
            lblInfo = Label(self.setHeadingWindow, text="Press roll to roll sphero and adjust its bearing using the slider", font = ('Calibri', 12))
            lblInfo.grid(row = 1, column = 1, padx = (10,10), pady = (20,20))

            # bearing slider is the entry for the amount of compensation to provide so that the Sphero is
            # facing the correct way.
            self.bearingSlider = Scale(self.setHeadingWindow, to=359, orient=HORIZONTAL, length = 200)
            self.bearingSlider.grid(row=2, column=1, columnspan=4)

            # button roll makes the Sphero roll at native bearing zero for one second so that the user can identify
            # how many degrees away from the desired orientation the sphero native is
            self.btnBearingRoll = Button(self.setHeadingWindow, text = "Roll", command = lambda:
                self.fnBearingRoll(self.bearingSlider.get()), font=('Calibri',14))
            self.btnBearingRoll.grid(row = 3, column =1, padx=(20,200), pady = (10,10))

            # when button continue is pressed, sphero is disconnected, then fnSpheroStart in LabyrinthModule2Function is called
            self.btnContinue = Button(self.setHeadingWindow, text="Continue", command=lambda :self.fnContinue(self.bearingSlider.get()), font=('Calibri', 14))
            self.btnContinue.grid(row=3, column=1, padx = (200,20), pady = (10,10))

        # if there is a bluetooth error
        except (IOError, RuntimeError, AttributeError):
            # ask user if they would like to attempt the connection again
            attemptAgain = tkMessageBox.askyesno("Sphero Connection", "Connection Failure. Retry Connection?")
            if attemptAgain is True: # user would like to attempt again
                self.fnSetHeadingWindow()
            else: # user does not want to attempt again
                # clear status bar; no processes going on
                lblStatusUpdate[0].config(text = '')

    def fnBearingRoll(self, bearing):
        # roll at bearing of slider for 2 seconds
        sphero.roll(50, bearing, 1, True)
        lstDisplayLBLNames[0].after(2000)
        # stop roll
        sphero.roll(0,0,0,True)

    def fnContinue(self, bearing):
        # disconnect from sphero as bluetooth connection cannot be carried over to another file
        self.setHeadingWindow.destroy()
        sphero.disconnect()

        # clear status bar
        lblStatusUpdate[0].config(text='')
        self.frWindow.update()

        # call the sphero start function with the argument bearing being the value chosen on the bearing slider
        # bearing : int,  0-359 degrees
        self.fn.fnSpheroStart(bearing)

appBasicGUI = GUI(wdBaseWindow)
wdBaseWindow.mainloop()