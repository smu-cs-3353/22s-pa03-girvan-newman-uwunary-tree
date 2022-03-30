from networkx import graphml
import networkx as nx
from collections import deque
import numpy as np
import random
from collections import deque
import math





# Parameters
inFile = "../data/dataset.graphml"  # The datafile to load in
nodeSubsetPercent = 0.8             # Number of random nodes to pick in the betweeness algorithm
betThreshold = 4                    # Threshold betweeness value to remove
    
    
    
class Node:
    # Initialze the node
    # Input:
    #   value - The value of the node
    #   level - The level of the node in the tree 
    def __init__(self, value, level):
        self.val = value        # Value stored in the node
        self.shortestPaths = 1  # The number of shortest paths that can
                                # reach this node from the root
        self.children = []      # Children of this node
        self.parents = []       # The parents of this node
        self.sameLevel = []     # Nodes on same level as this one
        self.level = level      # The level of the node
        self.labeled = False
    
    # Test if two nodes are equal
    # Inputs:
    #   n - A node to test against this node
    def __eq__(self, n):
        return n.val == self.val
    
    # Add a child to this node
    # Input:
    #   c - A child node to add to this node
    def addChild(self, c):
        self.children.append(c)
        c.parents.append(self)
    
    # Add a parent to this node
    # Input:
    #   p - The parent to add to this node
    def addParent(self, p):
        self.parents.append(p)
        p.children.append(self)
        self.shortestPaths += 1
        
    # True if the given node is a child of this node, false otherwise
    # Inputs:
    #   n - A node to look for in this node's children
    def isChild(self, n):
        return n in self.c



# Inputs:
#   node - A node of the tree of the graph in tree form
#   parent - The parent of the given node to examine
#   edges - A dictionary of edges to add edges to
# Output:
#   None (edges is changed in the function)
def edgeLabelling(node, parent, edges):
    if node.labeled == True:
        # Divide the betweeness between the parent nodes
        if len(node.children) == 0:
            betweeness = 1/float(len(node.parents))
        else:
            betweeness = node.shortestPaths/float(len(node.parents))
        
        # Store the betweeness of this node and its parent
        try: # Does the key (parent, child) exist?
            edges[(parent.val, node.val)] += betweeness
        except KeyError:
            try: # Does the key (child, parent) exist?
                edges[(node.val, parent.val)] += betweeness
            except KeyError:
                # Add the key (parent, child)
                edges[(parent.val, node.val)] = betweeness
        return
    
    # If node is a root node, iterate to the child nodes and
    # calculate their betweeness
    
    # If node is a leaf, calculate the betweeness of
    # the edges between it and it's parent
    if len(node.children) == 0:
        # If the node has multiple parents, divide the
        # betweeness value
        betweeness = 1/float(len(node.parents))
        
        
        
        ## Store the betweeness
        
        try: # Does the key (parent, child) exist?
            edges[(parent.val, node.val)] += betweeness
        except KeyError:
            try: # Does the key (child, parent) exist?
                edges[(node.val, parent.val)] += betweeness
            except KeyError:
                # Add the key (parent, child)
                edges[(parent.val, node.val)] = betweeness
    
    # If the node is not a leaf node
    else:
        # Calculate the betweness of all its children
        for c in node.children:
            edgeLabelling(c, node, edges)
        
        # The betweeness is equal to 1 plus the edges of its children
        betweeness = 1
        for c in node.children:
            try: # Does the key (node, child) exist?
                betweeness += edges[(node.val, c.val)]
            except KeyError:
                try: # Does the key (child, node) exist?
                    betweeness += edges[(c.val, node.val)]
                except KeyError:
                    # If the key does not exist, raise an error
                    raise RuntimeError("Key must exist")
        
        # Update the shortestPaths value of the node
        node.shortestPaths = betweeness
        
        # Divide the betweeness between the parent nodes
        betweeness /= float(len(node.parents))
        
        # Store the betweeness of this node and its parent
        try: # Does the key (parent, child) exist?
            edges[(parent.val, node.val)] += betweeness
        except KeyError:
            try: # Does the key (child, parent) exist?
                edges[(node.val, parent.val)] += betweeness
            except KeyError:
                # Add the key (parent, child)
                edges[(parent.val, node.val)] = betweeness
        
    node.labeled = True



# Inputs:
#   G - The graph to use
#   n - The node to find all paths from
#   edges - A dictionary of edges to add edges to
# Output:
#   None (edges is changed in the function)
def single_source_shortest_path(G, n, edges):
    # The visited nodes
    visited = []
    
    # Initialize the tree to the root node
    tree = Node(n, 1)
    
    
    
    
    ### Step 1 and 2 - Breadth First Search and Node Labelling
    
    # Stack used for BFS
    s = deque()
    
    # push the root node
    s.append(tree)
    visited.append(tree)
    
    # BFS variables
    curNode = tree.val  # Stores the current node being examined
    subTree = tree      # Subtree of the entire tree used to add more nodes
    level = 1           # The current level of the tree
    
    # Iterate until the queue is empty
    while s:
        # Dequeue the stack
        cur = s.pop()
        
        # The current level is the level of the current node + 1
        level = cur.level + 1
        
        # Iterate over all nodes adjacent to this node
        for n in list(G.neighbors(cur.val)):
            
            node = Node(n, level)
            try:
                # Try to get the index of the node
                # in the visited list
                loc = visited.index(node)
                
                # Get the node
                node = visited[loc]
                
                # If this node is equal to the level of cur,
                # set them as equal levels
                if node.level == cur.level:
                    if cur not in node.sameLevel:
                        node.sameLevel.append(cur)
                        cur.sameLevel.append(node)
                # If this node has a smaller level than the current
                # node, set this node as the parent of the current node
                elif node.level < cur.level:
                    if node not in cur.parents:
                        cur.addParent(node)
                
            
            # If the node isn't visited, push it and add
            # it to the tree
            except ValueError:
                s.append(node)
                visited.append(node)
                cur.addChild(node)
    
    
    
    
    ### Step 3 - edge labelling
    
    # Iterate over all children of the root node
    bet = dict()
    for c in tree.children:
        edgeLabelling(c, tree, bet)
    
    # Add the betweeness to the total edges dictionary
    for edge in bet.keys():
        try: # Does the edge exist?
            edges[edge] += bet[edge]/2
        except KeyError:
            try: # Does the reverse of the edge exist?
                edges[(edge[1], edge[0])] += bet[edge]/2
            except KeyError:
                # If the edge does not exist, add it
                edges[edge] = bet[edge]/2
    
    # Return the edges
    return edges



