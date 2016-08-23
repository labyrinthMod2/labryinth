# Eleni Cook
# 2016

# this pythoh file contians all the funtonality that the program Module 1- Labyrithn

# this is python file also contians Dijkstra Algorithm
# the algorithm is designed to find the shortest path in a maze
# the code has been taken from: http://www.bogotobogo.com/python/files/Dijkstra/Dijkstra_shortest_path.py
# this code has been modified  and added to for finding the shortest path for a maze

import sys

from xml.etree import ElementTree
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement
import xml.etree.ElementTree as ET
import locale
from buttonNames import listBtnName
import tkMessageBox



#a list of way points
listWayPoints = []

#a list of Barriers
listBarriers = []

# a list of the way point index numbers in the grid
listWayPointsIndex =[]

# a list of all the possible cells that can be visited in the maze
listValidGrids= []

# a list of all the shortest paths
listPaths =[]

# these are the Fucntions that are used in the GUI expect for Dijkstra's Algorithm
class Functions:

    # a list of the maze
    # this is the defult emtpy maze
    # the maze perminetly has barriers around it
    # "x" is a barrier
    #  0 is a empty grid
    # 1, 2 etc.. are waypoints
    listMaze1d = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x","x","x","x","x","x","x","x","x","x","x","x","x","x"]

    # this intiates the class
    def __init__(self):

        # this is a list of the current buttons that are waypoints
        self.listCurrentWayPoints=[]

        # a list of all avaible way points that the user could put into the maze
        
        self.listAvaibleWayPoints =[]

        # this for loop creates the way points to put into the list of avaible way points
        for waypoints in  range(1,97):
            self.listAvaibleWayPoints.append(waypoints)

        # this is an integer that decides how to the maze is going to be created
        # mode = 1, add way points
        # mode = 2 , delete way points
        # mode = 3 , add barriers
        # mode = 4, delete barriers
        self.mode = 0

    # this function sets the "mode" to Add Way Points when the user is creating the maze
    # Required Agruments:
    #   - none
    # Return Value:
    # - none 
    def fnAddWaypoints(self):
        self.mode = 1

    # this function sets the "mode" to Delete Way Points
    # Required Agruments:
    #   - none
    # Return Value:
    # - none 
    def fnDeleteWayPoint(self):
        index = -1
        # this for loops checks each grid in the maze
        for cell in self.listMaze1d:
            index = index + 1
            # this chekcs to see if the cell is an integer and is greater than zero, therefore a waypoint
            if isinstance(cell, int) and cell> 0:
                # the cell then becomes an empty cell in the maze
                self.listMaze1d[index]=0
                print "true"
                print   self.listMaze1d
                print cell
        # the list of avaible wywaypoint resets
        self.listAvaibleWayPoints = []
        # this for loops re-adds the available way point to the
        for wayPoint in range(1,97):
            self.listAvaibleWayPoints.append(wayPoint)

        # this for loops changes the buttons to white
        for buttons in self.listCurrentWayPoints:
            listBtnName[buttons].config(bg="white", text ="")

        print self.listMaze1d

    # this function sets the "mode" to Add Barriers
    # Required Agruments:
    #   - none
    # Return Value:
    # - none 
    def fnAddBarriers(self):
        self.mode = 3

     # this function sets the "mode" to Delete Barriers
    # Required Agruments:
    #   - none
    # Return Value:
    # - none 
    def fnDeleteBarriers(self):
        self.mode =4

    # this fucntion resets the maze
    # Required Agruments:
    #   - none
    # Return Value:
    # - listMaze1d: list
    def fnResetMaze(self):
        # this resest the maze to the defult state
        self.listMaze1d = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,"x",
        "x","x","x","x","x","x","x","x","x","x","x","x","x","x"]

        # this retest the avavible waypoints 
        self.listAvaibleWayPoints =[]

        # this re-adds the wypoints to the list
        for waypoint in range(1,97):
            self.listAvaibleWayPoints.append(waypoint)

      # this foor loops chnages each button to white 
        for button in range(0,96) :
            # button is the index for the list of button name that is going to be accessed
            # this chnages each button to white
            listBtnName[button].config(bg="white", text =" ")
     # this returns the maze so it can be saved and used outside the function 
        print self.listMaze1d
        return self.listMaze1d

    # this function creates the create based on the user input
    
    # Required Agruments:
    #   - num : integer
    # Return Value:
    # - listMaze1d : list
    
    def fnCreateMaze(self, num):
        # the 12x8 grid needs to be converted into a 14x10 grid
        # the reason being is that for the Dijskt
        
        # cell is the value of the grid cell in a 14x10 grid rather than the 12x8 that its original in
        cell = num+ 15
        # these if statements covert the 12x8 grid into the 14x10, as the maze always has barriers around the border
        # this is the first row of the 14x8
        if cell < 27:
            # the cell varaible has already been added 15 to it
            # therefore, there is no need to add anything to cell, if the cell is in the first row
            # the reason there is a if statement for this sination is because i wanted an else statement for validation if for
            # some reason the number wasnt in the grid
            pass

        # this is the second row in the grid of 14x10
        elif 27<=cell<=38:
            # from the initial 15, 2 is also added to count for the two barriers
            cell = cell +2

        # this is the thrid row in the grid of 14x10
        elif 39<= cell <=50:
            # from the initial 15, 4 is added to count for the two barriers in the pervious row and the two barriers in this row
            cell= cell +4

        # this is the fourth  row in the grid of 14x10
        elif 51<=cell<= 62:
            # from the initial 15, 6 is added to cell
            cell = cell+6

        # this is the 9th row in the grid of 14x10
        elif 63<=cell<=74:
            # from the initial 15, 8 is added to cell
            cell = cell + 8

       # this is the 10th row in the grid of 14x10
        elif 75<=cell<=86:
            # from the initial 15, 10 is added to cell
            cell=cell+10

        # this is the 11th row in the grid of 14x10
        elif 87<=cell<=98:
            # from the initial 15, 12 is added to cell
            cell = cell + 12

        # this is the 12th row in the grid of 14x10
        elif 99<=cell<=110:
            # from the initial 15, 14 is added to cell
            cell =cell + 14

        # this is the ninth row in th grid of 14x10
        elif cell >= 111:
            # from the initial 15, 16 is added to cell
            cell = cell + 16

        # this is used as validation as if for some reason the cell number isnt in the grid
        # the user is shown an error, to inform them that something went wrong
        # eg. it appears when the user hasn't chosen an option
        else:
            tkMessageBox.showwarning("Error", "There was a error with the cell value. Try Again")

        # if the mode = 1 then this means the user wants to add a way point
        if self.mode == 1:
            # this gets the next avaible way point
            wayPoint = self.listAvaibleWayPoints[0]
            # the way point is added to the maze
            self.listMaze1d[cell]= wayPoint
            # the way point is removed for the list of avaible way points
            self.listAvaibleWayPoints.remove(wayPoint)
            # the button changes to green to indicate it's a waypoint
            listBtnName[num].configure(bg= "#B6FF99", text =wayPoint)

            self.listCurrentWayPoints.append(num)

        # if the mode = 3, then the user wants to add a barrier
        elif self.mode ==3:
            # the cell they chose is changed to a barrier
            self.listMaze1d[cell] ="x"
            # the button is chnaged to red
            listBtnName[num].config(bg="#FF7575")


        # if the mode = 4 then the user wants to delete a barrier
        elif self.mode ==4:
            # curentCell is the cell they have choosen
            currentCell =self.listMaze1d[cell]

            # this is validation, to check to see if currentCell is infact a barrier
            if currentCell == "x":
                # if it is a barrier then the cell is chnaged to an empty cell
                self.listMaze1d[cell]=0
                # the button is changed to white
                listBtnName[num].config(bg="white")

            # if the cell is not a barrier then a error message wil appear
            # this informs tha user than the cell they have clicked on is not a barrier
            # nothing happens to the cell
            else:
                tkMessageBox.showwarning("Error", "This is not a Barrier")


        # if the mode is none of the above then an error message appears
        # this is validation and shows the user that they have to select an option
        else:
            tkMessageBox.showwarning("Error", "Please Select an Option")
        print self.listMaze1d

        # the function returns the mze as it has been edited, and has to be used outside of this class
        return self.listMaze1d

    # this function quits the program
    def fnExit(self):
        sys.exit()


