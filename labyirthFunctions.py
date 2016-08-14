
# Eleni Cook, 2016
# This is has the functions of the program and mainly the algorithm


# this class has the fucntions to do with the creating and
class Path:
    maze = [[1,"x","t",3,"x","x",],
            [0,0,0,0,0,"x",],
            ["x",0,"t",0,"x",0],
            [2,0,0,0,0,0]]
     
            
        
                
    # if the path needs to dupliacte 
    duplicate = False
    
    # this is the current main path that the programing is testing 
    mainPath = []
    
    # these are the possible paths that the maze could take
    possiblePaths = []
    
    # these are the possible next steps that the path can take 
    possibleNextSteps = []

    # this is the list of all possible paths 
    lstofPaths = []

    listWayPoints = []

    mainCooridates = []
    

# this fucntion finds the waypoint of the fucntion
    def fnFindWaypoints( maze, listWayPoints):
        for row in maze:
            for each in row:
                print each
                if isinstance(each, int) and each> 0:
                    listWayPoints.append(each)       
        print listWayPoints
        return listWayPoints

# this fucntion sorts the way points
# the reason why this sorting algrothim was used since the user can hypertheically enter
# as many way points as they want and TimSort is more efficent than Quick or Section Sort
    def fnTimSort(listWayPoints):
        listWayPoints.sort()
        print listWayPoints
        return listWayPoints

    def fnStartingWayPoint(listWayPoints, mainPath):
        mainPath = listWayPoints[0]
        print mainPath 
        return mainPath
        

    fnStartingWayPoint(listWayPoints, mainPath)
    fnFindWaypoints(maze, listWayPoints)
    fnTimSort(listWayPoints)
        


# this function dulicaptes a path when many options are available
    def fnPathDuplicate():
        # yo


# this fucntion adds a step to the path
    def fnAddStep():
        # yo
    

# this fucntion finds the next steps avavible
    def FindNextStep():
        # yo


# this fucntion takes a next step in the path    
    def fnTakeNextStep(path, nextStep, duplicate, maze, ):

        if duplicate == true:
            curtentPath = PathDuplicate()
            possiblePaths.append(currentPath)
        else:
            currentPath = mainPath

            
    # code the loop for finding if the path has found a maze
       foundWayPoint = False
       
        if foundWayPoint == False:
            duplicate = false
            vaildNextSteps = FindNextSteps()
            vaildPath = false

            for eachStep in vaildNextSteps:
                currentPath.append(eachStep)
                
                
                
                
        


    fnStartingWayPoint(listWayPoints, mainPath)
    fnFindWaypoints(maze, listWayPoints)
    fnTimSort(listWayPoints)
        


# this fucntion saves the path to XML
    def fnSavePathToXML():
        #yo


# class Step:

