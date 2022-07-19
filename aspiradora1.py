import matplotlib.pyplot as plt
import random
import statistics as st
from tkinter import messagebox
import time
from Node import *
from copy import copy, deepcopy


matrix = []
presentationMatrix = []

currLine = 1
currCol = 1
stack = [Node(1, 1)]
solution = [Node(1, 1)]

process_map = []


def mapNotClean():
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if (matrix[i][j] == 2):
                return True
    return False


def renderMatrix(matrix):
    plt.imshow(matrix, 'gray')
    plt.show(block=False)
    plt.plot(currCol, currLine, '*r', 'LineWidth', 5)
    plt.pause(0.1)
    plt.clf()


def createWorld(m, rows, cols):
    for mI in range(1, (rows) - 1):
        for aI in range(1, (cols) - 1):
            if (mI == 1 and aI == 1):
                continue
            number = random.randint(0, 3)
            m[mI][aI] = 2 if number == 1 else 0
    renderMatrix(matrix)
    global process_map
    global presentationMatrix
    process_map = deepcopy(matrix)
    presentationMatrix = deepcopy(matrix)


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


def main(t):

    global matrix
    global process_map
    global stack
    global currCol
    global currLine

    n = 0
    m = 0

    while(n <= 3 and m <= 3):
        print("\nn o m debe ser mayor a 3")
        n = int(input("Alto de la matriz: "))
        m = int(input("Ancho de la matriz: "))

    rows, cols = (n, m)
    matrix = []

    for i in range(rows):
        col = []
        for j in range(cols):
            if(i == 0 or j == 0 or j == m-1 or i == n-1):
                col.append(1)
            else:
                col.append(0)
        matrix.append(col)

    createWorld(matrix, n, m)

    start = time.time()  # inicio

    while (mapNotClean()):
        path = discoverPath()
        x = path.get_x()
        y = path.get_y()

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

    inicio = time.time()
    tiempo = 0

    for path in solution:
        if(tiempo >= t+0.15):
            renderMatrix(presentationMatrix)
            messagebox.showinfo("Time", "Limite de tiempo excedido")
            exit
            break
        else:
            currCol = path.get_y()
            currLine = path.get_x()
            renderMatrix(presentationMatrix)
            if (presentationMatrix[currLine][currCol] == 2):
                presentationMatrix[currLine][currCol] = 0
            print(tiempo)
        tiempo = time.time()-inicio
        renderMatrix(presentationMatrix)

    messagebox.showinfo(
        "Tarea", "Tiempo de limpieza: " + str("%.3f" % tiempo) + " segundos"
    )

    messagebox.showinfo(
        "Tarea", "Cantidad de movimientos:\n" + str(len(solution) - 1)
    )


if __name__ == "__main__":
    t = int(input("Ingresa el tiempo limite "))
    main(t)
