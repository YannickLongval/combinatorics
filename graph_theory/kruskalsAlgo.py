# This script implements Kruscal's Algorithm, and uses networkx to viualize the graph with the spanning tree

import networkx as nx
import matplotlib.pyplot as plt

# Original graph represented as a set of nodes, and a dictionary of the edges with their respective weights
# Important to note that the objects that are being used as nodes should match the objects in the edges
graph_nodes:set[object] = {1, 2, 3, 4, 5}
graph_edges:dict[tuple[object,object], int] = {(1, 2): 5, (1, 4): 3, (1, 5): 1, (2, 3): 6, (4, 5): 1, (3, 4): 2}

# Check if there is a cycle in the list of edges
def isCycle(edges:list[tuple[int, int]])->bool:
    # A list to keep track of the different connections in the graph
    connected_nodes:list[list[int]] = []

    for edge in edges:
        connected:bool = False
        for connection in connected_nodes:
            # Checking if the nodes of the edge are in any of the connections
            # Both nodes in the same connection means a cycle has been formed
            if edge[0] in connection and edge[1] in connection:
                return True
            if edge[0] not in connection and edge[1] in connection:
                connection.append(edge[0])
                connected = True
            if edge[1] not in connection and edge[0] in connection:
                connection.append(edge[1])
                connected = True
        # if not connected, then create a new connection in connected_nodes
        if not connected:
            connected_nodes.append([edge[0], edge[1]])
    return False

# To determine which edge to add, we need to find the lowest-weighted edge,
# that does not create a cycle with the existing spanning tree
def getEdge(edges:dict[tuple[object,object], int], spanningEdges:dict[tuple[object,object], int])->tuple[tuple[int, int], int]:
    lowestEdge:tuple[object, object] = ()
    lowestWeight:int = 0
    for edge in edges:
        if not isCycle(list(spanningEdges.keys())+[edge]) and (edges[edge] < lowestWeight or lowestWeight == 0):
            lowestWeight = edges[edge]
            lowestEdge = edge
    return lowestEdge, lowestWeight

# Implementation of Kruskals algorithm to find a 
# minimal weight spanning tree for the graph
# The algorithm is as follows:
# Choose the edge of least weight
# Choose the next least edge that does not produce a cycle
# Stop after you've chosen n-1 edges
def kruskal(nodes:set[object], edges:dict[tuple[object,object], int]) -> tuple[set[object], dict[tuple[object,object], int]]:
    count:int = 0
    spanningEdges:dict[tuple[object,object], int] = {}
    graphVisual: dict[tuple[object,object],  tuple[int, bool]] = {}
    
    while count < len(nodes)-1:
        edge, weight = getEdge(edges, spanningEdges)
        spanningEdges[edge] = weight
        count += 1

    for edge in edges.keys():
        graphVisual[edge] = (edges[edge], edge in spanningEdges.keys())
    
    draw_graph(graphVisual)
    return nodes, spanningEdges

# draw the graph with the given edges, their weights, and whether or not they are part of the spanning tree
def draw_graph(gEdges:dict[tuple[object,object], tuple[int, bool]]):
    G:nx.Graph = nx.Graph()
    labels:dict = {}
    print(gEdges)
    for edge in gEdges.keys():
        labels[(edge[0], edge[1])] = gEdges[edge][0]
        G.add_edge(edge[0], edge[1], color="red" if gEdges[edge][1] else "black", weight=4 if gEdges[edge][1] else 2)

    pos = nx.circular_layout(G)

    edges = G.edges()
    colors = [G[u][v]['color'] for u,v in edges]
    weights = [G[u][v]['weight'] for u,v in edges]

    nx.draw(G, pos, edge_color=colors, width=weights, with_labels=labels)

    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels=labels,
        font_color='black',
        rotate=False,
        font_size=10
    )
    plt.show()

span_tree_nodes:set[object] 
span_tree_edges:dict[tuple[object,object], int] 
span_tree_nodes, span_tree_edges= kruskal(graph_nodes, graph_edges)