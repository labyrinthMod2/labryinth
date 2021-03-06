# Labyrinth Module 2
# Cecily Tighe
# 2016

# contains functionality for Labyrinth Module 2

import xml.etree.ElementTree as ET
import sphero_driver
from Tkinter import *
import time
from displayNames import lstDisplayLBLNames, lblTime, lblStatusUpdate
import tkMessageBox

sphero = sphero_driver.Sphero()

class Functions:
    def __init__(self):
        self.arrMaze = []
        self.bestRoute = []
        # parse xml file
        tree = ET.parse('route.xml')
        # bestRoute and dictMaze are gathered from xml file
        # bestRoute: list of all of the grids the sphero visits in order of visitation
        # arrMaze: 1d array containing 96 characters representing objects in the maze

        # self.arrMaze is gathered from the xml file
        index = 0
        # because the maze array in the xml file has barriers, these need to be removed
        # to format the array for display
        for each in tree.findall('cell'):
            index += 1
            # the first row is not used
            if index < 15:
                continue
            # the last row is not used
            elif index > 126:
                continue
            # the right row is not used
            elif index % 14 == 0:
                continue
            # the left row is not used
            elif index % 14 == 1:
                continue
            # the actual grids are placed in the arrMaze array
            else:
                self.arrMaze.append(each.text)
        # bestRoute is gathered from the xml file
        for eachRoute in tree.findall('route'):
            for eachCell in eachRoute.findall('grid'):
                eachCell = int(eachCell.text) + 1

                # in the xml file, barriers are included in the grid size,
                #  so instead of a 8*12 grid, it becomes a 14*10 grid
                # to overcome this, the magnitude of the grid needs to be lowered according to position in the maze
                if eachCell < 28:
                    eachCell -= 15
                elif eachCell < 42:
                    eachCell -= 17
                elif eachCell < 56:
                    eachCell -= 19
                elif eachCell < 70:
                    eachCell -= 21
                elif eachCell < 84:
                    eachCell -= 23
                elif eachCell < 98:
                    eachCell -= 25
                elif eachCell < 112:
                    eachCell -= 27
                elif eachCell < 126:
                    eachCell -= 30
                self.bestRoute.append(eachCell)

        # some of the grid values in the xml path may be repeated due to individual paths being
        # calculated for each waypoint so these need to be removed to insure the display will work
        index = 0
        for eachCell in self.bestRoute:
            try:
                # if the next grid is the same as the current grid, remove it from bestRoute
                if self.bestRoute[index] == self.bestRoute[index +1]:
                    self.bestRoute.remove(eachCell)
            except IndexError:  # the last grid will have no 'next grid'
                pass
            index += 1

        # define variable start
        self.startTime = time.time()

        # set the initial value for stop boolean
        self.stop = False

        # how long it takes to cross one (12*8) grid in milliseconds at sphero speed 50 when added to the wait time
        # of the start function
        self.timeOneGrid = 600
        #
        self.obs = PhotoImage(file='obs.gif')
        self.leftUp = PhotoImage(file="left_up.gif")
        self.leftDown = PhotoImage(file="left_down.gif")
        self.rightDown = PhotoImage(file='right_down.gif')
        self.rightUp = PhotoImage(file='right_up.gif')
        self.hor = PhotoImage(file='horizontal.gif')
        self.ver = PhotoImage(file='vertical.gif')
        self.start = PhotoImage(file='start.gif')
        self.blank = PhotoImage(file='blank.gif')

        # display is updated with obstacles

        for i in range(96):
            if self.arrMaze[i] == 'x':
                print i
                lstDisplayLBLNames[i].config(image=self.obs)
                lstDisplayLBLNames[i].image = self.obs

        print self.bestRoute
        try:
            # the first grid picture is set - start point
            lstDisplayLBLNames[self.bestRoute[0] - 1].config(image=self.start)
            lstDisplayLBLNames[self.bestRoute[0] - 1].image = self.start
        except IndexError:
            tkMessageBox.showerror("No route Found", "There is no route found, please try putting in a route again.")

    # Upon button 'Start' pressed, route will be calculated and sent to sphero to move
    # input: bearing (0 - 259 int value)
    # output: movement of Sphero"""
    def fnSpheroStart(self, bearing):
        # set status update
        lblStatusUpdate[0].config(text='Connecting to Sphero...')
        # update the window
        lstDisplayLBLNames[2].update()

        # wait 10 seconds for bluetooth sphero connection to be ready again
        lstDisplayLBLNames[0].after(5000)

        try:
            # bluetooth sphero connection is activated
            sphero.connect()
            # raw values set
            sphero.set_filtered_data_strm(40, 1, 0, True)
            # sphero is ready
            sphero.start()
            lblStatusUpdate[0].config(text='Connection successful')
            # update the window
            lstDisplayLBLNames[2].update()

            # set stop to false
            self.stop = False

            # set initial time
            self.startTime = time.time()

        # in case of bluetooth connection to sphero failure
        except (IOError, RuntimeError, AttributeError):
            # ask user if they would like to attempt the connection again
            attemptAgain = tkMessageBox.askyesno("Sphero Connection", "Connection Failure. Retry Connection?")
            if attemptAgain is True:  # user would like to attempt again
                self.fnSpheroStart(bearing)

            else:  # user does not want to attempt again
                # clear status bar; no processes going on
                lblStatusUpdate[0].config(text='')
                # update the window
                lstDisplayLBLNames[2].update()

        index = 0
        # this loops through each grid in bestRoute as determines where to direct sphero
        # then it calls the update display function to represent the route as it is occurring
        for eachStep in self.bestRoute:
            # if stop has been pressed, display ceases updating
            if self.stop == True:
                break
            # make the variables index, eachStep able to be accessed in the display logic function
            self.index = index
            self.eachStep = eachStep

            # all directions are in terms of sphero travelling at 'bearing'
            # if the next grid visited is equal to current grid + 1, straight ahead
            try:
                if self.bestRoute[index + 1] == self.bestRoute[index] + 1:
                    sphero.roll(50, bearing, 1, True)
                    self.fnDisplayLogic()

                # if the next grid visited is equal to current grid + 1, then it must be located behind
                elif self.bestRoute[index + 1] == self.bestRoute[index] - 1:
                    if bearing + 180 >= 360:
                        bearing -= 360
                    sphero.roll(50, bearing + 180, 1, True)
                    self.fnDisplayLogic()

                # if the next grid visited is equal to current grid + 12, then it must be located to the right
                elif self.bestRoute[index + 1] == self.bestRoute[index] - 12:
                    if bearing + 270 >= 360:
                        bearing -= 360
                    sphero.roll(50, bearing + 270, 1, True)
                    self.fnDisplayLogic()

                # if the next grid visited is not equal to current grid - 12, it must be located to the left
                elif self.bestRoute[index + 1] == self.bestRoute[index] + 12:
                    if bearing + 90 >= 360:
                        bearing -= 360
                    sphero.roll(50, bearing + 90, 1, True)
                    self.fnDisplayLogic()

            # the end of the route
            except IndexError:
                self.fnDisplayLogic()
                # stop sphero rolling
                sphero.roll(0,0,0,True)

            # time delay
            lstDisplayLBLNames[0].after(self.timeOneGrid)
            index += 1

    # stops the movement of the sphero
    # input: button 'stop' pressed in interface
    # output: if sphero control mode:
    #         - movement of sphero stops
    #         - sphero disconnects via bluetooth
    #         - display is wiped ecept for obstacles and start point + time elapsed cleared
    #        if simulation mode:
    #       - display is wiped ecept for obstacles and start point + time elapsed cleared
    def fnSpheroStop(self):
        # clears the display of route
        for eachGrid in self.bestRoute:
            # start image is already set so it is skipped in the blanking process
            if self.bestRoute[0] == eachGrid:
                pass
            else:
                lstDisplayLBLNames[eachGrid - 1].config(image=self.blank)
                lstDisplayLBLNames[eachGrid - 1].image = self.blank

        # set the stop boolean to true
        self.stop = True

        try:
            # if mode selected is simulation, trying to disconnect from a sphero that was never connected in the first
              # place will raise an error
            # clear status
            lblStatusUpdate[0].config(text='Disconnecting from Sphero...')
            lstDisplayLBLNames[2].update()
            # disconnect from sphero via bluetooth
            sphero.term_thread()
            sphero.disconnect()
            # update status
            lblStatusUpdate[0].config(text='Sphero Disconnected')
        except (IOError, RuntimeError, AttributeError):
            lblStatusUpdate[0].config(text='')

        # clear time elapsed label
        lblTime[0].config(text = "00:00")

