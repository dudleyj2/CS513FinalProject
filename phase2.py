import folium
from folium import plugins
from folium.plugins import HeatMap

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('~/Downloads/e-scooter-trips-2020-1.csv')
total_columns = len(df.columns)
print(f'Total Dataset Columns: {total_columns}')
print(f"Initial Data Rows: {df.size/total_columns}")


# Remove Rows from Table with NA Values
df.dropna(inplace=True)
print(f"Rows after removing NA's: {df.size/total_columns}")


# Find Trip Duration Mean
trip_duration_mean = df['Trip Duration'].mean()
print(f'Trip Duration Mean: {trip_duration_mean}')

# Find Trip Duration Standard Deviation
trip_duration_std = df['Trip Duration'].std()
print(f'Trip Duration Standard Deviation: {trip_duration_std}')

# Find +/- 2 SD from Mean
print('Standard Deviation Range = +/-2 St. Dev. from Mean')
print(f'Standard Deviation Range = [{trip_duration_mean - 2*trip_duration_std}, {trip_duration_mean + 2*trip_duration_std}]')

# Learn here that Mean and Standard Deviation might not be the best approach
# Do a Describe on the Data
print('Data Description')
print(df['Trip Duration'].describe())

# Median here is a much better fit
print(f"Median Trip Length (Seconds): {df['Trip Duration'].median()}")
print(f"Median Trip Length (Minutes): {df['Trip Duration'].median()/60}")

# Let's go with data between 5th and 95th percentiles
duration_5th_percentile = np.percentile(df['Trip Duration'], 5)
duration_95th_percentile = np.percentile(df['Trip Duration'], 95)
print(f"5th Percentile Duration (Seconds): {duration_5th_percentile}")
print(f"5th Percentile Duration (Minutes): {duration_5th_percentile/60}")

print(f"95th Percentile Duration (Seconds): {duration_95th_percentile}")
print(f"95th Percentile Duration (Minutes): {duration_95th_percentile/60}")


# This is a good fit
# Both are within out SD range, but excessively long trips are not influencing our dataset
df_duration_5th_percentile = df[df['Trip Duration'] < duration_5th_percentile].index
df.drop(df_duration_5th_percentile, inplace=True)
print(f"Rows after removing short trips: {df.size/total_columns}")

df_duration_95th_percentile = df[df['Trip Duration'] > duration_95th_percentile].index
df.drop(df_duration_95th_percentile, inplace=True)
print(f"Rows after removing long trips: {df.size/total_columns}")
# Remove Rows < 5th Percentile Duration

print('\n\n\n')
# Repeat, but for Trip Distance Now
# Find Trip Distance Mean
trip_distance_mean = df['Trip Distance'].mean()
print(f'Trip Distance Mean: {trip_distance_mean}')

# Find Trip Distance Standard Deviation
trip_distance_std = df['Trip Distance'].std()
print(f'Trip Distance Standard Deviation: {trip_distance_std}')

# Find +/- 2 SD from Mean
print('Standard Deviation Range = +/-2 St. Dev. from Mean')
print(f'Standard Deviation Range = [{trip_distance_mean - 2*trip_distance_std}, {trip_distance_mean + 2*trip_distance_std}]')

# Learn here that Mean and Standard Deviation might not be the best approach
# Do a Describe on the Data
print('Data Description')
print(df['Trip Distance'].describe())

# Median here is a much better fit
print(f"Median Trip Length (Seconds): {df['Trip Distance'].median()}")
print(f"Median Trip Length (Minutes): {df['Trip Distance'].median()/60}")

# Let's go with data between 5th and 95th percentiles
distance_5th_percentile = np.percentile(df['Trip Distance'], 5)
distance_95th_percentile = np.percentile(df['Trip Distance'], 95)
print(f"5th Percentile Distance (Feet): {distance_5th_percentile}")
print(f"5th Percentile Distance (Miles): {distance_5th_percentile/5280}")

print(f"95th Percentile Distance (Feet): {distance_95th_percentile}")
print(f"95th Percentile Distance (Miles): {distance_95th_percentile/5280}")

# Not a Great Value at 5th Percentile - let's do 10 & 90
distance_10th_percentile = np.percentile(df['Trip Distance'], 10)
distance_90th_percentile = np.percentile(df['Trip Distance'], 90)
print(f"10th Percentile Distance (Feet): {distance_10th_percentile}")
print(f"10th Percentile Distance (Miles): {distance_10th_percentile/5280}")

print('hmm...lets see 10/90')
print(f"90th Percentile Distance (Feet): {distance_90th_percentile}")
print(f"90th Percentile Distance (Miles): {distance_90th_percentile/5280}")
print(f'this one is more realistic, so lets go with that')


# This is a good fit
# Both are within out SD range, but excessively long trips are not influencing our dataset

df_distance_10th_percentile = df[df['Trip Distance'] < distance_10th_percentile].index
df.drop(df_distance_10th_percentile, inplace=True)
print(f"Rows after removing short trips: {df.size/total_columns}")

