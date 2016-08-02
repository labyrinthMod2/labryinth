# Labyrinth Module 2
# Cecily Tighe
# 2016

#contains most of the functionality

import xml.etree.ElementTree as ET
import time
#import sphero_driver as sphero
from Tkinter import *
from displayNames import lstDisplayLBLNames


class Functions:

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

        speed = 0.35
        time_one_grid = 0.125

        #bestRoute = visited points

        """4. from the best route, Sphero specific instructions are generated
        input:best route
        output: instructions are sent to and are carried out by Sphero"""



        #set heading to zero to ensure orienatation is correct
        #sphero.set_heading(self, heading, response)

        # set the initial clock
        startTime = time.clock()
        index = 0
        bestRoute = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96]
        print bestRoute
        for eachStep in bestRoute:

            # if the next grid visited is equal to current grid + 1, then it must be located to the right
            try:
                if bestRoute[index + 1] == bestRoute[index] + 1:
                    while True:
                        if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                            # sphero.roll(50, 0, 1, True)
                            print 'right'
                        else:
                            break

                # if the next grid visited is equal to current grid + 1, then it must be located to the left
                elif bestRoute[index + 1] == bestRoute[index] - 1:
                    while True:
                        if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                            # sphero.roll(50, 180, 1, True)
                            print 'left'
                        else:
                            break

                # if the next grid visited is equal to current grid + 12, then it must be located downwards
                elif bestRoute[index + 1] == bestRoute[index] - 12:
                    while True:
                        if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                            # sphero.roll(50, 270, 1, True)
                            print 'up'
                        else:
                            break

                # if the next grid visited is not equal to any of the earlier options, it must be located upwards
                elif bestRoute[index + 1] == bestRoute[index] + 12:
                    while True:
                        if round(time.clock(), 2) < round(startTime + 0.5 * index, 2):
                            # sphero.roll(50, 270, 1, True)
                            print 'down'
                        else:
                            break
                index += 1
            # the end of the route
            except IndexError:
                pass
                
                
            
    """ stops the movement of the sphero"""
    def fnSpheroStop(self):
        """also stop display"""
        #sphero.disconnect(self)


    """upon mouse click 'stop', uses an arrangement of pictures to replicate the route the Sphero is following
        input: best route instructions
        output: display is updated"""

    def fnUpdateDisplay(self):

        """using list of pictures to replicate route
            wait amount of seconds, display the next picture"""
        leftUp = PhotoImage(file="left_up.gif")
        leftDown = PhotoImage(file="left_down.gif")
        rightDown = PhotoImage(file='right_down.gif')
        rightUp = PhotoImage(file='right_up.gif')
        hor = PhotoImage(file='horizontal.gif')
        ver = PhotoImage(file='vertical.gif')
        ob3 = PhotoImage(file='ob3.gif')
        ob3 = PhotoImage(file='ob3.gif')
        ob1 = PhotoImage(file='ob1.gif')

        bestRoute = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36, 48, 60, 72, 84, 96]
        dictMaze = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 11, 12,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    'Z', 'A', 'A', 0, 0, 0, 0, 0, 0, 0, 0, 0,]
        # set picture for obstacles
        # this happens first as it is not reliant upon time

        index = 0
        for eachCell in dictMaze:
            index += 1
            print eachCell


            if str(eachCell )== 'Z' or 'A':
                lstDisplayLBLNames[index].config(image=hor)
                lstDisplayLBLNames[index].image = hor

            elif eachCell == 'Y' or 'B':
                ob2 = PhotoImage(file='ob2.gif')
                lstDisplayLBLNames[index].config(image=ob2)
                lstDisplayLBLNames[index].image=ob2

            elif eachCell == 'X' or 'C':

                lstDisplayLBLNames[index].config(image=ob1)
                lstDisplayLBLNames[index].image=ob1



        index = -1

        startTime = time.time()
        for eachStep in bestRoute:
            index += 1





            while True:
                nowTime = time.time()
                timeElapsed = nowTime - startTime

                if timeElapsed > 0.5 *(index + 1):
                    try:
                        print 'trying'

                        # last grid is to the left of the current grid
                        if bestRoute[index - 1] == bestRoute[index] - 1:
                            # next grid is above current grid but last grid was to the left
                            if bestRoute[index + 1] == bestRoute[index] - 12:
                                lstDisplayLBLNames[eachStep - 1].config(image=leftUp)
                                lstDisplayLBLNames[eachStep - 1].image = leftUp


                            # next grid is below current grid but last grid was the left
                            elif bestRoute[index + 1] == bestRoute[index] + 12:
                                lstDisplayLBLNames[eachStep - 1].config(image=leftDown)
                                lstDisplayLBLNames[eachStep - 1].image = leftDown

                            # next grid is to the right of the current grid but last grid was to the left
                            elif bestRoute[index + 1] == bestRoute[index] + 1:
                                lstDisplayLBLNames[eachStep - 1].config(image=hor)
                                lstDisplayLBLNames[eachStep - 1].image = hor
                                print 'y'




                        # last grid is to the right of the current grid
                        elif bestRoute[index - 1] == bestRoute[index] + 1:
                            # next grid is above the current grid but last grid was to the right
                            if bestRoute[index + 1] == bestRoute[index] - 12:
                                lstDisplayLBLNames[eachStep - 1].config(image=rightUp)
                                lstDisplayLBLNames[eachStep - 1].image = rightUp

                            # next grid is below the current grid but last grid was to the right
                            elif bestRoute[index + 1] == bestRoute[index] + 12:
                                lstDisplayLBLNames[eachStep - 1].config(image=rightDown)
                                lstDisplayLBLNames[eachStep - 1].image = rightDown


                            # last grid was to the right and next grid is to the left of the current grid
                            elif bestRoute[index + 1] == bestRoute[index] - 1:
                                lstDisplayLBLNames[eachStep - 1].config(image=hor)
                                lstDisplayLBLNames[eachStep - 1].image = hor



                        # last grid is above of the current grid
                        if bestRoute[index - 1] == bestRoute[index] - 12:
                            # next grid is to the left of current grid, last grid was above current grid
                            if bestRoute[index + 1] == bestRoute[index] - 1:
                                lstDisplayLBLNames[eachStep - 1].image = leftUp

                            # next grid is to the right of current grid, last grid was above current grid
                            elif bestRoute[index + 1] == bestRoute[index] + 1:
                                lstDisplayLBLNames[eachStep - 1].config(image=rightUp)
                                lstDisplayLBLNames[eachStep - 1].image = rightUp

                            # next grid is below current grid, last grid was above current grid
                            elif bestRoute[index + 1] == bestRoute[index] + 12:
                                lstDisplayLBLNames[eachStep - 1].config(image=ver)
                                lstDisplayLBLNames[eachStep - 1].image = ver


                        # last grid is below the current grid
                        if bestRoute[index - 1] == bestRoute[index] + 12:
                            # next grid is to the left of current grid, last grid was below current grid
                            if bestRoute[index + 1] == bestRoute[index] + 1:
                                lstDisplayLBLNames[eachStep - 1].config(image=leftDown)
                                lstDisplayLBLNames[eachStep - 1].image = leftDown

                                # next grid is to the right of current grid, last grid was below
                            elif bestRoute[index + 1] == bestRoute[index] - 1:
                                lstDisplayLBLNames[eachStep - 1].config(image=rightDown)
                                lstDisplayLBLNames[eachStep - 1].image = rightDown

                            # next grid is above of current grid, last grid was below current grid
                            elif bestRoute[index + 1] == bestRoute[index] - 12:
                                lstDisplayLBLNames[eachStep - 1].config(image=ver)
                                lstDisplayLBLNames[eachStep - 1].image = ver

                    # there is no 'last grid' - the current grid is the start route
                    # or
                    # there is no 'next grid'- current grid is the end route
                    except IndexError:
                        # init = PhotoImage(file = 'start.gif')
                        lstDisplayLBLNames[eachStep - 1].config(image=ver)
                        lstDisplayLBLNames[eachStep - 1].image = ver
                    break

                else:
                    pass
        print lstDisplayLBLNames












