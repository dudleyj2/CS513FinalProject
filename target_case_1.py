import folium
from folium import plugins
from folium.plugins import HeatMap

import pandas as pd

df = pd.read_csv("~/Desktop/output.csv")
total_columns = len(df.columns)

# Separate DF by Start Time Hour
print(f"Calculating Start Times")
hour_starts = [f" {i}:00"[-5:] for i in range(24)]
dfs_by_hour_start = [df[df["Start Time"].str.contains(hour)] for hour in hour_starts]

print(f"Sample of Entries with Start Time at 12AM:")
print(dfs_by_hour_start[0]["Start Time"].head())

print(f"Sample of Entries with STart Time at 4:00PM")
print(dfs_by_hour_start[16]["Start Time"].head())


# Separate DF by End Time Hour
print(f"\n\nCalculating End Times")
hour_ends = [f" {i}:00"[-5:] for i in range(24)]
dfs_by_hour_end = [df[df["End Time"].str.contains(hour)] for hour in hour_ends]

print(f"Sample of Entries with End Time at 12AM:")
print(dfs_by_hour_end[0]["End Time"].head())

print(f"Sample of Entries with End Time at 4:00PM")
print(dfs_by_hour_end[16]["End Time"].head())




# Get Total Rows/Hour
trips_per_hour_start = [hour.size/total_columns for hour in dfs_by_hour_start]

print(f'Calculating End Times')
dfs_by_hour_end = [df[df['End Time'].str.contains(hour)] for hour in hour_starts]

for hour in dfs_by_hour_end:
    print(hour['End Time'].head())

# Get Total Rows/Hour
trips_per_hour_end = [hour.size/total_columns for hour in dfs_by_hour_end]

print(f'Trips per Hour Start: ')
for i in range(len(trips_per_hour_start)):
    print(f'Hour {i}: {trips_per_hour_start[i]}')

print(f'\n\nTrips per Hour End: ')
for i in range(len(trips_per_hour_end)):
    print(f'Hour {i}: {trips_per_hour_end[i]}')