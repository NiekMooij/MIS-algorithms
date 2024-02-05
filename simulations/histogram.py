import networkx as nx
import numpy as np
import os
import pandas as pd
import sys
import random
from communities.algorithms import bron_kerbosch
import MIS_algorithms as MIS

def get_histogram_data(type):
    if type == "erdos_renyi_histogram":
        G = MIS.erdos_renyi(60, 0.1, connected=True)
    if type == "random_bipartite_histogram":
        G = MIS.random_bipartite(30, 30, 0.1, connected=True)
    if type == "random_geometric_histogram":
        G = MIS.random_geometric(60, 0.2, connected=True)
        
    print('Network generated.')
    
    bron_kerbosch_output = bron_kerbosch(nx.to_numpy_array(nx.complement(G)), pivot=True)
    print('Bron-Kerbosch performed.')
    
    df = pd.DataFrame(columns=['uniform_MIS', 'LV_MIS'], index=range(1, len(bron_kerbosch_output) + 1))

    for index, item in enumerate(bron_kerbosch_output):
        uniform_output = list(bron_kerbosch_output[index])
        LV_output = MIS.lotka_volterra(G, tau=1.1, x0=[ random.random() for i in range(len(G)) ])
        
        df.iloc[index] = { 'uniform_MIS': uniform_output, 'LV_MIS': LV_output }
        
        percentage = np.round((index + 1) / len(bron_kerbosch_output) * 100, 2)
        print(f'{percentage} %')
            
    A = nx.to_numpy_array(G)
    np.save(os.path.join(sys.path[0], "data_empty/" + type + "_A.npy"), A)
    
    df.to_csv(os.path.join(sys.path[0], "data_raw/" + type + ".csv"), index=False)
    df.to_pickle(os.path.join(sys.path[0], "data_raw/" + type + ".pkl"))

    # Analyze results
    for key in ['uniform_MIS', 'LV_MIS']:
        df[key] = df[key].apply(lambda x: len(x))

    value_counts_uniform = df['uniform_MIS'].value_counts().to_dict()
    value_counts_LV = df['LV_MIS'].value_counts().to_dict()
    keys = set(value_counts_uniform.keys()).union(value_counts_LV.keys())
    df_data = pd.DataFrame(columns = [ 'value', 'count_uniform', 'count_LV' ])

    for key in keys:
        if value_counts_uniform.get(key) is not None and value_counts_LV.get(key) is not None:
            new_row = { 'value': key, 'count_uniform': value_counts_uniform[key], 'count_LV': value_counts_LV[key]  }
            df_data = pd.concat([df_data, pd.DataFrame(new_row, index=[0])], ignore_index=True)
            
        elif value_counts_uniform.get(key) is not None and value_counts_LV.get(key) is None:
            new_row = { 'value': key, 'count_uniform': value_counts_uniform[key], 'count_LV': 0  }
            df_data = pd.concat([df_data, pd.DataFrame(new_row, index=[0])], ignore_index=True)
            
        elif value_counts_uniform.get(key) is None and value_counts_LV.get(key) is not None:
            new_row = { 'value': key, 'count_uniform': 0, 'count_LV': value_counts_LV[key]  }
            df_data = pd.concat([df_data, pd.DataFrame(new_row, index=[0])], ignore_index=True)
                
    df_data.to_csv(os.path.join(sys.path[0], f"data_analysed/" + type + ".csv"), index=False)
    df_data.to_pickle(os.path.join(sys.path[0], f"data_analysed/" + type + ".pkl"))
    
if __name__ == '__main__':
    types = [
             "erdos_renyi_histogram",
             "random_bipartite_histogram",
             "random_geometric_histogram"
             ]

    get_histogram_data("random_geometric_histogram")