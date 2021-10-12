"""
Here is a test file of the Dijkstra algorithm, with graph described by adjacency list or matrix.

To test the solution, I use graphs and results from this page : http://dominique.frin.free.fr/terminales/exosTES-Dijkstra-cor.pdf
Note that I have replaced letters by numbers (A->0, B->1...) :

A = 0
B = 1
C = 2
D = 3
E = 4
F = 5
G = 6
"""
import unittest
import Dijkstra 

class TestDijkstraFunctions(unittest.TestCase):
    def test_from_adjacancyList_to_adjacancyMatrix(self):
        self.assertEqual(Dijkstra.graph1_matrix, Dijkstra.from_adjacencyList_to_adjacencyMatrix(Dijkstra.graph1_list))
        self.assertEqual(Dijkstra.graph2_matrix, Dijkstra.from_adjacencyList_to_adjacencyMatrix(Dijkstra.graph2_list))
    def test_from_adjacancyMatrix_to_adjacancyList(self):
        self.assertEqual(Dijkstra.graph1_list, Dijkstra.from_adjacencyMatrix_to_adjacencyList(Dijkstra.graph1_matrix))
        self.assertEqual(Dijkstra.graph2_list, Dijkstra.from_adjacencyMatrix_to_adjacencyList(Dijkstra.graph2_matrix))
    def test_dijkstra(self):
        self.assertEqual((12,[0,4,3,5,6]), Dijkstra.dijkstra(Dijkstra.graph1_matrix))
        self.assertEqual((37,[0,2,3,5,6]))


if __name__ == '__main__':
    unittest.main()