# Labyrinth Module 2
# Cecily Tighe
# 2016

#contains most of the functionality

import xml.etree.ElementTree as ET
import time
#import sphero_driver
from Tkinter import *
from displayNames import lstDisplayLBLNames

#sphero = sphero_driver.Sphero()

class Functions:
    def __init__(self):

        # bestRoute and dictMaze are gathered from xml file
        # bestRoute: list of all of the grids the sphero visits in order of visitation
        # arrMaze: 1d array containing 96 characters representing objects in the maze
        self.bestRoute = [1, 2, 3, 4, 5, 17, 29, 41, 42, 43, 55, 67, 79, 91, 92, 93, 94, 95, 96]

        self.arrMaze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 11, 12,
                        'Z', 'Z', 'Z', 0, 0, 0, 'X', 0, 0, 0, 0, 0,
                        'Z', 'Z', 'Z', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        'Z', 'Z', 'Z', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 'X', 0, 0,
                        0, 'Y', 'Y', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 'Y', 'Y', 0, 0, 0, 0, 0, 0, 0, 0, 0]

        ob2 = PhotoImage(file='ob2.gif')
        ob3 = PhotoImage(file='ob3.gif')
        ob1 = PhotoImage(file='ob1.gif')

        self.leftUp = PhotoImage(file="left_up.gif")
        self.leftDown = PhotoImage(file="left_down.gif")
        self.rightDown = PhotoImage(file='right_down.gif')
        self.rightUp = PhotoImage(file='right_up.gif')
        self.hor = PhotoImage(file='horizontal.gif')
        self.ver = PhotoImage(file='vertical.gif')
        self.start = PhotoImage(file='start.gif')

        # display is updated with obstacles
        for i in range(96):
            print self.arrMaze[i]
            if self.arrMaze[i] == 'Z':
                lstDisplayLBLNames[i].config(image=ob3)
                lstDisplayLBLNames[i].image = ob3

            elif self.arrMaze[i] == 'Y':
                lstDisplayLBLNames[i].config(image=ob2)
                lstDisplayLBLNames[i].image = ob2

            elif self.arrMaze[i] == 'X':
                lstDisplayLBLNames[i].config(image=ob1)
                lstDisplayLBLNames[i].image = ob1

        # the first grid picture is set - start point
        lstDisplayLBLNames[self.bestRoute[0] - 1].config(image=self.start)
        lstDisplayLBLNames[self.bestRoute[0] - 1].image = self.start




    """using bluetooth, the Sphero is checked for a response and a battery level is received
        output: error raised if no response or no battery"""
    def fnSpheroCheck(self):

        """get battery life, response check. if battery is below a certain point, raise error
        """
        #battery = sphero.get_power_state(True)
        #print battery



    """ Upon button 'Start' pressed, route will be calculated and sent to sphero to move
        output: movement of Sphero"""
    def fnSpheroStart(self):

        # bluetooth sphero connection is activated
        #sphero.connect()

        # raw values set
        #sphero.set_filtered_data_strm(40, 1, 0, True)

        #s sphero is ready
        #sphero.start()

        speed = 0.35
        time_one_grid = 0.125

        #bestRoute = visited points

        """ from the best route, Sphero specific instructions are generated
        input:best route
        output: instructions are sent to and are carried out by Sphero"""

        # set heading to zero to ensure orientation is correct
        # sphero.set_heading(self, heading, response)

        index = 0

        for eachStep in self.bestRoute:

            # if the next grid visited is equal to current grid + 1, then it must be located to the right
            try:
                if self.bestRoute[index + 1] == self.bestRoute[index] + 1:
                    print 'right'
                    # sphero.roll(50, 0, 1, True)

                # if the next grid visited is equal to current grid + 1, then it must be located to the left
                elif self.bestRoute[index + 1] == self.bestRoute[index] - 1:
                    # sphero.roll(50, 180, 1, True)
                    print 'left'

                # if the next grid visited is equal to current grid + 12, then it must be located downwards
                elif self.bestRoute[index + 1] == self.bestRoute[index] - 12:
                    # sphero.roll(50, 270, 1, True)
                    print 'up'

                # if the next grid visited is not equal to any of the earlier options, it must be located upwards
                elif self.bestRoute[index + 1] == self.bestRoute[index] + 12:
                    # sphero.roll(50, 270, 1, True)
                    print 'down'

            # the end of the route
            except IndexError:
                pass
            index += 1
            self.fnUpdateDisplay()



            
    # stops the movement of the sphero
    def fnSpheroStop(self):
        """also stop display"""
        #sphero.disconnect(self)


    """upon mouse click 'start', uses an arrangement of pictures to replicate the route the Sphero is following
        input: best route instructions
        output: display is updated"""

    def fnUpdateDisplay(self):

        # using list of pictures to replicate route, wait amount of seconds, display the next picture
        index = -1
        for eachStep in self.bestRoute:
            index += 1
            lstDisplayLBLNames[0].after(1000)

            try:
                # the first grid is already set so is ignored in the loop
                if index == 0:
                    continue

                # last grid is to the left of the current grid
                if self.bestRoute[index - 1] == self.bestRoute[index] - 1:
                    # next grid is above current grid but last grid was to the left
                    if self.bestRoute[index + 1] == self.bestRoute[index] - 12:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.leftUp)
                        lstDisplayLBLNames[eachStep - 1].image = self.leftUp

                    # next grid is below current grid but last grid was the left
                    elif self.bestRoute[index + 1] == self.bestRoute[index] + 12:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.leftDown)
                        lstDisplayLBLNames[eachStep - 1].image = self.leftDown

                    # next grid is to the right of the current grid but last grid was to the left
                    elif self.bestRoute[index + 1] == self.bestRoute[index] + 1:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.hor)
                        lstDisplayLBLNames[eachStep - 1].image = self.hor

                # last grid is to the right of the current grid
                elif self.bestRoute[index - 1] == self.bestRoute[index] + 1:
                    # next grid is above the current grid but last grid was to the right
                    if self.bestRoute[index + 1] == self.bestRoute[index] - 12:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.rightUp)
                        lstDisplayLBLNames[eachStep - 1].image = self.rightUp

                    # next grid is below the current grid but last grid was to the right
                    elif self.bestRoute[index + 1] == self.bestRoute[index] + 12:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.rightDown)
                        lstDisplayLBLNames[eachStep - 1].image = self.rightDown

                    # last grid was to the right and next grid is to the left of the current grid
                    elif self.bestRoute[index + 1] == self.bestRoute[index] - 1:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.hor)
                        lstDisplayLBLNames[eachStep - 1].image = self.hor

                # last grid is above of the current grid
                elif self.bestRoute[index - 1] == self.bestRoute[index] - 12:
                    # next grid is to the left of current grid, last grid was above current grid
                    if self.bestRoute[index + 1] == self.bestRoute[index] - 1:
                        lstDisplayLBLNames[eachStep -1].config(image = self.leftUp)
                        lstDisplayLBLNames[eachStep - 1].image = self.leftUp

                    # next grid is to the right of current grid, last grid was above current grid
                    elif self.bestRoute[index + 1] == self.bestRoute[index] + 1:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.rightUp)
                        lstDisplayLBLNames[eachStep - 1].image = self.rightUp

                    # next grid is below current grid, last grid was above current grid
                    elif self.bestRoute[index + 1] == self.bestRoute[index] + 12:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.ver)
                        lstDisplayLBLNames[eachStep - 1].image = self.ver

                # last grid is below the current grid
                elif self.bestRoute[index - 1] == self.bestRoute[index] + 12:
                    # next grid is to the left of current grid, last grid was below current grid
                    if self.bestRoute[index + 1] == self.bestRoute[index] + 1:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.leftDown)
                        lstDisplayLBLNames[eachStep - 1].image = self.leftDown

                        # next grid is to the right of current grid, last grid was below
                    if self.bestRoute[index + 1] == self.bestRoute[index] - 1:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.rightDown)
                        lstDisplayLBLNames[eachStep - 1].image = self.rightDown

                    # next grid is above of current grid, last grid was below current grid
                    elif self.bestRoute[index + 1] == self.bestRoute[index] - 12:
                        lstDisplayLBLNames[eachStep - 1].config(image=self.ver)
                        lstDisplayLBLNames[eachStep - 1].image = self.ver

            # there is no 'next grid'- current grid is the end route
            except IndexError:
                # init = PhotoImage(file = 'start.gif')
                lstDisplayLBLNames[eachStep - 1].config(image=self.start)
                lstDisplayLBLNames[eachStep - 1].image = self.start
            lstDisplayLBLNames[2].update()

