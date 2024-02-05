import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

# Define the used color palette
cud_palette = [
    '#0101fd',  # Blue
    '#E69F00',  # Orange
    '#000000',  # Black
    '#ff0101',  # Red
    '#0072B2',  # Blue
    '#D55E00',  # Vermilion
    '#CC79A7',  # Reddish Purple
    '#F95C99',  # Reddish Pink
    '#999999',  # Gray
    '#CC61B0',  # Pink
    '#F95C99',  # Reddish Pink
]

fig, ax1 = plt.subplots(figsize=(8,6))

size = 1200

# First draw the open edges
H = nx.Graph()
H.add_node('B', label_name='+', loc=(2,3), color=cud_palette[1], node_size=size, label_size = 16)
H.add_node('F', label_name='+', loc=(1,-1), color=cud_palette[1], node_size=size, label_size = 16)
H.add_node('I', label_name='+', loc=(7,2), color=cud_palette[1], node_size=size, label_size = 16)
H.add_node('H', label_name='+', loc=(7,0), color=cud_palette[1], node_size=size, label_size = 16)

H.add_node('1', loc=(6,-2))
H.add_node('2', loc=(8,-2))
H.add_node('3', loc=(0,-2))
H.add_node('4', loc=(3,4))
H.add_node('5', loc=(6.5,3.5))
H.add_node('6', loc=(8,3.5))

H.add_edge('H', '1', linestyle='dotted')
H.add_edge('H', '2', linestyle='dotted')
H.add_edge('F', '3', linestyle='dotted')
H.add_edge('B', '4', linestyle='dotted')
H.add_edge('I', '5', linestyle='dotted')
H.add_edge('I', '6', linestyle='dotted')

pos = nx.get_node_attributes(H, 'loc')
colors = [ 'white' for node in H.nodes() ]
edge_width = 2

nx.draw_networkx_edges(H, ax=ax1, pos=pos, alpha=1, width=edge_width, style='dashed')


# Then draw the rest of the network
G = nx.Graph()
G.add_node('A', label_name='+', loc=(0,2), color=cud_palette[1], node_size=size, label_size = 16)
G.add_node('B', label_name='+', loc=(2,3), color=cud_palette[1], node_size=size, label_size = 16)
G.add_node('C', label_name='-', loc=(4,2), color=cud_palette[0], node_size=size, label_size = 24)
G.add_node('D', label_name='-', loc=(2,0), color=cud_palette[0], node_size=size, label_size = 24)
G.add_node('E', label_name='s', loc=(4,0), color=cud_palette[3], node_size=size, label_size = 16)
G.add_node('F', label_name='+', loc=(1,-1), color=cud_palette[1], node_size=size, label_size = 16)
G.add_node('G', label_name='-', loc=(6,1), color=cud_palette[0], node_size=size, label_size = 24)
G.add_node('H', label_name='+', loc=(7,0), color=cud_palette[1], node_size=size, label_size = 16)
G.add_node('I', label_name='+', loc=(7,2), color=cud_palette[1], node_size=size, label_size = 16)
G.add_node('J', label_name='-', loc=(9,1), color=cud_palette[0], node_size=size, label_size = 24)

G.add_edge('A', 'B')
G.add_edge('B', 'C')
G.add_edge('A', 'D')
G.add_edge('B', 'D')
G.add_edge('D', 'E')
G.add_edge('D', 'F')
G.add_edge('C', 'I')
G.add_edge('E', 'G')
G.add_edge('G', 'H')
G.add_edge('G', 'I')
G.add_edge('I', 'H')
G.add_edge('H', 'J')

pos = nx.get_node_attributes(G, 'loc')
colors =list(nx.get_node_attributes(G, 'color').values())
node_size = list(nx.get_node_attributes(G, 'node_size').values())
labels = { node: list(nx.get_node_attributes(G, 'label_name').values())[i] for i, node in enumerate(G.nodes()) }
node_font_sizes = {node: list(nx.get_node_attributes(G, 'label_size').values())[i] for i, node in enumerate(G.nodes())}
edge_width = 2

nx.draw(G, pos=pos, ax=ax1, node_color=colors, with_labels=False, linewidths=1, edgecolors='black', node_size=node_size, width=edge_width)

# Draw node labels with individual font sizes
for node, (x, y) in pos.items():
    ax1.text(x, y, labels[node], color='white', fontsize=node_font_sizes[node], ha='center', va='center')

plt.savefig(os.path.join(sys.path[0], 'Figure3.pdf'), dpi=900, transparent=True, bbox_inches='tight')
plt.show()