#Kairavi Chahal
#kchahal@andrew.cmu.edu

def readMaze(maze, filename):
    mazeFile = open(filename, "r")
    lines = mazeFile.readlines()
    for line in lines:
        line = line.strip()
        row = [c for c in line]
        maze.append(row)

def findStartRow(maze):
    for row in xrange(len(maze)):
        for col in xrange(len(maze[row])):
            if (maze[row][col] == "S"):
                return row

def findStartCol(maze):
    for row in xrange(len(maze)):
        for col in xrange(len(maze[row])):
            if (maze[row][col] == "S"):
                return col

def findPath(row, col, maze, mazeSolution):
    if (maze[row][col] == "F"):
        mazeSolution.append("End: (%d, %d)" % (row, col))
        return True
    if (maze[row][col] == "W"):
        return False
    if ("(%d, %d)" % (row, col) in mazeSolution):
        return False
    mazeSolution.append("(%d, %d)" % (row, col))
    #print mazeSolution
    if ((row < len(maze)-1) and (findPath(row+1, col, maze, mazeSolution))) or ((col > 0) and (findPath(row, col-1, maze, mazeSolution))) or ((row > 0) and (findPath(row-1, col, maze, mazeSolution))) or ((col < len(maze[row])-1) and (findPath(row, col+1, maze, mazeSolution))):
        return True
    else:
        mazeSolution.remove("(%d, %d)" % (row, col))
        #print mazeSolution
    return False

def solveMaze(maze, mazeSolution):
    row = findStartRow(maze)
    col = findStartCol(maze)
    if findPath(row, col, maze, mazeSolution):
        return True

mazeFile = "sampleMaze.txt"

maze = []
mazeSolution = []

readMaze(maze, mazeFile)

if (solveMaze(maze, mazeSolution)):
    print "The solution is:", mazeSolution
else:
    print "No solution found."
