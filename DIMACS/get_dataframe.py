from scipy.io import mmread
import os
import sys
import numpy as np
import networkx as nx
import pandas as pd

def get_data():
        
    data = []
    for graph_name in sorted(os.listdir(os.path.join(sys.path[0], 'graphs'))):

        a = mmread(os.path.join(sys.path[0], f'graphs/{graph_name}/{graph_name}.mtx'))
        A = a.todense()
        G = nx.from_numpy_array(A)
        size = len(G)
        density =  np.round(len(G.edges()) / ( size * (size-1) / 2 ), 2)

        degrees = [ G.degree(node) for node in G ]
        degree_min = min(degrees)
        degree_max = max(degrees)

        new_row = {
                    'graph_name': graph_name,
                    'vertices': G.nodes(),
                    'edges': G.edges(),
                    'size': size,
                    'density': density,
                    'degree_min': degree_min,
                    'degree_max': degree_max,
                    'LV_output': None,
                    'LV_time': None,
                    'continuation_output': None, 
                    'continuation_time': None,
                    'greedy_output': None,
                    'greedy_time': None,
        }
        
        data.append(new_row)
            
    df = pd.DataFrame(data)

    df.to_csv(os.path.join(sys.path[0], "data_empty/DIMAC.pkl"), index=False)
    df.to_pickle(os.path.join(sys.path[0], "data_empty/DIMAC.pkl"))

if __name__ == '__main__':
    get_data()