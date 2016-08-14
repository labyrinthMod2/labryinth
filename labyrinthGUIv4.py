
# Eleni Cook, 2016
# This is a GUI for the program 

from Tkinter import *

from PIL import Image, ImageTk

from functools import partial

import tkMessageBox

import labyrinthFunctions
Lab = labyrinthFunctions.Functions()

from buttonNames import listBtnName

class Module1GUI():

   
    # this displays the first module of the labyrinth program
    def displayWindowOne(self):
        self.tlOne = Toplevel(bd=0, highlightthickness=0)
        self.tlOne.rowconfigure(0, weight=1)
        self.tlOne.columnconfigure(0, weight=1)
        self.cvOne = Canvas(self.tlOne, bd=0, highlightthickness=0, bg = "#b3c9d1")
        self.cvOne.grid(row=0, column=0, sticky=N+S+E+W)
        self.frmWindowOne = Frame(self.cvOne, bg ="#b3c9d1")
        self.tlOne.title("Labyrinth")
        self.tlOne.minsize(700, 450)
        self.frmWindowOne.pack(fill= BOTH, expand =1)
        self.tlOne.resizable(0,0)
        self.frmWindowOne.grid()



        #set the default image for the maze
        self.blank = PhotoImage(file = 'white.gif')
        size = 55,55

        # transparent photo
        imTransparent = Image.open("transparent.png")
        imTransparent.thumbnail(size, Image.ANTIALIAS)
        photoTransparent = ImageTk.PhotoImage(imTransparent)

        # image of the waypoint
        imFlag = Image.open("flag.png")
        imFlag.thumbnail(size, Image.ANTIALIAS)
        photoFlag = ImageTk.PhotoImage(imTransparent)

        # image of the barriers
        imBarriers = Image.open("mountain.png")
        imBarriers.thumbnail(size, Image.ANTIALIAS)
        photoBarriers = ImageTk.PhotoImage(imBarriers)

        imBackgroud=Image.open("background.gif")
        imBackgroud.thumbnail(size, Image.ANTIALIAS)
        photoBackground = ImageTk.PhotoImage(imBackgroud)



        #background image
        background_image=PhotoImage(file = 'background.gif')
        background_label = Label(self.frmWindowOne, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image


        # empty labels which are for spacing
        self.lblEmpty1 = Label(self.frmWindowOne, bg ="black")
        self.lblEmpty1.grid(row =0)

        self.lblEmpty5 = Label(self.frmWindowOne, bg="black" )
        self.lblEmpty5.grid(row =6)

        self.lblEmpty2 = Label(self.frmWindowOne, bg="black", width = 2,)
        self.lblEmpty2.grid(column = 0)

        self.lblEmpty3 = Label(self.frmWindowOne, width = 2, bg= "black")
        self.lblEmpty3.grid(column = 1)

        self.lblEmpty4 = Label(self.frmWindowOne, width = 2, bg ="black")
        self.lblEmpty4.grid(column = 14, row =6)


        # this is a list of RadioButtons for the user to create the maze
        option = IntVar()

        """self.lbltitle = Label(self.frmWindowOne, text="Select an Option and Press a Cell to Create the Maze", font=("Calibri", 12,"bold" )

                              ,bg="white", fg="black")"""

        self.lblSelect = Label(self.frmWindowOne, text= "Options:", font=("Calibri", 12,"bold" ),bg="white", fg="black")
        self.lblSelect.grid(row =3, column = 1, sticky = W+E+S+N)

        self.rbAddWayPoints =Radiobutton(self.frmWindowOne, text="Add Waypoints", variable=option, value=1, font=("Calibri", 12), indicatoron=0,command=Lab.fnAddWaypoints )
        self.rbAddWayPoints.grid(row =4, column =1, sticky = W+E+S+N)

        self.rbDeleteWayPoints= Radiobutton(self.frmWindowOne, text="Delete Waypoints", variable=option, value=2, font=("Calibri", 12,), indicatoron=0, command= Lab.fnDeleteWayPoint)
        self.rbDeleteWayPoints.grid(row =5, column =1, sticky = W+E+S+N)

        self.rbAddBarriers= Radiobutton(self.frmWindowOne, text="Add Barriers", variable=option, value=3, font=("Calibri", 12, ), indicatoron=0,command= Lab.fnAddBarriers)
        self.rbAddBarriers.grid(row =6, column =1, sticky = W+E+S+N)

        self.rbDeleteBarriers= Radiobutton(self.frmWindowOne, text="Delete Barriers", variable=option, value=4, font=("Calibri", 12, ), indicatoron=0, command= Lab.fnDeleteBarriers)
        self.rbDeleteBarriers.grid(row =7, column =1, sticky = W+E+S+N)



        self.btnReset= Button(self.frmWindowOne, text="Reset Maze", font=("Calibri", 12, ), command= Lab.fnResetMaze)
        self.btnReset.grid(row =8, column =1, sticky = W+E+S+N)



# solve button calls a funtion to find all the possible routes
        self.btnSolve = Button(self.frmWindowOne, text=" Solve",font=("Calibri", 12), bg ="white", command=labyrinthFunctions.fnSaveMaze)
        self.btnSolve.grid(row=10, column=3, sticky =N+S+W+E)

# quit button
        self.btnQuit = Button(self.frmWindowOne, text=" Quit", font=("Calibri", 12),)
        self.btnQuit.grid(row=10, column=13,sticky = E+W+S+N)


    #  this is a list of numbers for the buttons
        listBtnNum = []

        # this loop creates the numbers the add to the list of numbers
        for btnNum in range(96):
            listBtnNum.append(btnNum)


       # this index used to find the button from the list of button names
        index = 0

        # this loop creates the buttons in the GUI
        for x in range(8):
            for y in range (12):
                # it first has a loop of x and y coordinates for the buttons

                # number is used to pass into one of the functions
                number = listBtnNum[index]

                # this creates the buttons
                listBtnName[index] = Button(self.frmWindowOne,font =("Calibri,", 12) , width=4, height=2, anchor=CENTER, bg= "white" )
                listBtnName[index].configure(command = partial(Lab.fnCreateMaze,number))
                listBtnName[index].grid(row=x+2, column = y+3,sticky =E)
                index = index + 1
        
        
        self.frmWindowOne.update()
    
        
    def __init__(self, master=None):

        master.withdraw()

        
        self.displayWindowOne()    

        master.mainloop()


        

        

wdBaseWindow = Tk()
appBasicGUI = Module1GUI(wdBaseWindow)
wdBaseWindow.mainloop()
