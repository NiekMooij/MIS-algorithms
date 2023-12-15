import random
import networkx as nx

def random_geometric(size: int, k: float) -> nx.Graph:
    """
    Generate a geometric random graph.

    Parameters:
    - size (int): The number of nodes in the graph.
    - k (float): The threshold distance for edges between nodes.

    Returns:
    - nx.Graph: The generated geometric graph.
    """
    # Create an empty graph
    G = nx.Graph()

    # Continue adding nodes until the graph becomes connected
    while not nx.is_connected(G):
        # Add nodes with random positions in the unit square
        for i in range(1, size + 1):
            x, y = random.random(), random.random()
            G.add_node(i, pos=(x, y))

        # Add edges based on the distance between nodes
        for i in range(1, size + 1):
            for j in range(i + 1, size + 1):
                x1, y1 = G.nodes[i]['pos']
                x2, y2 = G.nodes[j]['pos']
                distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
                if distance < k:
                    G.add_edge(i, j)
                        
    return G