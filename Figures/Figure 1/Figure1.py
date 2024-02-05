import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pickle
import matplotlib.gridspec as gridspec

# import data
A0 = np.load(os.path.join(sys.path[0], 'data/A0.npy'))
output_arr = np.load(os.path.join(sys.path[0], 'data/output_arr.npy'), allow_pickle=True)
bifurcation_point_arr = np.load(os.path.join(sys.path[0], 'data/bifurcation_point_arr.npy'))

with open(os.path.join(sys.path[0], 'data/pos.npy'), 'rb') as file:
    pos = pickle.load(file)
pos[3] = [ 0.3478643, -0.41109559]
pos[6] = [-0.71973279, 0.31351894]
pos[7] = [-0.31973279, -0.61351894]

# Define values
G = nx.from_numpy_array(A0)
tau_min, tau_max, step_size = 0, 1.1, 0.0001
domain = np.arange(tau_min, tau_max, step_size)

# Create the figure
fig = plt.figure(figsize=(10,10))
gs = gridspec.GridSpec(4, 28, height_ratios=[35, 3, 14, 14])
big_ax = fig.add_subplot(gs[0, :])
ax1 = fig.add_subplot(gs[2, 0:8])
ax2 = fig.add_subplot(gs[2, 10:18])
ax3 = fig.add_subplot(gs[2, 20:28])
ax4 = fig.add_subplot(gs[3, 0:8])
ax5 = fig.add_subplot(gs[3, 10:18])
ax6 = fig.add_subplot(gs[3, 20:28])
fig.subplots_adjust(wspace=0.3, hspace=0.3)

# Define the used color palette
cud_palette = [
    '#0101fd',  # Blue
    '#E69F00',  # Orange
    '#000000',  # Black
    '#D55E00',  # Vermilion
    '#CC61B0',  # Pink
    '#F95C99',  # Reddish Pink
    '#a5682a',  # Brown
    '#ff0101'   # Red
]

# Plot data
count_number = 400
size = 40
skip = 50
markers = ['o', 's', 'D', '^', 'v', 'p', 'H', '*']
labels ={0: r'$x^*_1$', 1: r'$x^*_2$', 2: r'$x^*_3$', 3: r'$x^*_4$', 4: r'$x^*_5$', 5: r'$x^*_6$', 6: r'$x^*_7$', 7: r'$x^*_8$'}
order = [ 3, 4, 0, 6, 7, 2, 5, 1 ]

# Scatter plot
for i in range(len(output_arr[0])):    
    data_index = order[i]
    x_data = domain[data_index*skip:][count_number::count_number+1]
    y_data = output_arr[data_index*skip:][:,data_index][count_number::count_number+1]
    marker = markers[i]
    color = cud_palette[len(cud_palette) -1 - i]
    label = labels[i]

    big_ax.scatter(0, output_arr[0][i], color=color, s=size, marker=marker, facecolors='none', edgecolors=color)
    big_ax.scatter(domain[40], output_arr[40][i], color=color, s=size, marker=marker, facecolors='none', edgecolors=color)
    big_ax.scatter(domain[250], output_arr[250][i], color=color, s=size, marker=marker, facecolors='none', edgecolors=color)

    big_ax.scatter(x_data, y_data, color=color, s=size, marker=marker, label=label, facecolors='none', edgecolors=color)

# Line through scatter plot
for i in range(len(output_arr[0])): 
    data_index = order[i]

    x_data = domain
    y_data = output_arr[:,data_index]
    
    marker = markers[i]
    color = cud_palette[len(cud_palette) -1 - i]
    label = labels[i]
    
    if label == r'$x^*_5$' or label == r'$x^*_4$':
        mask = y_data > 0.4
        y_data = np.array([ item if item > 0.4 else 0 for item in y_data ])
        
    elif label == r'$x^*_8$':
        
        mask = np.array([ True if x_data[i] < 1-1e-3 else False for i in range(len(x_data)) ])
        
    elif label in [ r'$x^*_6$', r'$x^*_7$' ]:
        mask = y_data < 1-1e-3
    
    else:
        mask = y_data > 1e-3

    # Apply the mask to the data
    y_data = y_data[mask]
    x_data = x_data[mask]
    
    big_ax.plot(x_data, y_data, color=color)


big_ax.set_xlim(-0.03, 1.1)

# Draw dashed lines at the bifurcations
bifurcation_point_arr = bifurcation_point_arr[:-1]
for bifurcation_point in bifurcation_point_arr:
    big_ax.axvline(bifurcation_point+0.5*1e-2, -0.2, 0.035, color='red', linestyle=':', clip_on=False)
    
big_ax.axvline(0, 1.08, 0.96, color='red', linestyle=':', clip_on=False)
big_ax.axvline(1, 1.08, 0.96, color='red', linestyle=':', clip_on=False)
        
# Define appropriate networks
cud_palette = [
    '#E69F00',  # Orange
    '#0101fd',  # Blue
    '#000000',  # Black
    '#ff0101',  # Red
]

vertices_removed_arr = [ [], [3], [3,4], [0,3,4], [0,3,4,7], [0,3,4,6,7] ]
H1 = G.copy()
colors_1 = [ cud_palette[0] if node not in vertices_removed_arr[0] else cud_palette[3] for node in G  ]

