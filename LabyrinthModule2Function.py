# Labyrinth Module 2
# Cecily Tighe
# 2016

# contains functionality for Labyrinth Module 2

import xml.etree.ElementTree as ET
import sphero_driver
from Tkinter import *
import time
from displayNames import lstDisplayLBLNames, lblTime
import tkMessageBox

sphero = sphero_driver.Sphero()
#sphero = sphero_driver.Sphero('test', '68:86:E7:02:76:77')

class Functions:
    def __init__(self):
        self.arrMaze = []
        self.bestRoute = []
        # parse xml file
        tree = ET.parse('route.xml')
        for each in tree.findall('cell'):
            self.arrMaze.append(each.text)

        index = 0
        top = []
        left = []
        right = []
        bottom = []
        # the maze is sorted so that barriers are removed and only maze array is left
        print self.arrMaze
        print len(self.arrMaze)
        for eachItem in self.arrMaze:
            # barriers are removed so only 'x''s left are obstacles
            if index < 14:
                top.append(eachItem)
                self.arrMaze.remove(eachItem)
            elif index % 14 == 0:
                left.append(eachItem)
                self.arrMaze.remove(eachItem)
            elif index % 14 == 13:
                right.append(eachItem)
                self.arrMaze.remove(eachItem)
            elif index > 124:
                bottom.append(eachItem)
                self.arrMaze.remove(eachItem)
            index += 1
        print self.arrMaze
        print len(self.arrMaze)
        print 'top', len(top)
        print 'left', len(left)
        print 'right', len(right)
        print 'bottom', len(bottom)

        # route is gathered, sorted and appended to bestRoute
        for eachRoute in tree.findall('route'):
            for eachGrid in eachRoute.findall('grid'):
                eachGrid = eachGrid.text
                self.bestRoute.append(int(eachGrid))
        print self.bestRoute
        index = 0
        for eachCell in self.bestRoute:
            try:
                if self.bestRoute[index] == self.bestRoute[index +1]:
                    self.bestRoute.remove(eachCell)
            except: # the last grid will have no 'next grid'
                pass

            # in the xml file, barriers are included in the grid size, so instead of a 8*12 grid, it becomes a 14*10 grid
            # to overcome this, the magnitude of the grid needs to be lowered according to position in the maze
            if eachCell < 27:
                self.bestRoute[index] = self.bestRoute[index] - 14
            elif eachCell < 41:
                self.bestRoute[index] = self.bestRoute[index] - 16
            elif eachCell < 55:
                self.bestRoute[index] = self.bestRoute[index] - 18
            elif eachCell < 69:
                self.bestRoute[index] = self.bestRoute[index] - 20
            elif eachCell < 83:
                self.bestRoute[index] = self.bestRoute[index] - 22
            elif eachCell < 97:
                self.bestRoute[index] = self.bestRoute[index] - 24
            elif eachCell < 111:
                self.bestRoute[index] = self.bestRoute[index] - 26
            elif eachCell < 125:
                self.bestRoute[index] = self.bestRoute[index] -28
            index += 1

        print self.bestRoute

        self.bestRoute = [1, 2, 3, 4, 5, 17, 29, 41, 42, 43, 55, 67, 79, 91, 92, 93, 94, 95, 96]

        self.arrMaze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 11, 12,
                        'Z', 'Z', 'Z', 0, 0, 0, 'X', 0, 0, 0, 0, 0,
                        'Z', 'Z', 'Z', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        'Z', 'Z', 'Z', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 'X', 0, 0,
                        0, 'Y', 'Y', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 'Y', 'Y', 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # define variable start
        self.startTime = time.time()

        # set the initial value for stop boolean
        self.stop = False

        # how long it takes to cross one (12*8) grid in milliseconds at sphero speed 50 when added to the wait time
        # of the start function
        self.timeOneGrid = 1

        # bestRoute and dictMaze are gathered from xml file
        # bestRoute: list of all of the grids the sphero visits in order of visitation
        # arrMaze: 1d array containing 96 characters representing objects in the maze



        self.ob2 = PhotoImage(file='ob2.gif')
        self.ob3 = PhotoImage(file='ob3.gif')
        self.ob1 = PhotoImage(file='ob1.gif')

        self.leftUp = PhotoImage(file="left_up.gif")
        self.leftDown = PhotoImage(file="left_down.gif")
        self.rightDown = PhotoImage(file='right_down.gif')
        self.rightUp = PhotoImage(file='right_up.gif')
        self.hor = PhotoImage(file='horizontal.gif')
        self.ver = PhotoImage(file='vertical.gif')
        self.start = PhotoImage(file='start.gif')
        self.blank = PhotoImage(file='blank.gif')

        # display is updated with obstacles
        try:
            for i in range(96):
                if self.arrMaze[i] == 'Z':
                    lstDisplayLBLNames[i].config(image=self.ob3)
                    lstDisplayLBLNames[i].image = self.ob3

                elif self.arrMaze[i] == 'Y':
                    lstDisplayLBLNames[i].config(image=self.ob2)
                    lstDisplayLBLNames[i].image = self.ob2

                elif self.arrMaze[i] == 'X':
                    lstDisplayLBLNames[i].config(image=self.ob1)
                    lstDisplayLBLNames[i].image = self.ob1

        except IndexError: # arrMaze is empty
            tkMessageBox.showerror("Error", "The grid seems to be empty, please try again")

        try:
            # the first grid picture is set - start point
            lstDisplayLBLNames[self.bestRoute[0] - 1].config(image=self.start)
            lstDisplayLBLNames[self.bestRoute[0] - 1].image = self.start
        except IndexError:
            tkMessageBox.showerror("No route Found", "There is no route found, please try putting in a route again.")
            
        
    """using bluetooth, the Sphero is checked for a response and a battery level is received
        output: error raised if no response or no battery"""
    def fnSpheroCheck(self):

        """get battery life, response check. if battery is below a certain point, raise error
        """
        #battery = sphero.get_power_state(True)
        #print battery



    """ Upon button 'Start' pressed, route will be calculated and sent to sphero to move
        output: movement of Sphero"""



    def fnSpheroStart(self, bearing):

        print 'sphero start', bearing
        # bluetooth sphero connection is activated
        sphero.connect()

        # raw values set
        sphero.set_filtered_data_strm(40, 1, 0, True)

        #s sphero is ready
        sphero.start()

        #speed = 0.35 m/s

        # set stop to false
        self.stop = False

        """ from the best route, Sphero specific instructions are generated
        input:best route
        output: instructions are sent to and are carried out by Sphero"""

        # set initial time
        self.startTime = time.time()

        # the bearing variable, amount of compensation for roll heading


        index = 0
        #sphero.set_stablization(1, True)
        #sphero.set_heading(0, True)
        for eachStep in self.bestRoute:
            print 'start of loop'
            lstDisplayLBLNames[0].after(600)
            # if stop has been pressed, display ceases updating
            if self.stop == True:
                break

            # make the variables index, eachStep able to be accessed in the display logic function
            self.index = index
            self.eachStep = eachStep

            # if the next grid visited is equal to current grid + 1, then it must be located to the right
            try:
                if self.bestRoute[index + 1] == self.bestRoute[index] + 1:
                    print 'right'
                    sphero.roll(50, bearing, 1, True)
                    self.fnDisplayLogic()

                # if the next grid visited is equal to current grid + 1, then it must be located to the left
                elif self.bestRoute[index + 1] == self.bestRoute[index] - 1:
                    if bearing + 180 >= 360:
                        bearing = bearing - 360

                        print bearing + 180
                        print bearing #global
                    sphero.roll(50, bearing + 180, 1, True)
                    print 'left'
                    self.fnDisplayLogic()

                # if the next grid visited is equal to current grid + 12, then it must be located downwards
                elif self.bestRoute[index + 1] == self.bestRoute[index] - 12:
                    if bearing + 270 >= 360:
                        bearing = bearing - 360
                    sphero.roll(50, bearing + 270, 1, True)
                    print 'up'
                    self.fnDisplayLogic()

                # if the next grid visited is not equal to any of the earlier options, it must be located upwards
                elif self.bestRoute[index + 1] == self.bestRoute[index] + 12:
                    if bearing +90 >= 360:
                        bearing = bearing - 360
                    sphero.roll(50, bearing + 90, 1, True)
                    print 'down'
                    self.fnDisplayLogic()

            # the end of the route
            except IndexError:
                self.fnDisplayLogic()
                sphero.roll(0,0,0,True)

            # time delay

            lstDisplayLBLNames[0].after(self.timeOneGrid)
            print "#####"
            index += 1

    # stops the movement of the sphero
    def fnSpheroStop(self):
        # clears the display of route
        for eachGrid in self.bestRoute:
            # start image is already set so it is skipped in the blanking process
            if self.bestRoute[0] == eachGrid:
                pass
            else:
                lstDisplayLBLNames[eachGrid - 1].config(image=self.blank)
                lstDisplayLBLNames[eachGrid - 1].image = self.blank
                
        # if the route wen through an obstacle, obstacle images would disappear so they need to be recreated
            for i in range(96):
                if self.arrMaze[i] == 'Z':
                    lstDisplayLBLNames[i].config(image=self.ob3)
                    lstDisplayLBLNames[i].image = self.ob3

                elif self.arrMaze[i] == 'Y':
                    lstDisplayLBLNames[i].config(image=self.ob2)
                    lstDisplayLBLNames[i].image = self.ob2

                elif self.arrMaze[i] == 'X':
                    lstDisplayLBLNames[i].config(image=self.ob1)
                    lstDisplayLBLNames[i].image = self.ob1
                    
        # set the stop boolean to true
        self.stop = True

        # disconnect from sphero via bluetooth
        sphero.disconnect()

        
        # clear time elapsed label
        lblTime[0].config(text = "00:00")

