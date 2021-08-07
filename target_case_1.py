import folium
from folium import plugins
from folium.plugins import HeatMap

import pandas as pd

df = pd.read_csv('~/Desktop/output.csv')

# Separate DF by Hour
print(f'Calculating Start Times')
hour_starts = [f' {i}:00'[-5:] for i in range(24)]
dfs_by_hour_start = [df[df['Start Time'].str.contains(hour)] for hour in hour_starts]

print(f"Sample of Entries from 12AM:")
print(dfs_by_hour_start[0]['Start Time'].head())

print(f"Sample of Entries from 4:00PM")
print(dfs_by_hour_start[16]['Start Time'].head())