H2 = G.copy()
edges_removed = [ edge for edge in G.edges() if edge[0] in vertices_removed_arr[1] or edge[1] in vertices_removed_arr[1] ]
colors_2 = [ cud_palette[0] if node not in vertices_removed_arr[1] else cud_palette[3] for node in G  ]
H2.remove_edges_from(edges_removed)

H3 = G.copy()
edges_removed = [ edge for edge in G.edges() if edge[0] in vertices_removed_arr[2] or edge[1] in vertices_removed_arr[2] ]
colors_3 = [ cud_palette[0] if node not in vertices_removed_arr[2] else cud_palette[3] for node in G  ]
H3.remove_edges_from(edges_removed)

H4 = G.copy()
edges_removed = [ edge for edge in G.edges() if edge[0] in vertices_removed_arr[3] or edge[1] in vertices_removed_arr[3] ]
colors_4 = [ cud_palette[0] if node not in vertices_removed_arr[3] else cud_palette[3] for node in G  ]
colors_4[2] = cud_palette[1]
colors_4[5] = cud_palette[1]
H4.remove_edges_from(edges_removed)

H5 = G.copy()
edges_removed = [ edge for edge in G.edges() if edge[0] in vertices_removed_arr[5] or edge[1] in vertices_removed_arr[5] ]
colors_5 = [ cud_palette[0] if node not in vertices_removed_arr[5] else cud_palette[3] for node in G  ]
colors_5[2] = cud_palette[1]
colors_5[5] = cud_palette[1]
colors_5[1] = cud_palette[1]
H5.remove_edges_from(edges_removed)

# Draw the networks
node_size = 400
edge_width = 2
edge_color = 'black'

labels ={0: '3', 1: '8', 2: '6', 3: '1', 4: '2', 5: '7', 6: '4', 7: '5'}

nx.draw(H1, ax=ax1, pos=pos, with_labels=False, node_size=node_size, node_color=colors_1, edge_color=edge_color, width=edge_width, edgecolors='black')
nx.draw_networkx_labels(H1, ax=ax1, pos=pos, labels=labels, font_color='white')

nx.draw(H2, ax=ax2, pos=pos, with_labels=False, node_size=node_size, node_color=colors_2, edge_color=edge_color, width=edge_width, edgecolors='black')
nx.draw_networkx_labels(H2, ax=ax2, pos=pos, labels=labels, font_color='white')

nx.draw(H3, ax=ax3, pos=pos, with_labels=False, node_size=node_size, node_color=colors_3, edge_color=edge_color, width=edge_width, edgecolors='black')
nx.draw_networkx_labels(H3, ax=ax3, pos=pos, labels=labels, font_color='white')

nx.draw(H4, ax=ax4, pos=pos, with_labels=False, node_size=node_size, node_color=colors_4, edge_color=edge_color, width=edge_width, edgecolors='black')
nx.draw_networkx_labels(H4, ax=ax4, pos=pos, labels=labels, font_color='white')

nx.draw(H5, ax=ax5, pos=pos, with_labels=False, node_size=node_size, node_color=colors_5, edge_color=edge_color, width=edge_width, edgecolors='black')
nx.draw_networkx_labels(H5, ax=ax5, pos=pos, labels=labels, font_color='white')

# Add text
ax6.set_xlabel('')
ax6.set_ylabel('')
ax6.set_xticks([])
ax6.set_yticks([])
ax6.set_xticklabels([])
ax6.set_yticklabels([])
ax6.spines['top'].set_visible(False)
ax6.spines['right'].set_visible(False)
ax6.spines['bottom'].set_visible(False)
ax6.spines['left'].set_visible(False)

ax6.text(0.07, 0.35, '{6,7,8} → MIS', fontsize = 18)

captions = [ '(a)', '(b)', '(c)', '(d)', '(e)', '(f)' ]
for index, ax in enumerate([ax1, ax2, ax3, ax4, ax5]):
    ax.margins(0.1)
    ax.set_xlim([-1, 1.25])
    ax.set_ylim([-0.9, 1])
    
    ax.text(0, -1.1, captions[index], fontsize=14)

big_ax.text(0.0046, 1.08, '(a)', fontsize=14)
big_ax.text(0.244, -0.25, '(b)', fontsize=14)
big_ax.text(0.327, -0.25, '(c)', fontsize=14)
big_ax.text(0.463, -0.25, '(d)', fontsize=14)
big_ax.text(1.0046, 1.07, '(e)', fontsize=14)
big_ax.hlines(1, -1, 1.3, 'black', alpha=0.5)
big_ax.hlines(0, -1, 1.3, 'black', alpha=0.5)
big_ax.text(0.51, -0.15, r'$\tau$', fontsize=14)
big_ax.set_ylabel(r'$x^{\ast}$', fontsize=14)
big_ax.legend(loc='center left', bbox_to_anchor=(-0.006, 0.34), fontsize=10)
big_ax.set_ylim([-0.02, 1.02])
big_ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=14)
big_ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0], ['0.0', '0.2', '0.4', '0.6', '0.8', '1.0'], fontsize=14)

# Make grey dashed lines.
ax1.axvline(1.5, -1.6, 1, color='grey', clip_on=False, alpha=0.6)
ax2.axvline(1.5, -1.6, 1, color='grey', clip_on=False, alpha=0.6)
ax2.axhline(-1.4, -1.4, 2.4, color='grey', clip_on=False, alpha=0.6)


plt.savefig(os.path.join(sys.path[0], 'Figure1.pdf'), dpi=900, transparent=True, bbox_inches='tight')
plt.show()