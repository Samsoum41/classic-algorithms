"""
Here is an implementation of the Dijkstra algorithm

To test the solution, I use graphs and results from this page : http://dominique.frin.free.fr/terminales/exosTES-Dijkstra-cor.pdf

"""

"""

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
"""
# It is the graph of the 6th exercise on the link. I've replaced letters by numbers (A->0, B->1...)
graph1_list =[   
    {(4,6), (3,10), (1,5)},
    {(0,5), (2,5)},
    {(1,5), (3,7), (6,3)},
    {(0,10), (2,7), (4,3), (5,1), (6,4)},
    {(0,6), (3,3), (5,5)},
    {(4,5), (3,1), (6,2)},
    {(3,4), (5,2), (2,3)}
] 

graph1_matrix = [
    [0, 5, 0, 10, 6, 0, 0], 
    [5, 0, 5, 0, 0, 0, 0], 
    [0, 5, 0, 7, 0, 0, 3], 
    [10, 0, 7, 0, 3, 1, 4], 
    [6, 0, 0, 3, 0, 5, 0], 
    [0, 0, 0, 1, 5, 0, 2], 
    [0, 0, 3, 4, 0, 2, 0]
]

# Here we work on an adjacency matrix
graph2_list = [
    {(1, 4), (2, 8)}, 
    {(0, 4), (2, 7), (3, 18), (4, 21)}, 
    {(0, 8), (1, 7), (3, 10), (5, 25)}, 
    {(1, 18), (2, 10), (4, 15), (5, 12), (6, 31)}, 
    {(1, 21), (3, 15), (5, 10), (6, 17)}, 
    {(2, 25), (3, 12), (4, 10), (6, 7)}, 
    {(3, 31), (4, 17), (5, 7)}
]
graph2_matrix = [
    [0,4,8,0,0,0,0],
    [4,0,7,18,21,0,0],
    [8,7,0,10,0,25,0],
    [0,18,10,0,15,12,31],
    [0,21,0,15,0,10,17],
    [0,0,25,12,10,0,7],
    [0,0,0,31,17,7,0],
]

def from_adjacencyMatrix_to_adjacencyList(matrix):
    n = len(matrix)
    return [{(j,matrix[i][j]) for j in range(n) if matrix[i][j]>0} for i in range(n)]

def from_adjacencyList_to_adjacencyMatrix(array):
    n = len(array)
    result =  [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for el in array[i]:
            result[i][el[0]] = el[1]
    return result

