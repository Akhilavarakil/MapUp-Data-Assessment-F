import pandas as pd
import numpy as np


def calculate_distance_matrix(df) -> pd.DataFrame:
   
    # Create a pivot table to represent distances between Id's
    distance_matrix = df.pivot_table(values='distance', index='id_1', columns='id_2', fill_value=0)

    # Add bidirectional distances for the matrix  symmentry
   distance_matrix =  distance_matrix + distance_matrix.T

    # Set diagonal values to 0 
    np.fill_diagonal(distance_matrix.values, 0)

    return distance_matrix

df = pd.read_csv('dataset-3.csv')

# Call the function to calculate the distance matrix
result_matrix = calculate_distance_matrix(df)

# Print the result_matrix
print(result_matrix)





def unroll_distance_matrix(df) -> pd.DataFrame:
    
    # Reset the index to make 'id_1' a column
    df_reset = df.reset_index()

    # Melt the dataframe to unroll the distance matrix
    unroll_df = pd.melt(df_reset, id_vars=['id_1'], var_name='id_end', value_name='distance')

    # Rename the columns
    unroll_df.columns = ['id_start', 'id_end', 'distance']

    # Exclude rows where 'id_start' is equal to 'id_end'
    unroll_df = unroll_df[unroll_df['id_start'] != unroll_df['id_end']]

    return unroll_df

result_unroll_df = unroll_distance_matrix(result_matrix)

# Print the result_unroll_df 
print(result_unroll_df)





def calculate_toll_rate(df) -> pd.DataFrame:
    
   # Rate coefficients for each vehicle type
    rate_coefficients = {'moto': 0.8, 'car': 1.2, 'rv': 1.5, 'bus': 2.2, 'truck': 3.6}

    # Create columns for each vehicle type and calculate toll rates
    for vehicle_type, rate_coefficient in rate_coefficients.items():
        df[vehicle_type] = df['distance'] * rate_coefficient

    return df

# result_unroll_df' is the unroll DataFrame from Question 2
result_with_toll_rate = calculate_toll_rate(result_unroll_df)

# Print the result_with_toll_rate 
print(result_with_toll_rate)