#######################################################################################################################

# this is Dijkstra Algrothim
# I didn't write this algrothim
# this algrothim has been taken from:  http://www.bogotobogo.com/python/files/Dijkstra/Dijkstra_shortest_path.py

# this class creates the vertices
class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxint
        # Mark all nodes unvisited        
        self.visited = False  
        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])


# this class creates the the graph which is the maze
class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start, target):
    print '''Dijkstra's shortest path'''
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print 'updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())
            else:
                print 'not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance())

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)
        
#######################################################################################################################


# this is so variables can be access across classes
# the maze is created in the class Fucntions and has to been accessed outside of the class
f=Functions()


    # this function finds the way points of the maze
    # required Arguments:
    #   - list of Way Points: list
    # Return Value:
    #   -List of Way Points: list
    #
def fnFindWaypoints(listWayPoints):

        #this loop find the waypoint in the maze
        for grid in f.listMaze1d:
            # checks to see if the grid in the maze is an integer and over 0, therefore a way point
            if isinstance(grid, int) and grid> 0:
                    # the way point is then added to the list of way points
                    listWayPoints.append(grid)
        # the list of way point is then returned so it can be used in later functions
        return listWayPoints



# this function finds the barriers in the maze
# Required Arguments:
#   - List of Barrier Indexes: list
# Return Value:
#   -list of Barrier Indexes: list

