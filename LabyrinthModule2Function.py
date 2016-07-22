# Labyrinth Module 2
# Cecily Tighe
# 2016

import xml.etree.ElementTree as ET
import time
#import sphero_driver as sphero
#import LabyrinthModule2GUI as GUI
from Tkinter import *

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
        time_one_grid = 1

        dictTime = {}

        routeArray = [[1, 7, 13, 14, 15, 16, 17, 23, 24],
                      [1, 7, 13, 14, 15, 16, 17, 11, 12, 18, 24]]


        """ 1. All routes are retrieved from an xml file
        input: -
        output: 2D array of all routes"""







        """ 2.Approximate time of route length is calculated and appended to a dictionary along with the actual route
        input: list of routes
        output: dictionary of route with time
        eg:
        dictRoute = {[route]:450 }
        """

        for eachRoute in routeArray:
        #create a new item in the dictionary of route to route times
        #length of time is equal to the amount of sub grids crossed multiplied
        #by the time it takes to cross 1 grid in seconds at speed 1.4 m/s
            eachRoute = tuple(eachRoute)
            approx_length = len(eachRoute) * time_one_grid
            dictTime[approx_length] = eachRoute
        print 'dict: ' + str(dictTime)
        


        """3. From the list of times, all times are sorted and the lowest time returned
        input: dictionary of route times with actual route
        output: best time"""

        lstTime = sorted(dictTime, key=dictTime.get)
        bestRoute = dictTime[lstTime[0]]
        print bestRoute

        """4. from the best route, Sphero specific instructions are generated
        input:best route
        output: instructions are sent to and are carried out by Sphero"""



        #set heading to zero to ensure orienatation is correct
        #sphero.set_heading(self, heading, response)

        # set the initial clock
        startTime = time.clock()

        for eachStep in bestRoute:
            # if the next grid visited is equal to current grid + 1, then it must be located to the right
            if bestRoute[eachStep+1] == bestRoute[eachStep] + 1:
                while True:
                    if round(time.clock(),2) < round(startTime + time_one_grid, 2):
                        #sphero.roll(50, 0, 1, True)
                        print 'right'
                    else:
                        break

            # if the next grid visited is equal to current grid + 1, then it must be located to the left
            elif bestRoute[eachStep+1] == bestRoute[eachStep] - 1:
                while True:
                    if round(time.clock(),2) < round(startTime + time_one_grid):
                        #sphero.roll(50, 180, 1, True)
                        print 'left'
                    else:
                        break

            # if the next grid visited is equal to current grid + 1, then it must be located downwards
            elif bestRoute[eachStep+1] == bestRoute[eachStep] + 7:
                while True:
                    if round(time.clock(),2) < round(startTime + time_one_grid):
                        #sphero.roll(50, 270, 1, True)
                        print 'up'
                    else:
                        break

            # if the next grid visited is not equal to any of the earlier options, it must be located upwards
            else:
                while True:
                    if round(time.clock(),2) < round(startTime + time_one_grid):
                        #sphero.roll(50, 270, 1, True)
                        print 'down'
                    else:
                        break
                
            
                
                
                
            
    """ stops the movement of the sphero"""
    def fnSpheroStop(self):
        """also stop display"""
        #sphero.disconnect(self)

    """upon mouse click 'stop', uses an arrangement of pictures to replicate the route the Sphero is following
        input: best route instructions
        output: display is updated"""
    def fnUpdateDisplay(self, bestRoute):
        """using list of pictures to replicate route
            wait amount of seconds, display the next picture"""
        ld = PhotoImage(file = 'left_down.gif')
        lu = PhotoImage(file = 'left_up.gif')
        ru = PhotoImage(file = 'right_up.gif')
        rd = PhotoImage(file = 'right_down.gif')
        hor = PhotoImage(file = 'horizontal.gif')
        ver = PhotoImage(file = 'vertical.gif')

        """for eachStep in self.bestRoute:
            if eachStep == 'r':
                GUI.lstDisplayLBLNames[eachStep].config(image = hor)
                
            elif eachStep == 'l':
                GUI.lstDisplayLBLNames[eachStep].config(image = hor)
            elif eachStep == 'u':
                while True:
                    if int(time.clock()) < int(starttime + self.time):
                        sphero.roll(50, 270, 1, True)
                    else:
                        break
            elif eachStep == 'd':
                while True:
                    if int(time.clock()) < int(starttime + self.time):
                        sphero.roll(50, 270, 1, True)
                    else:
                        break"""
            
            

        

        

    """when return is selected in menubar, the window closes and module 1 is opened"""
    def fnReturnModule1(self):
        """do the thing"""
 

  #  fnRouteTimes({1 : [1,7,13,14,15,16,17, 23,24],2:[1,7,13,14,15,16,17, 11,12, 18,24]}, speed)

    fnSpheroStart(0)