import os
import sys
import numpy as np
import networkx as nx
import time
import pandas as pd
import MIS_algorithms as MIS

def update_row(row: dict) -> dict:
    """Calculate output values and update row."""
    
    if row['LV_output'] == None or row['continuation_output'] == None or row['greedy_output'] == None:
                
        # Define networkx graph
        G = nx.Graph()
        G.add_nodes_from(row['vertices'])
        G.add_edges_from(row['edges'])
            
        start_time = time.time()
        maximum_count = 0
        for i in range(10):
            LV_output_temp  = MIS.lotka_volterra(G, tau=1.1, x0=np.random.random(len(G)))
            if len(LV_output_temp) > maximum_count:
                LV_output = LV_output_temp
        LV_time = time.time() - start_time
        
        start_time = time.time()
        continuation_output  = MIS.continuation(G)
        continuation_time = time.time() - start_time
        
        start_time = time.time()
        greedy_output  = MIS.greedy(G)
        greedy_time = time.time() - start_time
        
        row['LV_output'] = LV_output
        row['LV_time'] = LV_time
        row['continuation_output'] = continuation_output
        row['continuation_time'] = continuation_time
        row['greedy_output'] = greedy_output
        row['greedy_time'] = greedy_time

    return row

def save_data(df: pd.DataFrame, type: str):
    """Save dataframe to csv and pickle format."""
    start_time = time.time()
    df.to_csv(os.path.join(sys.path[0], 'data_raw/' + "DIMAC" + '.csv'), header=True, index=False)
    df.to_pickle(os.path.join(sys.path[0], 'data_raw/' + "DIMAC" + '.pkl'))
    save_time = time.time() - start_time  
    print(f'Data saved in {np.round(save_time,3)} seconds.')
    
def analyse_graphs():
    df = pd.read_pickle(os.path.join(sys.path[0], 'data_empty/' + 'DIMAC' + '.pkl'))
    
    for index, row in df.iterrows():
        row_updated = update_row(row)
        df.iloc[index] = pd.Series(row_updated)
            
        save_data(df, type)
        print('Network analysed.')

if __name__ == '__main__':
    analyse_graphs()