def fnFindBarriers( listBarriers):

    # index is used to find the index of the barriers in the maze
    index =-1
    # this for loops find the barrier indexes
    for grid in f.listMaze1d:
        # the index is added to as the for loop, loops through check cell
        index = index +1
        # checks to see if the grid is a barreier
        if grid =="x":
            # the grid is a barrier then it is appened to a list of barrier indexes
            listBarriers.append(index)

    # the list of barriers is returned to be used in later fucntions
    return listBarriers



# this fucntion finds the vaild grid spots that can be travelled to
# Required Agruments:
#   - List of Vaild Grids: list
# Return Value:
#   - List of Valid Grids : list
def fnFindVaildGrid(listValidGrids):

    # this is index for the index number for the cell in the maze
    index = -1
    # this for loop checks every cell in the maze
    for grid in f.listMaze1d:
        # as the for loops goes through each maze the index number (which is the cell umber) increases
        index = index +1
        # if statment checks to see if the cell is not a barrier
        if grid != "x":
            # if the cell is a not a barrier the index is appended to a list of valid gris cells
            listValidGrids.append(index)
    #the list of valid grid cells is returned to be used in later fucntions
    return listValidGrids


# this function sorts the way points
# the reason why this sorting algorithm was used since the user can hypothetically enter
# as many way points as they want and TimSort is more efficient than Quick or Section Sort
# also I wanted to use the quicker sorting algorthim than Quick and Section Sort since the I wanted
# dijkstra algorithm to run and find the shortest path as fast as possible

# Required Arguments:
#   - List of Way Points: list
# Return Value:
#   -list of Way point : list
def fnTimSort(listWayPoints):
    # this sorts the way points
    listWayPoints.sort()
    # returns the sorted list of way points
    return listWayPoints

# finds the index of the waypoints

# Required Arguments:
#   - List of Way Points: list
#   - List of Way Point indexes: list
# Return Value:
#   -list of Barrier Indices
def fnWayPointsIndex( listWayPointsIndex, listWayPoints):

    # for loops goes trhough each way point in the list of way points
    for waypoint in listWayPoints:
        # this is the index of the way point
        index = -1

        # the checks each cell in the maze
        for cell in f.listMaze1d:

            # as the for loop, loops through the maze the index of each cell increases
            index = index+1
            # checks to see if the cell is a way point
            if waypoint == cell:
                # if the cell is a waypoint it adds it to the list
                listWayPointsIndex.append(index)
    # returns the list of way point indexes
    return listWayPointsIndex

    # this function saves the maze and the shortest paths to a XML file

# Required Arguments:
#   - xml file: string
# Return Value:
#   -list of Barrier none
def fnSaveToXml(xmlFile):

        # this creates the xml document
        rootName = Element("Labyrinth_Maze")

        # for loop goes through get cell in the maze
        for cell in f.listMaze1d:
            # this writes the maze to the xml file
            cellElement = SubElement(rootName, "cell")
            cellElement.text= str(cell)

        # this writes all the paths to xml
        for paths in listPaths:
            routeElement = SubElement(rootName, "route")
            # this writes each grid on a different line
            for grid in paths:
                gridElement =SubElement(routeElement, "grid")
                gridElement.text =str(grid)

        xmlTree = ElementTree.ElementTree(rootName)
        # this writes the content to the xml file
        try:
            xmlTree.write(xmlFile, encoding="utf-8", xml_declaration=True)
        except:
            print "unhandled error."
            pass


# this function asks the user if they want to solve the maze
# Required Arguments:
#   - none
# Return Value:
#   -none
def fnSaveMaze():

    # this is validation and asks if they want to solve the maze
    saveMaze = tkMessageBox.askyesno("Solve Maze", "Are you sure you want to solve this maze?")
    # if the the user says yes, the value of saveMaze is true
    if saveMaze == True:
        # calls the fucntion to solve the maze and find the shortest path
        fnSolveMaze(listWayPointsIndex, listValidGrids, listBarriers, listWayPoints)
    # if the user doesnt want to solve the maze nothing happens
    else:
        pass