# Inputs:
#   G - The graph to use
# Output
#   edges - The betweeness between all edges
def calculateBetweeness(G):
    # The betweeness of the graph
    # map:   edge -> betweeness
    betweeness = dict()
    
    # Get a subset of the graph
    e = list(G.edges)
    random.shuffle(e)
    sub = G.edge_subgraph(e[:int(len(e)*nodeSubsetPercent)])
    
    # Iterate over all nodes
    for n in list(sub.nodes):
        # Calculate the betweeness for all paths from that node
        single_source_shortest_path(sub, n, betweeness)
    
    # Return the betweeness
    return betweeness




# Input:
#   G - The graph to iterate
#   node - The node to look at in the graph
#   visited - The already visited nodes
def findCommunities(G, node, visited):
    # Iterate over all nodes adjacent to this node
    # and add them to the visited nodes
    for n in list(G.neighbors(node)):
        # If the node hasn't been visited, add it
        # to the community and visit its neighbors
        if n not in visited:
            visited.append(n)
            findCommunities(G, n, visited)
                




def main():
    # Read in the graph and store data on it
    G = graphml.read_graphml(inFile)
    
    # Iterate until the Q value is no longer increasing
    Q_prev = -np.inf
    Q = -np.inf
    maxBetweeness = [0]
    while (Q >= Q_prev):#len(G.edges) and len(maxBetweeness) > 0):
        # Update the Q_prev value
        Q_prev = Q
        
        # Calculate the betweeness of all edges in the graph
        betweeness = calculateBetweeness(G)
        
        # Get the edges with the max betweeness
        #maxBetweeness = np.argwhere(np.array(list(betweeness.values()), dtype=np.float16) == list(betweeness.values())[np.argmax(np.array(list(betweeness.values()), dtype=np.float16))])
        maxBetweeness = np.argwhere(np.array(list(betweeness.values()), dtype=np.float16) >= 3*math.log2(len(list(G.edges))))
        
        # Store the number of edges before removing any edges (m)
        m = len(list(G.edges))
        
        # Store the old graph
        oldG = G.copy()
        
        # Remove all max edges from the graph
        for edge in maxBetweeness:
            e = list(betweeness.keys())[edge.item()]
            G.remove_edge(e[0], e[1])
        
        
        
        
        
        ### Compute the modularity (Q)
        # https://www.pnas.org/doi/full/10.1073/pnas.0601602103#FD3
        
        # Compute the differences B_ij
        # - B_ij = (A - (k_i-k_j)/2m)
        #    - A = 1 if an egde is between node i and j
        #           in the new graph
        #    - k_i = degree of node i
        #    - k_j = degree of node j
        #    - m = number of edges in the old graph
        # - s_i * s_j = 1 if i and j are in the same group, -1 otherwise
        # - sum1 = The first summation
        #    - sum_ij[ B_ij*(s_i*s_j +1) ]
        # - sum2 = The second summation
        #    - sum_ij[ B_ij ]
        
        # Iterate over all nodes in the old graph (i)
        sum1 = 0
        sum2 = 0
        for i in list(oldG.nodes):
            # Iterate over all nodes in the new graph (j)
            for j in list(G.nodes):
                # Calculate the B value
                k_i = len(list(G.neighbors(i)))
                k_j = len(list(G.neighbors(j)))
                A = 1 if ((i, j) in G.edges or (j, i) in G.edges) else 0
                
                B = A - (k_i*k_j)/2*m
                
                
                # Calculate the s value (s_i * s_j) + 1
                comm = []
                findCommunities(G, i, comm)
                s = 1 if j in comm else -1
                s += 1
                
                # Compute the B values to be summed
                B_1 = B*s
                B_2 = B
                
                # Store the B values
                sum1 += B_1
                sum2 += B_2
        
        # Compute the final Q value
        Q = (1/2*m)*(0.5*sum1 - sum2)
        
        print()
        
    Q = oldG
        
    # Iterate over all nodes and find the communities
    comm = []           # The communities found
    totalVisited = []   # The total visited nodes
    for node in list(G.nodes):
        # If the node has been visited, skip this iteration
        if node in totalVisited:
            continue
    
        visited = []    # The nodes that were visited already
        findCommunities(G, node, visited)
        
        # Add the visited nodes to the communities
        if len(visited) != 0:
            comm.append(visited)
        else:
            comm.append([node])
        
        # Add the visited nodes to the total visited nodes
        totalVisited += visited
    
    c = nx.community.girvan_newman(G) 
    k = 3   # number of communities
    for _ in range(k-1):
        comms = next(c)
    print()



main()