# in simulation mode, only display logic is called as there is no control of sphero
# input: button 'start' pressed while mode selected is 'simulation'
# output: self.index : index of interation in route
#         self.eachStep : actual cell value of iteration in route
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
            # the display logic is in terms of the sphero robot being in the centre of the current grid
            # travelling at 'bearing' in degrees True
            #               left
            #               _________
            #  behind    |  sphero -> | ahead
            #            |  ----------|
            #                right

            # last grid is behind the current grid
            if self.bestRoute[self.index - 1] == self.bestRoute[self.index] - 1:
                # next grid is above current grid but last grid was behind
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftUp

                # next grid is to the right of current grid but last grid was behind
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftDown

                # next grid is straight ahead of current grid but last grid was behind
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.hor)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.hor

            # last grid is to straight ahead of current grid
            elif self.bestRoute[self.index - 1] == self.bestRoute[self.index] + 1:
                # next grid is to the left of current grid but last grid was straight ahead
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightUp

                # next grid is to the right of current grid but last grid was straight ahead
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightDown

                # last grid was straight ahead and next grid is directly behind current grid
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.hor)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.hor

            # last grid is to the left of current grid
            elif self.bestRoute[self.index - 1] == self.bestRoute[self.index] - 12:
                # next grid is directly behind current grid, last grid was to the left
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftUp

                # next grid is straight ahead current grid, last grid was to the left
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightUp)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightUp

                # next grid to the right of current grid, last grid was to the left
                elif self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 12:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.ver)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.ver

            # last grid is to the right of the current grid
            elif self.bestRoute[self.index - 1] == self.bestRoute[self.index] + 12:
                # next grid is directly behind current grid, last grid was to the right
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] + 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.rightDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.rightDown

                    # next grid is to the right of current grid, last grid was to the right
                if self.bestRoute[self.index + 1] == self.bestRoute[self.index] - 1:
                    lstDisplayLBLNames[self.eachStep - 1].config(image=self.leftDown)
                    lstDisplayLBLNames[self.eachStep - 1].image = self.leftDown

                # next grid is to the left of current grid, last grid to the right
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
