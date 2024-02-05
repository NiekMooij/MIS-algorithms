import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import sys
from matplotlib.lines import Line2D

def get_path_graph(size):
    G = nx.Graph()
    for i in range(size-1):
        G.add_edges_from([(i+1, i+2)])
        
    return G
    
def get_fixed_point(tau, A):
    M = -tau * A - np.identity(len(A))
    point = np.linalg.solve(M, -np.ones(len(G)))
    
    return point

def get_plot(G, tau, ax=None, fig=None):

    A = nx.to_numpy_array(G)
    point = get_fixed_point(tau, A)
        
    ax.stem([ node for node in G ], point, linefmt=':')
    
    ax.set_xticks([ node for node in G ], [ node for node in G ], fontsize=12)
    ax.set_yticks([ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], [ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], fontsize=12)

    ax.set_xlabel('node', fontsize=14)
    ax.set_ylabel(r'$x^{\ast}$', fontsize=14)
    
if __name__ == "__main__":
    
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
    
    fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12,4))
    fig.subplots_adjust(hspace=0.3, wspace=0.25)

    # Odd case
    size = 11
    G = get_path_graph(size)
    
    # First tau case
    tau = 1/2-0.05
    A = nx.to_numpy_array(G)
    point = get_fixed_point(tau, A)
        
    markerline, stemlines, baseline = ax1.stem(np.array([ int(node) for node in G ])-0.12, point, 
                                               linefmt='black', 
                                               basefmt='black'
                                            #    label=r'$\tau =$' + f'{tau}'
                                               )
    markerline.set_markerfacecolor(cud_palette[0])
    markerline.set_markersize(10)
    
    ax1.set_xticks([ node for node in G ], [ node for node in G ], fontsize=14)
    ax1.set_yticks([ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], [ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], fontsize=14)

    ax1.set_xlabel('node', fontsize=14)
    ax1.set_ylabel(r'$x^{\ast}$', fontsize=14)
    
    # ---------------------------------------------------------------------------------------------------------
    
    # Second tau case
    tau = 1/2
    A = nx.to_numpy_array(G)
    point = get_fixed_point(tau, A)
        
    markerline, stemlines, baseline = ax1.stem(np.array([ int(node) for node in G ])+0.12, 
                                               point, linefmt='black', 
                                               basefmt='black'
                                            #    label=r'$\tau =$' + f'{tau}'
                                               )
    markerline.set_markerfacecolor(cud_palette[1])
    markerline.set_markersize(10)
    
    ax1.set_xticks([ node for node in G ], [ node for node in G ], fontsize=14)
    ax1.set_yticks([ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], [ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], fontsize=14)

    ax1.set_xlabel('node', fontsize=14)
    ax1.set_ylabel(r'$x^{\ast}$', fontsize=14)
    
    # Add legend to the plot
    line1 = Line2D([], [], color=cud_palette[0], marker='o', linestyle='None', label=r'$\tau = 0.45$', markersize=10, markeredgecolor='black')    
    line2 = Line2D([], [], color=cud_palette[1], marker='o', linestyle='None', label=r'$\tau = 1/2$', markersize=10, markeredgecolor='black')    
    legend = ax1.legend(handles=[line1, line2], loc=(0.38,0.7))
    ax1.add_artist(legend)
    
    # Even case
    size = 10
    G = get_path_graph(size)
    A = nx.to_numpy_array(G)
    point = get_fixed_point(tau, A)
        
    markerline, stemlines, baseline = ax2.stem(np.array([ int(node) for node in G ])-0.1,
                                               point, 
                                               linefmt='black', 
                                               basefmt='black'
                                            #    label=r'$\tau =$' + f'{tau}'
                                               )
    markerline.set_markerfacecolor(cud_palette[0])
    markerline.set_markersize(10)
    
    ax2.set_xticks([ node for node in G ], [ node for node in G ], fontsize=14)
    ax2.set_yticks([ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], [ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], fontsize=14)

    ax2.set_xlabel('node', fontsize=14)
    ax2.set_ylabel(r'$x^{\ast}$', fontsize=14)
    
    # Second tau case
    tau = (2 * np.cos(np.pi / (size-1)))**(-1)

    A = nx.to_numpy_array(G)
    point = get_fixed_point(tau, A)
        
    markerline, stemlines, baseline = ax2.stem(np.array([ int(node) for node in G ])+0.1, 
                                               point, 
                                               linefmt='black', 
                                               basefmt='black'
                                            #    label=r'$\tau =$' + r'$\left( 2 \cos\left(\frac{\pi}{n-1}\right) \right)^{-1}$'
                                               )
    markerline.set_markerfacecolor(cud_palette[1])
    markerline.set_markersize(10)
    
    ax2.set_xticks([ node for node in G ], [ node for node in G ], fontsize=14)
    ax2.set_yticks([ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], [ 0.0, 0.2, 0.4, 0.6, 0.8, 1.0 ], fontsize=14)

    ax2.set_xlabel('node', fontsize=14)
    ax2.set_ylabel(r'$x^{\ast}$', fontsize=14)

    # Add legend to the plot
    line1 = Line2D([], [], color=cud_palette[0], marker='o', linestyle='None', label=r'$\tau = 1/2$', markersize=10, markeredgecolor='black')    
    line2 = Line2D([], [], color=cud_palette[1], marker='o', linestyle='None', label=r'$\tau =$' + r'$\left( 2 \cos\left(\frac{\pi}{n-1}\right) \right)^{-1}$', markersize=10, markeredgecolor='black')    
    legend = ax2.legend(handles=[line1, line2], loc=(0.296,0.8))
    ax2.add_artist(legend)

    ax1.text(0.5, 1.02, 'Odd (n=11)', ha='center', transform=ax1.transAxes, fontsize=14)    
    ax2.text(0.5, 1.02, 'Even (n=10)', ha='center', transform=ax2.transAxes, fontsize=14)    
    
    save_name = os.path.join(sys.path[0], 'Figure2.pdf')
    plt.savefig(save_name, dpi=900, transparent=True, bbox_inches='tight')
    
    plt.show()



