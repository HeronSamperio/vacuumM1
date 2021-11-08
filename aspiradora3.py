#A01276217-A01276214
import matplotlib.pyplot as plt
import random
from Node import *
from copy import copy, deepcopy

matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

presentationMatrix = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

currLine = 6
currCol = 6
stack = [Node(6, 6)]
solution = [Node(6, 6)]
currLine1 = 1
currCol1 = 1
stack1 = [Node(1, 1)]
solution1 = [Node(1, 1)]
currLine2 = 6
currCol2 = 1
stack2 = [Node(6, 1)]
solution2 = [Node(6, 1)]
process_map = []

def mapNotClean():
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if (matrix[i][j] == 2):
                return True
    return False

#imprime el resultado y recorrido
def renderMatrix(matrix):
    plt.imshow(matrix, 'gray')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.plot(currCol1, currLine1, '*c', 'LineWidth', 5)
    plt.plot(currCol2, currLine2, '*y', 'LineWidth', 5)
    plt.pause(0.3)
    plt.clf()

#genera el tablero con datos aleatorios
def createWorld(m):#implementar verificar si la cantidad de cuadros sucios es par 
    global presentationMatrix
    x= len(presentationMatrix)
    y=0
    for mI in range(1, x-1):
        for aI in range(1, x-1):
            if (mI == 1 and aI == 1):
                continue
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0

    renderMatrix(matrix)
    global process_map
    process_map = deepcopy(matrix)
    presentationMatrix = deepcopy(matrix)


#######

def hasPosition(x, y):
    if (matrix[x][y] == 1):
        return False
    return True


def lookLeft(x, y, node):
    if (hasPosition(x - 1, y)):
        new_node = Node(x - 1, y, node)
        if (process_map[x - 1][y] == 2):
            return new_node
        if (process_map[x - 1][y] != 4):
            stack.append(new_node)
            process_map[x - 1][y] = 4


def lookRight(x, y, node):
    if (hasPosition(x + 1, y)):
        new_node = Node(x + 1, y, node)
        if (process_map[x + 1][y] == 2):
            return new_node
        if (process_map[x + 1][y] != 4):
            stack.append(new_node)
            process_map[x + 1][y] = 4


def lookAbove(x, y, node):
    if (hasPosition(x, y - 1)):
        new_node = Node(x, y - 1, node)
        if (process_map[x][y - 1] == 2):
            return new_node
        if (process_map[x][y - 1] != 4):
            stack.append(new_node)
            process_map[x][y - 1] = 4


def lookDown(x, y, node):
    if (hasPosition(x, y + 1)):
        new_node = Node(x, y + 1, node)
        if (process_map[x][y + 1] == 2):
            return new_node
        if (process_map[x][y + 1] != 4):
            stack.append(new_node)
            process_map[x][y + 1] = 4


def discoverPath():
    while (len(stack) != 0):
        node = stack.pop(0)
        x = node.get_x()
        y = node.get_y()

        auxNode = lookLeft(x, y, node)
        if (auxNode):
            return auxNode

        auxNode = lookAbove(x, y, node)
        if (auxNode):
            return auxNode

        auxNode = lookRight(x, y, node)
        if (auxNode):
            return auxNode

        auxNode = lookDown(x, y, node)
        if (auxNode):
            return auxNode


##
          
def hasPosition1(x, y):
    if (matrix[x][y] == 1):
        return False
    return True


def lookLeft1(x, y, node1):
    if (hasPosition1(x - 1, y)):
        new_node1 = Node(x - 1, y, node1)
        if (process_map[x - 1][y] == 2):
            return new_node1
        if (process_map[x - 1][y] != 4):
            stack1.append(new_node1)
            process_map[x - 1][y] = 4


def lookRight1(x, y, node1):
    if (hasPosition1(x + 1, y)):
        new_node1 = Node(x + 1, y, node1)
        if (process_map[x + 1][y] == 2):
            return new_node1
        if (process_map[x + 1][y] != 4):
            stack1.append(new_node1)
            process_map[x + 1][y] = 4


def lookAbove1(x, y, node1):
    if (hasPosition1(x, y - 1)):
        new_node1 = Node(x, y - 1, node1)
        if (process_map[x][y - 1] == 2):
            return new_node1
        if (process_map[x][y - 1] != 4):
            stack1.append(new_node1)
            process_map[x][y - 1] = 4


def lookDown1(x, y, node1):
    if (hasPosition1(x, y + 1)):
        new_node1 = Node(x, y + 1, node1)
        if (process_map[x][y + 1] == 2):
            return new_node1
        if (process_map[x][y + 1] != 4):
            stack1.append(new_node1)
            process_map[x][y + 1] = 4


def discoverPath1():
    while (len(stack1) != 0):
        node1 = stack1.pop(0)
        x = node1.get_x()
        y = node1.get_y()

        auxNode = lookLeft1(x, y, node1)
        if (auxNode):
            return auxNode

        auxNode = lookAbove1(x, y, node1)
        if (auxNode):
            return auxNode

        auxNode = lookRight1(x, y, node1)
        if (auxNode):
            return auxNode

        auxNode = lookDown1(x, y, node1)
        if (auxNode):
            return auxNode
        

##
          
def hasPosition2(x, y):
    if (matrix[x][y] == 1):
        return False
    return True


def lookLeft2(x, y, node2):
    if (hasPosition2(x - 1, y)):
        new_node2 = Node(x - 1, y, node2)
        if (process_map[x - 1][y] == 2):
            return new_node2
        if (process_map[x - 1][y] != 4):
            stack2.append(new_node2)
            process_map[x - 1][y] = 4


