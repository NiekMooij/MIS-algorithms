import os
import sys
import pandas as pd

def get_csv():
    df = pd.read_pickle(os.path.join(sys.path[0], 'data_raw/' + "DIMAC" + '.pkl'))
    df.drop( columns=['vertices', 'edges', 'LV_time', 'continuation_time', 'greedy_time'], inplace=True)
        
    for key in ['LV_output', 'continuation_output', 'greedy_output']:
        df[key] = df[key].apply(lambda x: len(x))
        
    df.rename(columns={'graph_name': 'name'}, inplace=True)
    df.rename(columns={'density': r'$\rho$'}, inplace=True)
    df.rename(columns={'degree_min': r'$d_{\text{min}}$'}, inplace=True)
    df.rename(columns={'degree_max': r'$d_{\text{max}}$'}, inplace=True)
    df.rename(columns={'LV_output': 'LV'}, inplace=True)
    df.rename(columns={'continuation_output': 'CLV'}, inplace=True)
    df.rename(columns={'greedy_output': 'Greedy'}, inplace=True)

    df.to_csv(os.path.join(sys.path[0], f"data_analyzed/" + "DIMAC" + ".csv"), index=False)
    df.to_pickle(os.path.join(sys.path[0], f"data_analyzed/" + "DIMAC" + ".csv"))

if __name__ == '__main__':
    get_csv()