df_distance_90th_percentile = df[df['Trip Distance'] > distance_90th_percentile].index
df.drop(df_distance_90th_percentile, inplace=True)
print(f"Rows after removing long trips: {df.size/total_columns}")
# Remove Rows < 5th Percentile Distance

"""
review sizes of data set
that leaves us with D'
done
Data Cleaning Done

Let's Produce Heat Maps by Hour to Determine Locations for Bike Routes
"""
df['Start Time'].apply(pd.to_datetime)
df['End Time'].apply(pd.to_datetime)

# Separate DF by Hour
print(f'Calculating Start Times')
hour_starts = [f' {i}:00'[-5:] for i in range(24)]

dfs_by_hour_start = [df[df['Start Time'].str.contains(hour)] for hour in hour_starts]

for hour in dfs_by_hour_start:
    print(hour['Start Time'].head())

# Get Total Rows/Hour
trips_per_hour_start = [hour.size/total_columns for hour in dfs_by_hour_start]

print(f'Calculating End Times')
dfs_by_hour_end = [df[df['End Time'].str.contains(hour)] for hour in hour_starts]

for hour in dfs_by_hour_end:
    print(hour['End Time'].head())

# Get Total Rows/Hour
trips_per_hour_end = [hour.size/total_columns for hour in dfs_by_hour_end]

# Put into Chart for Visual
print(f'Trips per Hour Start: ')
for start_time in trips_per_hour_start:
    print(f'{start_time}')

print(f'\nTrips per Hour End: ')
for end_time in trips_per_hour_end:
    print(f'{end_time}')

"""
dfs_by_hour = 
dfs = []

# Chart by most common start times
start_times = [df_s0, df_s1, df_s2, df_s3, df_s4, df_s5, df_s6, df_s7, df_s8, df_s9, df_s10, df_s11, df_s12, df_s13, df_s14, df_s15, df_s16, df_s17, df_s18, df_s19, df_s20, df_s21, df_s22, df_s23]
start_times_per_hour = [hour.size/16 for hour in start_times]


df_e0 = df[df['End Time'].str.contains(' 0:00')]
df_e1 = df[df['End Time'].str.contains(' 1:00')]
df_e2 = df[df['End Time'].str.contains(' 2:00')]
df_e3 = df[df['End Time'].str.contains(' 3:00')]
df_e4 = df[df['End Time'].str.contains(' 4:00')]
df_e5 = df[df['End Time'].str.contains(' 5:00')]
df_e6 = df[df['End Time'].str.contains(' 6:00')]
df_e7 = df[df['End Time'].str.contains(' 7:00')]
df_e8 = df[df['End Time'].str.contains(' 8:00')]
df_e9 = df[df['End Time'].str.contains(' 9:00')]
df_e10 = df[df['End Time'].str.contains('10:00')]
df_e11 = df[df['End Time'].str.contains('11:00')]
df_e12 = df[df['End Time'].str.contains('12:00')]
df_e13 = df[df['End Time'].str.contains('13:00')]
df_e14 = df[df['End Time'].str.contains('14:00')]
df_e15 = df[df['End Time'].str.contains('15:00')]
df_e16 = df[df['End Time'].str.contains('16:00')]
df_e17 = df[df['End Time'].str.contains('17:00')]
df_e18 = df[df['End Time'].str.contains('18:00')]
df_e19 = df[df['End Time'].str.contains('19:00')]
df_e20 = df[df['End Time'].str.contains('20:00')]
df_e21 = df[df['End Time'].str.contains('21:00')]
df_e22 = df[df['End Time'].str.contains('22:00')]
df_e23 = df[df['End Time'].str.contains('23:00')]

# Chart by most common End Times
#end_times = [df_e0, df_e1, df_e2, df_e3, df_e4, df_e5, df_e6, df_e7, df_e8, df_e9, df_e10, df_e11, df_e12, df_e13, df_e14, df_e15, df_e16, df_e17, df_e18, df_e19, df_e20, df_e21, df_e22, df_e23]
#end_times_per_hour = [hour.size/16 for hour in end_times]


heat_maps = [folium.Map([41.8781, -87.6298], zoom_start=11) for i in range(24)]


my_heatmap_5 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_s5.iterrows()]
HeatMap(heat_data_start, blur=30, radiues=10).add_to(my_heatmap_5)
print('0')
my_heatmap_5.save("500.html")

my_heatmap_12 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_s12.iterrows()]
HeatMap(heat_data_start, blur=30, radiues=10).add_to(my_heatmap_12)
my_heatmap_12.save("1200.html")

my_heatmap_18 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_s18.iterrows()]
HeatMap(heat_data_start, blur=30, radiues=10).add_to(my_heatmap_18)
my_heatmap_18.save("1800.html")

my_heatmap_22 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_s22.iterrows()]
HeatMap(heat_data_start, blur=30, radiues=10).add_to(my_heatmap_22)
my_heatmap_22.save("2200.html")


"""
"""
let's do a describe to learn more about the data
why is that?
* some people ride and forget to log out of the app
* some people only ride for a few seconds before stopping
* some people get hit by cars and forget to log out
"""

# Remove Values outside 2 Standard Deviations of the Mean