def lookRight2(x, y, node2):
    if (hasPosition2(x + 1, y)):
        new_node2 = Node(x + 1, y, node2)
        if (process_map[x + 1][y] == 2):
            return new_node2
        if (process_map[x + 1][y] != 4):
            stack2.append(new_node2)
            process_map[x + 1][y] = 4


def lookAbove2(x, y, node2):
    if (hasPosition2(x, y - 1)):
        new_node2 = Node(x, y - 1, node2)
        if (process_map[x][y - 1] == 2):
            return new_node2
        if (process_map[x][y - 1] != 4):
            stack2.append(new_node2)
            process_map[x][y - 1] = 4


def lookDown2(x, y, node2):
    if (hasPosition2(x, y + 1)):
        new_node2 = Node(x, y + 1, node2)
        if (process_map[x][y + 1] == 2):
            return new_node2
        if (process_map[x][y + 1] != 4):
            stack2.append(new_node2)
            process_map[x][y + 1] = 4


def discoverPath2():
    while (len(stack2) != 0):
        node2 = stack2.pop(0)
        x = node2.get_x()
        y = node2.get_y()

        auxNode = lookLeft2(x, y, node2)
        if (auxNode):
            return auxNode

        auxNode = lookAbove2(x, y, node2)
        if (auxNode):
            return auxNode

        auxNode = lookRight2(x, y, node2)
        if (auxNode):
            return auxNode

        auxNode = lookDown2(x, y, node2)
        if (auxNode):
            return auxNode

def main():
    global matrix
    global process_map
    global stack
    global stack1
    global stack2
    global currCol
    global currLine
    global currCol1
    global currLine1
    global currCol2
    global currLine2
    
    createWorld(matrix)

    while (mapNotClean()):
        try:
            path2 = discoverPath2()
            x2 = path2.get_x()
            y2 = path2.get_y()
            print("0",path2)
            path1 = discoverPath1()
            x1 = path1.get_x()
            y1 = path1.get_y()
            print("1",path1)
            path = discoverPath()
            x = path.get_x()
            y = path.get_y()
            print("2",path)
        except AttributeError:
            path1 = discoverPath2()
            x1 = path2.get_x()
            y1 = path2.get_y()

        aux_list = []
        while (path2.get_parent() is not None):
            process_map[path2.get_x()][path2.get_y()] = 3
            aux_list.append(path2)
            path2 = path2.get_parent()
        aux_list.reverse()
        solution2.extend(aux_list)
        
        matrix[x2][y2] = 0
        stack2 = [Node(x2, y2)]
        process_map = deepcopy(matrix)

        aux_list = []
        while (path1.get_parent() is not None):
            process_map[path1.get_x()][path1.get_y()] = 3
            aux_list.append(path1)
            path1 = path1.get_parent()
        aux_list.reverse()
        solution1.extend(aux_list)
        
        matrix[x1][y1] = 0
        stack1 = [Node(x1, y1)]
        process_map = deepcopy(matrix)
        
        aux_list = []
        while (path.get_parent() is not None):
            process_map[path.get_x()][path.get_y()] = 3
            aux_list.append(path)
            path = path.get_parent()
        aux_list.reverse()
        solution.extend(aux_list)
        
        matrix[x][y] = 0
        stack = [Node(x, y)]
        process_map = deepcopy(matrix)
    
    for x in range(len(solution)+3):
        try:
            path2=solution2[x]
            path1=solution1[x]
            path=solution[x]
            currCol2 = path2.get_y()
            currLine2 = path2.get_x()
            currCol1 = path1.get_y()
            currLine1 = path1.get_x()
            currCol = path.get_y()
            currLine = path.get_x()
            #renderMatrix(presentationMatrix)
            if (presentationMatrix[currLine2][currCol2] == 2):
                presentationMatrix[currLine2][currCol2] = 0
            if (presentationMatrix[currLine1][currCol1] == 2):
                presentationMatrix[currLine1][currCol1] = 0
            if (presentationMatrix[currLine][currCol] == 2):
                presentationMatrix[currLine][currCol] = 0    
            renderMatrix(presentationMatrix)
        except IndexError:
            try:
                path2=solution[x]
                path1=solution[x]
                path=solution[x]
                currCol2 = path2.get_y()
                currLine2 = path2.get_x()
                currCol1 = path1.get_y()
                currLine1 = path1.get_x()
                currCol = path.get_y()
                currLine = path.get_x()
                renderMatrix(presentationMatrix)
                if (presentationMatrix[currLine2][currCol2] == 2):
                    presentationMatrix[currLine2][currCol2] = 0
                if (presentationMatrix[currLine1][currCol1] == 2):
                    presentationMatrix[currLine1][currCol1] = 0
                if (presentationMatrix[currLine][currCol] == 2):
                    presentationMatrix[currLine][currCol] = 0    
                renderMatrix(presentationMatrix)
            except IndexError:
                path2=solution[x]
                path1=solution2[x]
                path=solution[x]
                currCol2 = path2.get_y()
                currLine2 = path2.get_x()
                currCol1 = path1.get_y()
                currLine1 = path1.get_x()
                currCol = path.get_y()
                currLine = path.get_x()
                renderMatrix(presentationMatrix)
                if (presentationMatrix[currLine2][currCol2] == 2):
                    presentationMatrix[currLine2][currCol2] = 0
                if (presentationMatrix[currLine1][currCol1] == 2):
                    presentationMatrix[currLine1][currCol1] = 0
                if (presentationMatrix[currLine][currCol] == 2):
                    presentationMatrix[currLine][currCol] = 0    
                renderMatrix(presentationMatrix)
    
    
if __name__ == "__main__":
    main()