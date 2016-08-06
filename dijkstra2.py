# Eleni Cook
# 2016
# this is Dijkstra Algrothim
# the algorthim is desgin to find the shortest path in a maze
# the code has been taken from: http://www.bogotobogo.com/python/files/Dijkstra/Dijkstra_shortest_path.py
# this code has been modified for finding the shortest path for a maze

import sys

listWayPoints = []
listBarriers = []
listWayPointsIndex =[]
listValidGrids= []

    # maze that the algorthim is trying to slove
maze = [[1, 0, 0, 0, 0, "x", 0, "x", 0, 0, "x", 0],
        ["x", "x", 0, 0, 0, "x", 0, 0, 0, 0, "x", "x"],
        [0, 0, 0, "x", 0, 0, 0, 0, "x", "x", 0 ,"x"],
        [0, "x", "x", 0, 0, "x", "x", "x", 0, 0, 0, "x"],
        [0, "x", 0, 0, 0, 0, "x", 'x', 0, 'x', 0, 0],
        [0, 'x', 0, 0, 'x', 0, 0, 0, 0, 2, 0, 'x'],
        ['x', 0, 'x', 0, 0, 'x', 'x', 'x', 0, 0, 0, 'x'],
        ['x', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'x']]

listMaze1d = ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x",
        "x", 1, 0, 0, 0, 0, "x", 0, "x", 0, 0, "x", 0,"x",
        "x", "x", "x", 0, 0, 0, "x", 0, 0, 0, 0, "x", "x","x",
        "x", 0, 0, 0, "x", 0, 0, 0, 0, "x", "x", 0 ,"x","x",
        "x", 0, "x", "x", 0, 0, "x", 0, "x", 0, 0, 0, "x","x",
        "x", 0, "x", 0, 0, 0, 0, "x","x", 0, "x", 0, 0,"x",
        "x", 0, "x", 0, 0, 0 , 0, 0, 0, 0, 2, 0, "x","x","x",
        "x", 0, "x", 0, 0, "x", "x", "x", 0, 0, 0, "x",0,"x",
        "x" , 0, 0, 3, 0, 0, 0, 0, 0, 0,0 ,0,0,"x",
        "x","x","x","x","x","x","x","x","x","x","x","x","x","x"]

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


    # this function finds the way points of the maze
def fnFindWaypoints( listMaze1d, listWayPoints):
        for grid in listMaze1d:
            if isinstance(grid, int) and grid> 0:
                    listWayPoints.append(grid)
        #print listWayPoints
        return listWayPoints


# this function finds the barriers in the maze
def fnFindBarriers(listMaze1d, listBarriers):
    index =-1
    for each in listMaze1d:
        index = index +1
        if each =="x":
            listBarriers.append(index)
            #print listBarriers
    return listBarriers

# this fucntion finds the vaild grid spots that can be travelled to
def fnFindVaildGrid(listValidGrids, listMaze1d):
    index = -1
    for grid in listMaze1d:
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
def fnWayPointsIndex(listMaze1d, listWayPointsIndex, listWayPoints):
    for waypoint in listWayPoints:
        index = -1
        for cell in listMaze1d:
            index = index+1
            if waypoint == cell:
                listWayPointsIndex.append(index)
                print listWayPointsIndex
    return listWayPointsIndex

fnFindWaypoints(listMaze1d, listWayPoints)
fnFindBarriers(listMaze1d, listBarriers)
fnTimSort(listWayPoints)
fnWayPointsIndex(listMaze1d, listWayPointsIndex, listWayPoints)
fnFindVaildGrid(listValidGrids, listMaze1d)
    
if __name__ == '__main__':

    g = Graph()


    # grid number which will be the vertices names with are strings
    grid =[]

    # grid numbers which are integers
    gridnum = []
    for num in range(1,141):
        grid.append(str(num))
        gridnum.append(num)
        print grid


    # creates vertices for the algorithm
    for vertex in grid:
        g.add_vertex(vertex)


    # create the edges for the algorithm
    # this loop creates the edges left/right of cell
    for step in gridnum:
        step1 = step + 1
        for validgrid in listValidGrids:
            if step == validgrid:
                for validNextStep in listValidGrids:
                    if step1 == validNextStep:
                        g.add_edge(str(step), str(step1),1 )
                        print "true " + str(step) + " " + str(step1)
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
                print "true two " + str(nextstep) +" " + str(step2)
        """else:
            print "false two" + nextstep
            print"""


    print 'Graph data:'
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

    startWayPointIndex = 0
    endWayPointIndex = 1
    while endWayPointIndex < len(listWayPointsIndex):
        print len(listWayPointsIndex)

        startWayPoint = listWayPointsIndex[startWayPointIndex]
        endWayPoint = listWayPointsIndex[endWayPointIndex]
        dijkstra(g, g.get_vertex(str(startWayPoint)), g.get_vertex(str(endWayPoint)))

        target = g.get_vertex(str(endWayPoint))
        path = [target.get_id()]
        shortest(target, path)
        print 'The shortest path : %s' %(path[::-1])
        startWayPointIndex = startWayPointIndex +1
        endWayPointIndex = endWayPointIndex+ 1
