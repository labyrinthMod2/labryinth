# Eleni Cook
# 2016
# this is Dijkstra Algorithm
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



# this is a list of way points
listWayPoints = []

# this is a list of Barriers
listBarriers = []

# this is a list of the way point index numbers in the grid
listWayPointsIndex =[]

# this is a list of all the possible cells that can be visited in the maze
listValidGrids= []

# a list of all the shortest paths
listPaths =[]

# maze that the algorithm is trying to slove


"""listMaze1d = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
        "x", 1, 0, 0, 0, 0, "x", 0, "x", 0, 0, "x", 0,"x",
        "x", "x", "x", 0, 0, 0, "x", 0, 0, 0, 0, "x", "x","x",
        "x", 0, 0, 0, "x", 0, 0, 0, 0, "x", "x", 0 ,"x",
        "x", 0, "x", "x", 0, 0, "x", 0, "x", 0, 0, 0, "x","x",
        "x", 0, "x", 0, 0, 0, 0, "x","x", 0, "x", 0, 0,"x",
        "x", 0, "x", 0, 0, 0 , 0, 0, 0, 0, 2, 0, "x","x","x",
        "x", 0, "x", 0, 0, "x", "x", "x", 0, 0, 0, "x",0,"x",
        "x" , 0, 0, 3, 0, 0, 0, 0, 0, 0,0 ,0,0,"x",
        "x","x","x","x","x","x","x","x","x","x","x","x","x","x"]"""


class Functions:
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

    def __init__(self):

        self.listAvaibleWayPoints =[]

        for waypoints in  range(1,97):
            self.listAvaibleWayPoints.append(waypoints)


        self.mode = 0
    # this fucntion opens a file
    """def fnopenfile(self):
        from tkFileDialog import askopenfilename

        Tk().withdraw()
        self.filename = askopenfilename()

        self.frmWindowOne.imgMaze = PhotoImage(file = self.filename)
        self.frmWindowOne.lblMaze.configure(image = self.frmWindowOne.imgMaze)
        self.frmWindowOne.lblMaze.photo = self.frmWindowOne.imgMaze"""

    # this function sets the "mode" to Add Way Points when the user is creating the maze
    def fnAddWaypoints(self):
        self.mode = 1

      # this function sets the "mode" to Delete Way Points
    def fnDeleteWayPoint(self):
        self.mode = 2

    # this function sets the "mode" to Add Barriers
    def fnAddBarriers(self):
        self.mode = 3

     # this function sets the "mode" to Delete Barriers
    def fnDeleteBarriers(self):
        self.mode =4

    # this fucntion resets the maze
    def fnResetMaze(self):
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
        self.listAvaibleWayPoints =[]
        for waypoint in range(1,97):
            self.listAvaibleWayPoints.append(waypoint)

        index = 0
        for button in range(1,97) :
            listBtnName[index].config(bg="white")
            index = index +1
        print self.listMaze1d
        return self.listMaze1d

    # this function creates the create based on the user input
    def fnCreateMaze(self, num):
        # cell is the value of the grid cell in a 14x10 grid rather than the 12x8 that its original in
        cell = num+ 15

        # these if statements covert the 12x8 grid into the 14x10, as the maze always has barriers around the border
        if cell < 29:
            print "cool"
        elif 29<=cell<=40:
            cell = cell +2
        elif 43<= cell <=54:
            cell= cell +4
        elif 57<=cell<= 68:
            cell = cell+6
        elif 71<=cell<=82:
            cell = cell + 8
        elif 85<=cell<=96:
            cell=cell+10
        elif 99<=cell<=110:
            cell = cell + 12
        elif 113<=cell<=124:
            cell =cell + 14

        #
        else:
            tkMessageBox.showwarning("Error", "There was a error with the cell value. Try Again")
            print cell

        if self.mode == 1:
            print 'run'
            waypoint = self.listAvaibleWayPoints[0]
            self.listMaze1d[cell]= waypoint
            self.listAvaibleWayPoints.remove(waypoint)
            listBtnName[num].configure(bg= "#B6FF99")


        elif self.mode == 2:
            deletedWayPoint = self.listAvaibleWayPoints[cell]
            if deletedWayPoint != "x" or deletedWayPoint != 0:
                self.listMaze1d[cell] =0
                self.listAvaibleWayPoints.append(deletedWayPoint)
                self.listAvaibleWayPoints.sort()
                print "rad"


                listBtnName[num].config(bg="white")

            else:
                tkMessageBox.showwarning("Error", "This is not a Way Point")


        elif self.mode ==3:
            self.listMaze1d[cell] ="x"
            listBtnName[num].config(bg="#FF7575")

        elif self.mode ==4:
            currentCell =self.listMaze1d[cell]
            if currentCell == "x":

                self.listMaze1d[cell]=0
                listBtnName[num].config(bg="white")
            else:
                tkMessageBox.showwarning("Error", "This is not a Barrier")


            for waypoints in  range(1,97):
                self.listAvaibleWayPoints.append(waypoints)

        else:
            tkMessageBox.showwarning("Error", "Please Select an Option")
        print self.listMaze1d
        return self.listMaze1d

    def fnExit(self):
        sys.exit()

# this is part of Dijkstra Algrothim
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


# this is so variables can be access across classes
f=Functions()
    # this function finds the way points of the maze
    # required Arguments:
    #   - list of the maze: list
    #   - list of Way Points: list
    # Return Value:
    #   -List of Way Points: list
    #
