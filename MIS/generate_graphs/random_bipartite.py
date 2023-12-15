import random
import networkx as nx

def random_bipartite(sizeA: int, sizeB: int, p: float) -> nx.Graph:
    """
    Generate a random bipartite graph.

    Parameters:
    - sizeA (int): Number of vertices in set A.
    - sizeB (int): Number of vertices in set B.
    - p (float): Probability of an edge between vertices in set A and set B.

    Returns:
    - nx.Graph: Bipartite graph with nodes labeled from 1 to sizeA+sizeB.
    """
    # Create an empty bipartite graph
    G = nx.Graph()

    # Define nodes for set A and set B
    A_vertices = list(range(1, sizeA + 1))
    B_vertices = list(range(sizeA + 1, sizeA + sizeB + 1))

    # Add nodes to the graph with bipartite attribute
    G.add_nodes_from(A_vertices, bipartite=0)
    G.add_nodes_from(B_vertices, bipartite=1)

    # Ensure the graph is connected
    while not nx.is_connected(G):
        # Re-initialize the graph and nodes
        G = nx.Graph()
        A_vertices = list(range(1, sizeA + 1))
        B_vertices = list(range(sizeA + 1, sizeA + sizeB + 1))
        G.add_nodes_from(A_vertices, bipartite=0)
        G.add_nodes_from(B_vertices, bipartite=1)

        # Add edges with probability p
        for vertexA in A_vertices:
            for vertexB in B_vertices:
                if random.random() < p:
                    G.add_edge(vertexA, vertexB)

    return G