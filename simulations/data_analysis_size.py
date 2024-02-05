import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import pandas as pd
from scipy import stats

def confidence_interval(data, confidence=0.95):
    """
    Calculate the confidence interval for the mean of the data.

    Parameters:
        data (list or array-like): The input data.
        confidence (float, optional): The desired confidence level (default is 0.95).

    Returns:
        tuple: A tuple (lower_bound, upper_bound) representing the confidence interval.
    """
    data = np.array(data)
    n = len(data)
    mean = np.mean(data)
    std_error = stats.sem(data)  # Standard error of the mean
    margin_of_error = std_error * stats.t.ppf((1 + confidence) / 2, n - 1)
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return [lower_bound, upper_bound]

    
if __name__ == '__main__':
    types = [
             "erdos_renyi_size_sparse",
             "erdos_renyi_size_dense"
             "random_bipartite_size_sparse",
             "random_bipartite_size_dense",
             "random_geometric_size_sparse",
             "random_geometric_size_dense"
             ]

    type = 'random_geometric_size_dense'
    
    file_loc = os.path.join(sys.path[0], "data_raw/" + type + ".pkl")
    df = pd.read_pickle(file_loc)

    if type in ["random_geometric_size_sparse", "random_geometric_size_dense"]:
        df.rename(columns={'r_radius': 'p_connection'}, inplace=True)
    
    if type in ["random_bipartite_size_sparse", "random_bipartite_size_dense"]:
        size_arr = list((set(df['size1'])))
    else:
        size_arr = sorted(list(set(df['size'])))
        
    # Determine length of the outputs
    for key in ['exact_output', 'LV_output', 'continuation_output', 'greedy_output']:
        df[key] = df[key].apply(lambda x: len(x))
        
    # Determine the average performance per size
    df_means = pd.DataFrame(columns=['size', 'p_connection', 'LV_app', 'LV_app_CI_lower', 'LV_app_CI_upper', 'continuation_app', 'continuation_app_CI_lower', 'continuation_app_CI_upper', 'greedy_app', 'greedy_app_CI_lower', 'greedy_app_CI_upper'])
    df_eff = pd.DataFrame(columns=['size', 'p_connection', 'LV_eff', 'continuation_eff', 'greedy_eff'])
    
    for size in size_arr:
        if type in ["random_bipartite_size_sparse", "random_bipartite_size_dense"]:
            df_size = df[df['size1'] == size]
            size = size * 2
        else:
            df_size = df[df['size'] == size]
            
        df_size.drop(['vertices', 'edges'], axis=1, inplace=True)

        # Calculate the performance
        LV_app = np.array(df_size['LV_output'] / df_size['exact_output'])
        continuation_app = np.array(df_size['continuation_output'] / df_size['exact_output'])
        greedy_app = np.array(df_size['greedy_output'] / df_size['exact_output'])
        
        confidence_level = 0.99
        p_connection = list(df_size['p_connection'])[0]
        averages = {
            'size': size,
            'p_connection': p_connection,
            
            'LV_app': np.mean(LV_app), 
            'LV_app_CI_lower': confidence_interval(LV_app, confidence_level)[0], 
            'LV_app_CI_upper': confidence_interval(LV_app, confidence_level)[1], 

            'continuation_app': np.mean(continuation_app), 
            'continuation_app_CI_lower': confidence_interval(continuation_app, confidence_level)[0],
            'continuation_app_CI_upper': confidence_interval(continuation_app, confidence_level)[1],

            'greedy_app': np.mean(greedy_app),
            'greedy_app_CI_lower': confidence_interval(greedy_app, confidence_level)[0],
            'greedy_app_CI_upper': confidence_interval(greedy_app, confidence_level)[1]
        }

        df_new = pd.DataFrame(averages, index=[0])
        df_means = pd.concat([df_means, df_new], ignore_index=True)
        
        # Calculate the efficiencies
        LV_eff = (df_size['LV_output'] == df_size['exact_output']).sum() / len(df_size)
        continuation_eff = (df_size['continuation_output'] == df_size['exact_output']).sum() / len(df_size)
        greedy_eff = (df_size['greedy_output'] == df_size['exact_output']).sum() / len(df_size)

        efficiencies = {
            'size': size,
            'p_connection': p_connection, 
            'LV_eff': np.mean(np.array(LV_eff)), 
            'continuation_eff': np.mean(np.array(continuation_eff)), 
            'greedy_eff': np.mean(np.array(greedy_eff)),
        }

        df_new = pd.DataFrame(efficiencies, index=[0])
        df_eff = pd.concat([df_eff, df_new], ignore_index=True)
        
    if type in ["random_geometric_size_sparse", "random_geometric_size_dense"]:
        df_means.rename(columns={'p_connection': 'r_radius'}, inplace=True)
        df_eff.rename(columns={'p_connection': 'r_radius'}, inplace=True)
        
    # Save all data
    df_means.to_csv(os.path.join(sys.path[0], "data_analysed/" + type + '_performance' + ".csv"), index=False)
    df_means.to_pickle(os.path.join(sys.path[0], "data_analysed/" + type + '_performance' + ".pkl"))
    
    df_eff.to_csv(os.path.join(sys.path[0], "data_analysed/" + type + '_efficiency' + ".csv"), index=False)
    df_eff.to_pickle(os.path.join(sys.path[0], "data_analysed/" + type + '_efficiency' + ".pkl"))
    