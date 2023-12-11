import pandas as pd
import numpy as np

def generate_car_matrix(df) -> pd.DataFrame:
    result_df = df.pivot(index='id_1', columns='id_2', values='car')
    np.fill_diagonal(result_df.values, 0)
    return result_df

df = pd.read_csv('dataset-1.csv')

# Call the function to generate the car matrix
result_matrix = generate_car_matrix(df)

# Print result_matrix 
print(result_matrix)



def get_type_count(df) -> dict:
     # Categorize 'car' values into types
    df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each car_type category
    car_type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically
    car_type_counts = dict(sorted(car_type_counts.items()))

    return car_type_counts

df = pd.read_csv('dataset-1.csv')

# Call the function to get the car type counts
result_counts = get_type_count(df)

# Print the result_counts 
print(result_counts)



def get_bus_indexes(df) -> list:
   
    # Calculate the mean of the 'bus' column
    bus_mean = df['bus'].mean()

    # Filter indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    return bus_indexes

df = pd.read_csv('dataset-1.csv')

# Call the function to get the bus indexes
result_indexes = get_bus_indexes(df)

# Print the result_indexes 
print(result_indexes)




def filter_routes(df) -> list:
   
    # Group by 'route' and calculate the average 'truck' values
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average 'truck' value is greater than 7
    filtered_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list alphabetically
    filtered_routes.sort()

    return filtered_routes

df = pd.read_csv('dataset-1.csv')

# Call the function to filter routes
result_routes = filter_routes(df)

# Print the result_routes 
print(result_routes)




def multiply_matrix(matrix) -> pd.DataFrame:
  
    # Apply conditions to multiply matrix values
    modified_matrix = matrix.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix
    
result_matrix = generate_car_matrix(df)

# Call the function to multiply matrix values
modified_result_matrix = multiply_matrix(result_matrix)

# Print the modified_result_matrix 
print(modified_result_matrix)



import pandas as pd

def time_check(df) -> pd.Series:
    
    # Convert 'startDay' and 'endDay' columns to datetime format
    df['startDay'] = pd.to_datetime(df['startDay'], format='%Y-%m-%d')
    df['endDay'] = pd.to_datetime(df['endDay'], format='%Y-%m-%d')

    # Extract day of week and hour from the timestamps
    df['start_day_of_week'] = df['startDay'].dt.dayofweek
    df['start_hour'] = df['startTime'].dt.components['hours']
    df['end_day_of_week'] = df['endDay'].dt.dayofweek
    df['end_hour'] = df['endTime'].dt.components['hours']

    # Create a mask for incorrect timestamps
    mask = (
        (df['start_hour'] != 0) | (df['end_hour'] != 23) | 
        (df['start_day_of_week'] != 0) | (df['end_day_of_week'] != 6)
    )

    # Create a boolean series with multi-index (id, id_2)
    result_series = df[mask].set_index(['id', 'id_2'])['startDay']

    return result_series

df = pd.read_csv('dataset-2.csv')

# Call the function to check timestamps
result_series = time_check(df)

# Print the result_series 
print(result_series)



