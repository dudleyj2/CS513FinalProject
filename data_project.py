import folium
from folium import plugins
from folium.plugins import HeatMap

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('~/Downloads/e-scooter-trips-2020-1.csv')

# Remove Trips with Duration (<60 Seconds)
short_duration_trips = df[df['Trip Duration'] < 60].index
df.drop(short_duration_trips, inplace=True)

# Remove Trips with Unreasonably Long Durations (>3600 Seconds)
long_duration_trips = df[df['Trip Duration'] > 60*60].index
df.drop(long_duration_trips, inplace=True)

# Remove Trips with Short Distances (< 300 feet)
short_distance_trips = df[df['Trip Distance'] < 300].index
df.drop(short_distance_trips, inplace=True)
print(df.size/16)

df.dropna(inplace=True)
print(df.size/16)

print(df.head())

# Convert times to 24 Hour
df['Start Time'].apply(pd.to_datetime)

# Separate DF by Hour
hours = [str(i)+':00' for i in range(24)]
dfs = []
df_s0 = df[df['Start Time'].str.contains(' 0:00')]
df_s1 = df[df['Start Time'].str.contains(' 1:00')]
df_s2 = df[df['Start Time'].str.contains(' 2:00')]
df_s3 = df[df['Start Time'].str.contains(' 3:00')]
df_s4 = df[df['Start Time'].str.contains(' 4:00')]
df_s5 = df[df['Start Time'].str.contains(' 5:00')]
df_s6 = df[df['Start Time'].str.contains(' 6:00')]
df_s7 = df[df['Start Time'].str.contains(' 7:00')]
df_s8 = df[df['Start Time'].str.contains(' 8:00')]
df_s9 = df[df['Start Time'].str.contains(' 9:00')]
df_s10 = df[df['Start Time'].str.contains('10:00')]
df_s11 = df[df['Start Time'].str.contains('11:00')]
df_s12 = df[df['Start Time'].str.contains('12:00')]
df_s13 = df[df['Start Time'].str.contains('13:00')]
df_s14 = df[df['Start Time'].str.contains('14:00')]
df_s15 = df[df['Start Time'].str.contains('15:00')]
df_s16 = df[df['Start Time'].str.contains('16:00')]
df_s17 = df[df['Start Time'].str.contains('17:00')]
df_s18 = df[df['Start Time'].str.contains('18:00')]
df_s19 = df[df['Start Time'].str.contains('19:00')]
df_s20 = df[df['Start Time'].str.contains('20:00')]
df_s21 = df[df['Start Time'].str.contains('21:00')]
df_s22 = df[df['Start Time'].str.contains('22:00')]
df_s23 = df[df['Start Time'].str.contains('23:00')]

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
end_times = [df_e0, df_e1, df_e2, df_e3, df_e4, df_e5, df_e6, df_e7, df_e8, df_e9, df_e10, df_e11, df_e12, df_e13, df_e14, df_e15, df_e16, df_e17, df_e18, df_e19, df_e20, df_e21, df_e22, df_e23]
end_times_per_hour = [hour.size/16 for hour in end_times]


my_heatmap_5 = folium.Map([41.8781, -87.6298], zoom_start=11)
heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df_s5.iterrows()]
HeatMap(heat_data_start, blur=30, radiues=10).add_to(my_heatmap_5)
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

hours = [i for i in range(24)]
heat_maps = []
for hour in hours:
    base_map = folium.Map([41.8781, -87.6298], zoom_start=11)
    heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in start_times[hour].iterrows()]
    HeatMap(heat_data_start, blur=30, radiues=10).add_to(base_map)
    base_map.save(f'{hour}.jpg')




my_heatmap = folium.Map([41.8781, -87.6298], zoom_start=11)

heat_data_start = [[row['Start Centroid Latitude'],row['Start Centroid Longitude']] for index, row in df.iterrows()]
heat_data_end = [[row['End Centroid Latitude'],row['End Centroid Longitude']] for index, row in df.iterrows()]

HeatMap(heat_data_start, blur=30, radiues=10).add_to(my_heatmap)
#HeatMap(heat_data_end).add_to(my_heatmap)
my_heatmap.save("index3.html")


'''
Outline
* 
'''
