# Labyrinth Module 2
# Cecily Tighe
# 2016

import xml.etree.ElementTree as ET

import sphero_driver

class Functions:
    dictRoute = {}

    """ gets route info from xml file and puts it into an array
    input: filename
    output: array of all routes"""
    def fnParseRoutes(self, file):
        """ self.dictRoutes.append(route)"""

    """ gets list of routes and calculates time for each route
        input: list of routes
        output: dictionary of route with time
        eg:
        dictRoute = {[route]:450 }
        list of route and number of seconds"""
    def fnRouteTimes(self):
        index = 0
        while index < len(self.dictRoute):
            for eachRoute in self.dictRoute:
                for eachStep in eachRoute:
                  #  routeTime = distance * speed
                   # self.dictRoute[index] = time
                    index += 1


        """for eachroute in lstRoutes:
            time = distance * speed
            add time to dictroutes"""

    """from the list of times, all times will be sorted and the lowest time returned
        input: route times
        output: best time"""
    def fnTimeSort(self):
        """for each time, sort for best one"""

    """from the best route, Sphero specific instructions will be generated
        input:best route
        output: instructions"""
    def fnGenerateRoute(self):
        """use the library to generate the instructions"""

    """using bluetooth, the Sphero is checked for a response and a battery level is received
        output: error raised if no response or no battery"""
    def fnSpheroCheck(self):
        """get battery life, response check. if battery is below a certain point, raise error
            maybe change colour??"""

    """ when the 'start' button is pressed, the spero will move
        input: route instructions
        output: movement of Sphero"""
    def fnSpheroStart(self):
        """call the capability function in here
            also call the display to start it"""

    """ stops the movement of the sphero"""
    def fnSpheroStop(self):
        """also stop display"""
        sphero_driver.disconnect(self)

    """upon mouse click 'stop', uses an arrangement of pictures to replicate the route the Sphero is following
        input: best route instructions
        output: display is updated"""
    def fnUpdateDisplay(self):
        """using list of pictures to replicate route
            wait amount of seconds, display the next picture"""

    """when return is selected in menubar, the window closes and module 1 is opened"""
    def fnReturnModule1(self):
        """do the thing"""



