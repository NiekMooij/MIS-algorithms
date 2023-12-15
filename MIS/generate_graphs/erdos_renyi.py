import random
import networkx as nx

def erdos_renyi(size: int, p: float) -> nx.Graph:
    """
    Generate an Erdős-Rényi random graph.

    Parameters:
    - size (int): The number of nodes in the graph.
    - p (float): The probability of an edge between any two nodes.

    Returns:
    - nx.Graph: The generated Erdős-Rényi graph.
    """
    # Create an empty graph
    G = nx.Graph()

    # Add nodes to the graph
    G.add_nodes_from(range(1, size + 1))

    # Continue adding edges until the graph becomes connected
    while not nx.is_connected(G):
        # Create a list of all possible edges
        edge_arr = [(i, j) for i in G.nodes() for j in G.nodes() if i < j]

        # Add edges with probability p
        for edge in edge_arr:
            if random.random() < p:
                G.add_edge(*edge)

    return G