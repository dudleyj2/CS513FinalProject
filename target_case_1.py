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


# Make Heat Maps
df_16 = df[df['Start Time'].str.contains('16:00')]
df_17 = df[df['Start Time'].str.contains('17:00')]
df_18 = df[df['Start Time'].str.contains('18:00')]
df_19 = df[df['Start Time'].str.contains('19:00')]


my_heatmap_16 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start_16 = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_16.iterrows()]
HeatMap(heat_data_start_16, blur=30, radiues=10).add_to(my_heatmap_16)
my_heatmap_16.save("1600.html")

my_heatmap_17 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start_17 = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_17.iterrows()]
HeatMap(heat_data_start_17, blur=30, radiues=10).add_to(my_heatmap_17)
my_heatmap_17.save("1700.html")

my_heatmap_18 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start_18 = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_18.iterrows()]
HeatMap(heat_data_start_18, blur=30, radiues=10).add_to(my_heatmap_18)
my_heatmap_18.save("1800.html")

my_heatmap_19 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start_19 = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_19.iterrows()]
HeatMap(heat_data_start_19, blur=30, radiues=10).add_to(my_heatmap_19)
my_heatmap_19.save("1900.html")


df_4 = df[df['Start Time'].str.contains(' 4:00')]
my_heatmap_4 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start_4 = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_4.iterrows()]
HeatMap(heat_data_start_4, blur=30, radiues=10).add_to(my_heatmap_4)
my_heatmap_4.save("400.html")