#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: June 2022
# ---------------------------------------------------------------------------
""" GRAPHS
    Functions that perform operations on graph data structures, and respective tests """  

from typing import List, Dict

### EXERCISE 1 ###
# prevent KeyErrors by checking that nodes (associated with key args) exist in the graph
# if they don't, nothing should happen

# Implementation of (undirected) graph using adjacency list
class GraphNode:
    def __init__(self, data: int):
        self.data = data 

class GraphWithAdjacencyList:
    def __init__(self):
        self.adjList = {}       # Dict[GraphNode, List[GraphNode]]
        self.keyNodeDict = {}   # Dict[int, GraphNode] - used to remove nodes by key
    
    def addNode(self, key: int):
        ''' Adds a new node to the graph. '''
        if key not in self.keyNodeDict: 
            newNode = GraphNode(key)
            self.adjList.update({newNode: []}) # mapped to empty list for now
            self.keyNodeDict[key] = newNode

    def removeNode(self, key: int): 
        ''' Removes the node from the graph. '''
        if key in self.keyNodeDict and self.keyNodeDict[key] in self.adjList:
            del self.adjList[self.keyNodeDict[key]]
            del self.keyNodeDict[key]      
    
    def addEdge(self, key1: int, key2: int):
        ''' Adds an edge between the nodes associated with key1 and key2. '''
        if key1 in self.keyNodeDict and key2 in self.keyNodeDict:
            node1 = self.keyNodeDict[key1]
            node2 = self.keyNodeDict[key2]
            # prevent duplicates
            if node1 not in self.adjList[node2]: 
                self.adjList[node1].append(node2)
                self.adjList[node2].append(node1)
    
    def removeEdge(self, key1: int, key2: int):
        ''' Removes an edge between node1 and node2. '''
        if key1 in self.keyNodeDict and key2 in self.keyNodeDict:
            node1 = self.keyNodeDict[key1]
            node2 = self.keyNodeDict[key2]
            # check that the edge exists
            if node2 in self.adjList[node1] and node1 in self.adjList[node2]:
                self.adjList[node1].remove(node2)
                self.adjList[node2].remove(node1)
    
    def getAdjNodes(self, key: int) -> List[GraphNode]: 
        ''' Get nodes that are connected to the node represented by 'key'. '''
        # check that the node (key) exists
        if key in self.keyNodeDict:
            return self.adjList[self.keyNodeDict[key]]
        
    # EXTRA UTILITY METHODS
    def printNodes(self):
        for node in self.adjList:
            print(str(node.data))

    def printAdjNodes(self):
        for node in self.adjList:
            print("edges of " + str(node.data))
            for adjNode in self.adjList[node]:
                print(str(node.data) + "->" + str(adjNode.data))
            print("\n")
    
    ### EXERCISE 2-3 ###
    # traversals are for directed graphs

    def dfs(self, key: int):
        ''' Traverse graph via DFS starting from 'key'. Print each node along the way. '''
        if key not in self.keyNodeDict:
            return 
        
        visited = set() # global variable
        dfsHelper(self.keyNodeDict(key))

        def dfsHelper(currNode, visited):
            # base case -- node has already been visited
            if currNode in visited:
                return
            
            # mark as visited  
            print(currNode.data)
            visited.add(currNode)

            # explore all neighbors
            for adjNode in self.adjList(currNode):
                dfsHelper(adjNode, visited)

    def bfs(self, key: int):
        ''' Traverse graph via BFS starting from 'key'. Print each node along the way. '''
        if key not in self.keyNodeDict:
            return

        q = []
        visited = set()

        q.append(self.keyNodeDict[key])
        while q:
            prevNode = q.pop(0)

            if prevNode not in visited:
                # mark as visited
                print(prevNode.data)
                visited.add(prevNode)

                # explore all neighbors
                for adjNode in self.adjList[prevNode]:
                    if adjNode not in visited:
                        q.append(adjNode)


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
    # # {1: [], 2: [], 3: [], 4: []}

    print("--- Adding edges ---")
    g.addEdge(1, 2)
    g.addEdge(1, 2) # add a duplicate edge
    g.addEdge(2, 1) # add a duplicate edge (flipped order)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    g.addEdge(1, 8) # add an edge where one node does not exist
    g.addEdge(8, 9) # add an edge where neither node exists
    g.printAdjNodes()
    # {1: [2, 4], 2: [1, 3], 3: [2], 4: [1]}

    # TODO
    # how are loops handled?
    # g.addEdge(3, 3)
    
    print("--- Removing edges ---")
    g.removeEdge(3, 2) # remove edge order should not matter
    g.removeEdge(3, 2) # remove an edge that has already been removed 
    g.removeEdge(2, 3) # remove an edge that has already been removed (flipped order) 
    g.removeEdge(1, 8) # remove an edge where one node does not exist
    g.removeEdge(8, 9) # remove an edge where neither node exists
    g.printAdjNodes()
    # # {1: [2, 4], 2: [1], 3: [], 4: [1]}

    print("--- Printing adjacent nodes ---")
    print(g.getAdjNodes(1)) # [2, 4]
    print(g.getAdjNodes(3)) # []
    print(g.getAdjNodes(4)) # [1]
    print(g.getAdjNodes(8)) # None (node does not exist)

def dfsBfsGraphs(): 
    graph = GraphWithAdjacencyList()
    graph.addNode(0)
    graph.addNode(1)
    graph.addNode(2)
    graph.addNode(3)

    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)

    graph.printAdjNodes()
    
    # graph.dfs(0)
    graph.bfs(0)

if __name__ == "__main__": 
    # undirectedGraph()   # Exercise 1
    dfsBfsGraphs()      # Exercise 2 -- UnboundLocalError, Exercise 3