# in simulation mode, only display logic is called as there is no control of sphero
    def fnUpdateDisplay(self):

        # set stop to false
        self.stop = False

        # set initial time
        self.startTime = time.time()

        # using list of pictures to replicate route, wait amount of seconds, display the next picture
        index = -1
        for eachStep in self.bestRoute:
            index += 1

            # if stop has been pressed, display ceases updating
            if self.stop == True:
                break

            # time delay
            lstDisplayLBLNames[0].after(500)

            # initial grid is already set so this is skipped
            if index == 0:
                continue

            # make the variable able to be accessed in the display logic function
            self.index = index
            self.eachStep = eachStep

            # call the display logic function to place correct image into the current grid
            self.fnDisplayLogic()

# here is the logic statements to determine which image to display in which grid to replicate the route
    def fnDisplayLogic(self):
        try:
            # update the time elapsed display
            nowTime = time.time()
            # calculate seconds passed since start was initially pressed
            timeElapsed = nowTime - self.startTime
            # display the difference in time
            lblTime[0].config(text=round(timeElapsed, 2))

            # last grid is to the left of the current grid
            if self.bestRoute[self.index - 1] == self.bestRoute[self.index] - 1:
                # next grid is above current grid but last grid was to the left
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftUp

                # next grid is below current grid but last grid was the left
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftDown

                # next grid is to the right of the current grid but last grid was to the left
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.hor)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.hor

            # last grid is to the right of the current grid
            elif self.bestRoute[self.index - 1] == self.bestRoute[self.index] + 1:
                # next grid is above the current grid but last grid was to the right
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightUp

                # next grid is below the current grid but last grid was to the right
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightDown

                # last grid was to the right and next grid is to the left of the current grid
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.hor)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.hor

            # last grid is above of the current grid
            elif self.bestRoute[self.index - 1] == self.bestRoute[self.index] - 12:
                # next grid is to the left of current grid, last grid was above current grid
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftUp

                # next grid is to the right of current grid, last grid was above current grid
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightUp

                # next grid is below current grid, last grid was above current grid
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.ver)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.ver

            # last grid is below the current grid
            elif self.bestRoute[self.index - 1] == self.bestRoute[self.index] + 12:
                # next grid is to the left of current grid, last grid was below current grid
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightDown

                    # next grid is to the right of current grid, last grid was below
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftDown

                # next grid is above of current grid, last grid was below current grid
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.ver)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.ver

        # there is no 'next grid'- current grid is the end route
        except IndexError:
            # init = PhotoImage(file = 'start.gif')
            lstDisplayLBLNames[self.eachStep - 1].config(image=self.start)
            lstDisplayLBLNames[self.eachStep - 1].image = self.start

        # update the window
        lstDisplayLBLNames[2].update()