# this function solves the maze and finds the shortest route
# Required Arguments:
#   - List of Way Points: list
#   - List of Way Point indexes: list
#   - List of Valid Grids: list
#   - List of Barriers: list
# Return Value:
#   -none
def fnSolveMaze(listWayPointsIndex, listValidGrids, listBarriers, listWayPoints):

    # resest all  these values 
    #a list of way points
    listWayPoints = []

    #a list of Barriers
    listBarriers = []

    # a list of the way point index numbers in the grid
    listWayPointsIndex =[]

    # a list of all the possible cells that can be visited in the maze
    listValidGrids= []

    # a list of all the shortest paths
    listPaths =[]


    # calls the find way point function
    fnFindWaypoints(listWayPoints )
    # calls the find barriers function
    fnFindBarriers(listBarriers)
    # calls the sort function
    fnTimSort(listWayPoints)
    # calls the find the way pnt indexes function
    fnWayPointsIndex(listWayPointsIndex,listWayPoints)
    # calls the find the valid grid functions
    fnFindVaildGrid(listValidGrids )

    # this is the starting way point in the list of way point, index
    # this finds the "starting " way point of the mae, for each shortest path
    startWayPointIndex = 0
    # this finds the "ending" way point for each path
    endWayPointIndex = 1

    # each shortest path is created from way point to way point
    # eg. from way point 1 to 2, for the first path, way point 2 to 3 , for the second path
    # this while loops keeps looping until all shortest paths are found connecting all waypoints
    if len(listWayPoints) >= 2:

        while endWayPointIndex < len(listWayPointsIndex):
            # this to access the graph class
            g = Graph()

            # grid number which will be the vertices names with are strings
            listGrid =[]

            # grid numbers which are integers
            listGridNum = []

            # for loop is for all the numbers from 0 to 140
            # which are the verities
            for num in range(0,140):
                # this is a list of string numbers which are the names of the vertices
                listGrid.append(str(num))
                # this is a list of integers, which are used to do the math and add edges
                listGridNum.append(num)



            # creates vertices for the algorithm
            for vertex in listGrid:
                # this creates a vertex for each grid in listGrid
                g.add_vertex(vertex)


            # create the edges for the algorithm
            # this loop creates the edges left/right of cell
            for gridCell in listGridNum:
                # this is the grid to the left of gridCell
                gridCellLeft = gridCell + 1
                # this loops through the valid grids in maze
                for validGrid in listValidGrids:
                    # checks to see if gridCell is a valid grid
                    if gridCell == validGrid:
                        # this loops through the valid grids again
                        for validNextStep in listValidGrids:
                            # checks if the grid to left of gridCell is a valid cell
                            if gridCellLeft == validNextStep:
                                # if its a valid cell, an edge for the algrothim
                                g.add_edge(str(gridCell), str(gridCellLeft),1 )
                                break
                        break

        # this loop creates edges above/below the cell
            for mazeCell in listGridNum:
                # this is the grid direct below maze cell
                mazeCellBelow = mazeCell + 14
                # this loops through each valid cell in the maze
                for validCell in listValidGrids:
                    # checks if the cell is a valid cell
                    if mazeCell == validCell:
                        # loops through the valid grid
                        for belowStep in listValidGrids:
                            # checks to see if the cell below in a valid cell
                            if mazeCellBelow== belowStep:
                                # if its valid, it creates the edge for the algrothim
                                g.add_edge(str(mazeCell), str(mazeCellBelow), 1)
                                break
                        break


            print 'Graph data:'
            # this for loops goes through some of algrothim,
            # it finds the connections and goes through grid of the maze to find the shortest path
            for v in g:
                for w in v.get_connections():
                    vid = v.get_id()
                    wid = w.get_id()
                    print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))


            # this gets the "staring" way point for the path
            startWayPoint = listWayPointsIndex[startWayPointIndex]
            # this gets the "ending"  way point for the path
            endWayPoint = listWayPointsIndex[endWayPointIndex]
            # this calls the dijskstra fucntion to  find the shortest path
            dijkstra(g, g.get_vertex(str(startWayPoint)), g.get_vertex(str(endWayPoint)))

            # this gets the target way point which is the "ending" way point
            target = g.get_vertex(str(endWayPoint))
            # this gets the paths
            path = [target.get_id()]
            # this finds the shortets path
            shortest(target, path)
            print 'The shortest path : %s' %(path[::-1])

            # this appends the the shortest path to the list of paths
            listPaths.append(path[::-1])

            # this added one to the way point index to find the next path from way pont to way point
            startWayPointIndex = startWayPointIndex +1
            endWayPointIndex = endWayPointIndex+ 1

        # this checks to see if the path found is valid
        if len(path) <=1:
            # this informs  that the shortest path cant be found
            tkMessageBox.showwarning("Error", "Shortest path can not be found")
        else:
            # this saves the shortest routes to an xml file
            fnSaveToXml("route.xml")
            # this informs the user that the maze has been solved
            tkMessageBox.showinfo("Solved Maze", "The shortest route has been saved to an XML file")

            #f.fnResetMaze()
    else:
        # this informs that user that the maze is incomplete and can be solved
         tkMessageBox.showwarning("Error", "Maze is incomplete. Can't be solved")



