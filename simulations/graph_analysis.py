import networkx as nx
import numpy as np
import os
import pandas as pd
import sys
import time
import MIS_algorithms as MIS
import datetime

def update_row(row: dict) -> dict:
    """Calculate output values and update row."""
    
    if row['exact_output'] is None or row['LV_output'] is None or row['continuation_output'] is None or row['greedy_output'] is None:
                
        # Define networkx graph
        G = nx.Graph()
        G.add_nodes_from(row['vertices'])
        G.add_edges_from(row['edges'])

        # Determine algorithm output
        if row['type'] == 'random_bipartite':
            start_time = time.time()
            exact_output = MIS.exact_bipartite(G)
            exact_time = time.time() - start_time  
        elif len(row['edges']) / (len(row['vertices'])**2) < 0.2:
            start_time = time.time()
            exact_output = MIS.exact_sparse(G)
            exact_time = time.time() - start_time  
        else:
            start_time = time.time()
            exact_output = MIS.exact(G)
            exact_time = time.time() - start_time
            
        start_time = time.time()
        LV_output  = MIS.lotka_volterra(G, tau=1.1, x0=np.random.random(len(G)))
        LV_time = time.time() - start_time
        
        start_time = time.time()
        continuation_output  = MIS.continuation(G)
        continuation_time = time.time() - start_time
        
        start_time = time.time()
        greedy_output  = MIS.greedy(G)
        greedy_time = time.time() - start_time
        
        row['exact_output'] = exact_output
        row['exact_time'] = exact_time
        row['LV_output'] = LV_output
        row['LV_time'] = LV_time
        row['continuation_output'] = continuation_output
        row['continuation_time'] = continuation_time
        row['greedy_output'] = greedy_output
        row['greedy_time'] = greedy_time

        return row, True
    
    return row, False

def save_data(df: pd.DataFrame, type: str):
    """Save dataframe to csv and pickle format."""
    start_time = time.time()
    df.to_csv(os.path.join(sys.path[0], 'data_raw/' + type + '.csv'), header=True, index=False)
    df.to_pickle(os.path.join(sys.path[0], 'data_raw/' + type + '.pkl'))
    save_time = time.time() - start_time  
    print(f'Data saved in {np.round(save_time,3)} seconds.')
    
def analyse_graphs(type, save_after_n_runs=100):
    
    if os.path.exists(os.path.join(sys.path[0], 'data_raw/' + type + '.pkl')):
        df = pd.read_pickle(os.path.join(sys.path[0], 'data_raw/' + type + '.pkl'))
    elif os.path.exists(os.path.join(sys.path[0], 'data_empty/' + type + '.pkl')):
        df = pd.read_pickle(os.path.join(sys.path[0], 'data_empty/' + type + '.pkl'))
    else:
        print('No test graphs generated.')

    count = 0
    
    for index, row in df.iterrows():
        row_updated, update_flag = update_row(row)
        df.iloc[index] = pd.Series(row_updated)
        
        if update_flag:
            count += 1

        if (count+1) % save_after_n_runs == 0 or index == len(df)-1:
            save_data(df, type)
            
        print(f'Network analysed - {datetime.datetime.now()}')

if __name__ == '__main__':
    types = [
            #  "erdos_renyi_probability",
            #  "erdos_renyi_size_sparse",
            #  "erdos_renyi_size_dense"
            #  "random_bipartite_probability",
            #  "random_bipartite_size_sparse",
            #  "random_bipartite_size_dense",
            #  "random_geometric_probability",
             "random_geometric_size_sparse",
             "random_geometric_size_dense"
             ]
    
    for type in types:
        analyse_graphs(type=type, save_after_n_runs=500)