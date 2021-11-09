#A01276217-A01276214
import matplotlib.pyplot as plt
import random
import statistics as st
from tkinter import messagebox
import time
from Node import *
from copy import copy, deepcopy


matrix = []

presentationMatrix = []

q=0
w=0

currLine = 1
currCol = 1
stack = [Node(1, 1)]
solution = [Node(1, 1)]

currLine1 = 1
currCol1 = 1
stack1 = [Node(1, 1)]
solution1 = [Node(1, 1)]

process_map = []

#verifica si el tablero esta limpio
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
    plt.pause(0.2)
    plt.clf()

#genera el tablero con datos aleatorios
def createWorld(m,rows,cols):
    for mI in range(1,(rows) - 1):
        for aI in range(1,(cols) - 1):
            if (mI == 1 and aI == 1):
                continue
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0
    renderMatrix(matrix)
    global process_map
    global presentationMatrix
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
        

def main(t):
    global q
    global w
    global process_map
    global stack
    global stack1
    global currCol
    global currLine
    global currCol1
    global currLine1
    global matrix
    
    while(q<=3 and w<=3):
        print("\nn o m debe ser mayor a 3")
        w = int(input("Dame el alto de la matriz: "))
        q = int(input("Dame el ancho de la matriz: "))
        
    rows, cols = (q, w)
    matrix=[]
    
    for i in range(rows):
        col = []
        for j in range(cols):
            if(i==0 or j==0 or j==w-1 or i==q-1):
                col.append(1)
            else:
                col.append(0)
        matrix.append(col)
    
    currLine = q-2
    currCol = w-2
    stack = [Node(q-2, w-2)]
    solution = [Node(q-2, w-2)]
    
    createWorld(matrix,q,w)
    
    start = time.time() #inicio
    
    while (mapNotClean()):
        try:
            path1 = discoverPath1()
            x1 = path1.get_x()
            y1 = path1.get_y()
            print("1",path1)
            path = discoverPath()
            x = path.get_x()
            y = path.get_y()
            print("2",path)
        except AttributeError:
            path = discoverPath1()
            x = path1.get_x()
            y = path1.get_y()
            
            
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
       
    inicio=time.time()
    tiempo=0
    i=q*w
    for x in range(i):
        if(tiempo>=t+0.02):
            renderMatrix(presentationMatrix)
            messagebox.showinfo("!!!!","Limite de tiempo excedido")
            break
        else:
            try:
                path1=solution1[x]
                path=solution[x]
                currCol1 = path1.get_y()
                currLine1 = path1.get_x()
                currCol = path.get_y()
                currLine = path.get_x()
                #renderMatrix(presentationMatrix)
                if (presentationMatrix[currLine1][currCol1] == 2):
                    presentationMatrix[currLine1][currCol1] = 0
                if (presentationMatrix[currLine][currCol] == 2):
                    presentationMatrix[currLine][currCol] = 0
                print(tiempo)
                tiempo = time.time()-inicio
                renderMatrix(presentationMatrix)
            except IndexError:
                try:
                    path1=solution[x]
                    path=solution[x]
                    currCol1 = path1.get_y()
                    currLine1 = path1.get_x()
                    currCol = path.get_y()
                    currLine = path.get_x()
                    renderMatrix(presentationMatrix)
                    if (presentationMatrix[currLine1][currCol1] == 2):
                        presentationMatrix[currLine1][currCol1] = 0
                    if (presentationMatrix[currLine][currCol] == 2):
                        presentationMatrix[currLine][currCol] = 0
                    print(tiempo)
                    tiempo = time.time()-inicio
                    renderMatrix(presentationMatrix)
                except IndexError:
                    try:
                        path1=solution1[x]
                    except IndexError:
                        path1=solution[x]
                    except:
                        path1=solution1[x]
                        path=solution[x]
                    currCol1 = path1.get_y()
                    currLine1 = path1.get_x()
                    currCol = path.get_y()
                    currLine = path.get_x()
                    renderMatrix(presentationMatrix)
                    if (presentationMatrix[currLine1][currCol1] == 2):
                        presentationMatrix[currLine1][currCol1] = 0
                    if (presentationMatrix[currLine][currCol] == 2):
                        presentationMatrix[currLine][currCol] = 0
                    print(tiempo)
                    tiempo = time.time()-inicio
                    renderMatrix(presentationMatrix)
            except IndexError:
                try:
                    path1=solution1[x]
                    path=solution1[x]
                except IndexError:
                    path1=solution1[x]
                    path=solution[x]
                    currCol1 = path1.get_y()
                    currLine1 = path1.get_x()
                    currCol = path.get_y()
                    currLine = path.get_x()
                    renderMatrix(presentationMatrix)
                    if (presentationMatrix[currLine1][currCol1] == 2):
                        presentationMatrix[currLine1][currCol1] = 0
                    if (presentationMatrix[currLine][currCol] == 2):
                        presentationMatrix[currLine][currCol] = 0
                    renderMatrix(presentationMatrix)
                    print(tiempo)
                    tiempo = time.time()-inicio
                    
    messagebox.showinfo("Tarea","Tiempo de limpieza: " +str("%.3f"%tiempo) + " segundos")
    
    messagebox.showinfo(
        "Tarea","Cantidad de movimientos:\n" +
        "1._"+(len(solution) - 1) + "\n"+
        "2._"+(len(solution1) - 1)
        )
    
    
if __name__ == "__main__":
    t=int(input("Ingresa el tiempo limite "))
    main(t)