def fnFindWaypoints(listWayPoints):

        #this loop find the waypoint in the maze
        # by checking if the vaule in the cell is an integer and greater than zero
        for grid in f.listMaze1d:
            if isinstance(grid, int) and grid> 0:
                    listWayPoints.append(grid)
        return listWayPoints



# this function finds the barriers in the maze
# Required Agruments:
#   - List of Maze: List
#   - List of Barrier Indices: list
# Return Value:
#   -list of Barrier Indices

def fnFindBarriers( listBarriers):

    # index is used to find the index of the barriers in the maze
    index =-1

    # this
    for grid in f.listMaze1d:
        index = index +1
        if grid =="x":
            listBarriers.append(index)

    return listBarriers

# this fucntion finds the vaild grid spots that can be travelled to
def fnFindVaildGrid(listValidGrids):
    index = -1
    for grid in f.listMaze1d:
        index = index +1
        if grid != "x":
            listValidGrids.append(index)
            print "grid" + str(index)
    return listValidGrids


# this function sorts the way points
# the reason why this sorting algorithm was used since the user can hypothetically enter
# as many way points as they want and TimSort is more efficient than Quick or Section Sort
# also I wanted to use the quicker sorting algorthim than Quick and Section Sort since the I wanted
# dijkstra algorithm to run and find the shortest path as fast as possible
def fnTimSort(listWayPoints):
    listWayPoints.sort()
    #print listWayPoints
    return listWayPoints

# finds the index of the waypoints
def fnWayPointsIndex( listWayPointsIndex, listWayPoints):
    for waypoint in listWayPoints:
        index = -1
        for cell in f.listMaze1d:
            index = index+1
            if waypoint == cell:
                listWayPointsIndex.append(index)
                #print listWayPointsIndex
    return listWayPointsIndex

    # this fucntion saves the maze and the shortest paths to a XML file
def fnSaveToXml(xmlFile):

        rootName = Element("Labyrinth_Maze")
        for cell in f.listMaze1d:
            cellElement = SubElement(rootName, "cell")
            cellElement.text= str(cell)




        for paths in listPaths:
            routeElement = SubElement(rootName, "route")
            for grid in paths:
                gridElement =SubElement(routeElement, "grid")
                gridElement.text =str(grid)



        xmlTree = ElementTree.ElementTree(rootName)
        try:
            xmlTree.write(xmlFile, encoding="utf-8", xml_declaration=True)
        except:
            print "unhandled error."
            raise


# this function solves the maze and finds the shortest route
def fnSaveMaze():
    saveMaze = tkMessageBox.askyesno("Solve Maze", "Are you sure you want to solve this maze?")
    print saveMaze
    print "radical"
    if saveMaze == True:
        print "epic"
        fnSolveMaze(listWayPointsIndex, listValidGrids, listBarriers, listWayPoints)
    else:
        print"frank"
        pass

def fnSolveMaze(listWayPointsIndex, listValidGrids, listBarriers, listWayPoints):
    fnFindWaypoints(listWayPoints )
    fnFindBarriers(listBarriers)
    fnTimSort(listWayPoints)
    fnWayPointsIndex(listWayPointsIndex,listWayPoints)
    fnFindVaildGrid(listValidGrids )

    startWayPointIndex = 0
    endWayPointIndex = 1

    while endWayPointIndex < len(listWayPointsIndex):
        print "gg"
        g = Graph()
        print len(f.listMaze1d)

        # grid number which will be the vertices names with are strings
        grid =[]

        # grid numbers which are integers
        gridnum = []
        for num in range(1,141):
            grid.append(str(num))
            gridnum.append(num)
            #print grid


        # creates vertices for the algorithm
        for vertex in grid:
            g.add_vertex(vertex)
            print grid


        # create the edges for the algorithm
        # this loop creates the edges left/right of cell
        for step in gridnum:
            step1 = step + 1
            for validgrid in listValidGrids:
                if step == validgrid:
                    for validNextStep in listValidGrids:
                        if step1 == validNextStep:
                            g.add_edge(str(step), str(step1),1 )
                            # print "true " + str(step) + " " + str(step1)
                            break
                        """else:
                            print "False" + str(step) + str(step1)"""

    # this loop creates edges above/below the cell
        for nextstep in gridnum:
            step2 = nextstep + 14
            for validcell in listValidGrids:
                if nextstep == validcell:
                    for belowStep in listValidGrids:
                        if step2== belowStep:
                            g.add_edge(str(nextstep), str(step2), 1)
                    #print "true two " + str(nextstep) +" " + str(step2)
            """else:
                print "false two" + nextstep
                print"""


        print 'Graph data:'
        for v in g:
            for w in v.get_connections():
                vid = v.get_id()
                wid = w.get_id()
                print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))


        # this while loop creates multiple paths from waypoint to waypoint
        print len(listWayPointsIndex)

        startWayPoint = listWayPointsIndex[startWayPointIndex]
        endWayPoint = listWayPointsIndex[endWayPointIndex]
        dijkstra(g, g.get_vertex(str(startWayPoint)), g.get_vertex(str(endWayPoint)))

        target = g.get_vertex(str(endWayPoint))
        path = [target.get_id()]
        shortest(target, path)
        print 'The shortest path : %s' %(path[::-1])


        listPaths.append(path[::-1])
        print listPaths

        startWayPointIndex = startWayPointIndex +1
        endWayPointIndex = endWayPointIndex+ 1

    fnSaveToXml("route.xml")




