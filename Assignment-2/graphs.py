#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: May 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" GRAPHS
    Functions that perform operations on graph data structures, and respective tests """  

from typing import List, Dict

### EXERCISE 1 ###
# prevent KeyErrors by ensuring that key args exist in the graph
# if they don't, nothing should happen

# Implementation of (undirected) graph using adjacency list
class GraphNode:
    def __init__(self, data):
        self.data = data 

class GraphWithAdjacencyList:
    def __init__(self, adjNodes={}):
        self.adjNodes = adjNodes # Dict[GraphNode, List[GraphNode]]
    
    def addNode(self, key: int):
        ''' Adds a new node to the graph. '''
        if key not in self.adjNodes:
            self.adjNodes.update({key: []}) # mapped to empty list for now

    def removeNode(self, key: int): 
        ''' Removes the node from the graph. '''
        # check that the node (key) exists
        if key in self.adjNodes:
            del self.adjNodes[key]
    
    def addEdge(self, node1: int, node2: int):
        ''' Adds an edge between node1 and node2. '''
        # check that both nodes (keys) exist
        if node1 in self.adjNodes and node2 in self.adjNodes:
            # prevent duplicates
            if node2 not in self.adjNodes[node1]: 
                self.adjNodes[node1].append(node2)
                self.adjNodes[node2].append(node1)
    
    def removeEdge(self, node1: int, node2: int):
        ''' Removes an edge between node1 and node2. '''
        # check that both nodes (keys) exist
        if node1 in self.adjNodes and node2 in self.adjNodes:
            # check that the edge exists
            if node2 in self.adjNodes[node1] and node1 in self.adjNodes[node2]:
                self.adjNodes[node1].remove(node2)
                self.adjNodes[node2].remove(node1)
    
    def getAdjNodes(self, key: int) -> List[GraphNode]: 
        ''' Get nodes that are connected to the node represented by 'key'. '''
        # check that the node(key) exists
        if key in self.adjNodes:
            return self.adjNodes[key]
        
    # EXTRA
    def printNodes(self):
        ''' Utility print method for the nodes in the graph. '''
        print(self.adjNodes)
    
    ### EXERCISE 2-3 ###
    # traversals are for directed graphs

    def DFS(self, key: int):
        ''' Traverse graph via DFS starting from 'key'. Print each node along the way. '''

    def BFS(self, key: int):
        ''' Traverse graph via BFS starting from 'key'. Print each node along the way. '''


# ----- TESTS -----

def undirectedGraph(): 
    # create following graph
    # Node1 -> Node2, Node4
    # Node2 -> Node1
    # Node3
    # Node4 -> Node1
    # {1: [2, 4], 2: [1], 3: [], 4: [1]}
    g = GraphWithAdjacencyList()
    
    ### note that all edge cases commented should have NO effects 

    print("--- Adding nodes ---")
    g.addNode(1)
    g.addNode(2)
    g.addNode(3)
    g.addNode(4)
    g.addNode(5)
    g.printNodes()
    # {1: [], 2: [], 3: [], 4: [], 5: []}

    print("--- Removing nodes ---")
    g.removeNode(5) 
    g.removeNode(8) # remove a node that does not exist
    g.printNodes()
    # {1: [], 2: [], 3: [], 4: []}

    print("--- Adding edges ---")
    g.addEdge(1, 2)
    g.addEdge(1, 2) # add a duplicate edge
    g.addEdge(2, 1) # add a duplicate edge (flipped order)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(1, 8) # add an edge where one node does not exist
    g.addEdge(8, 9) # add an edge where neither node exists
    g.printNodes()
    # {1: [2, 4], 2: [1, 3], 3: [2], 4: [1]}

    # how are loops handled?
    # g.addEdge(3, 3)
    # {1: [2, 4], 2: [1, 3], 3: [3, 3, 2], 4: [1]}
    
    print("--- Removing edges ---")
    g.removeEdge(3, 2) # remove edge order should not matter
    g.removeEdge(3, 2) # remove an edge that has already been removed 
    g.removeEdge(2, 3) # remove an edge that has already been removed (flipped order) 
    g.removeEdge(1, 8) # remove an edge where one node does not exist
    g.removeEdge(8, 9) # remove an edge where neither node exists
    g.printNodes()
    # {1: [2, 4], 2: [1], 3: [], 4: [1]}

    print("--- Printing adjacent nodes ---")
    print(g.getAdjNodes(1)) # [2, 4]
    print(g.getAdjNodes(3)) # []
    print(g.getAdjNodes(4)) # [1]
    print(g.getAdjNodes(8)) # None (node does not exist)

def directedGraphDFS(): 
    dfsGraph = GraphWithAdjacencyList()
    dfsGraph.addNode(0)
    dfsGraph.addNode(1)
    dfsGraph.addNode(2)
    dfsGraph.addNode(3)

    # add outgoing edges
    dfsGraph.addEdge(0, 1)
    dfsGraph.addEdge(0, 2)
    
    dfsGraph.printNodes()

    # does edge order matter? e.g. 0 -> 2, 1

if __name__ == "__main__": 
    # undirectedGraph() # Exercise 1
    directedGraphDFS()