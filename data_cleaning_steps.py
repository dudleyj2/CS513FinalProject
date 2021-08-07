import numpy as np
import pandas as pd

df = pd.read_csv("~/Downloads/e-scooter-trips-2020-1.csv")
# Get Total Number of Columns
total_columns = len(df.columns)
print(f"Total Dataset Columns: {total_columns}")

# Get Raw Row Total
raw_row_total = df.size/total_columns

# Remove Rows from Table with NA Values
df.dropna(inplace=True)
na_row_total = df.size/total_columns

print(f"Initial Raw Data Row Count: {raw_row_total}")
print(f"Row Count After Removing NA's: {na_row_total}")
print(f"Total NA Rows Removed: {raw_row_total - na_row_total}")




# Find Trip Duration Mean
trip_duration_mean = df['Trip Duration'].mean()
print(f'Trip Duration Mean: {trip_duration_mean}')

# Find Trip Duration Standard Deviation
trip_duration_std = df['Trip Duration'].std()
print(f'Trip Duration Standard Deviation: {trip_duration_std}')

# Find +/- 2 SD from Mean
print('Standard Deviation Range = +/-2 St. Dev. from Mean')
print(f'Standard Deviation Range = [{trip_duration_mean - 2*trip_duration_std}, {trip_duration_mean + 2*trip_duration_std}]')







"""


# Find Trip Duration Mean
trip_duration_mean = df["Trip Duration"].mean()
print(f"Trip Duration Mean: {trip_duration_mean}")

# Find Trip Duration Standard Deviation
trip_duration_std = df["Trip Duration"].std()
print(f"Trip Duration Standard Deviation: {trip_duration_std}")

# Find +/- 2 SD from Mean
print("Standard Deviation Range = +/-2 St. Dev. from Mean")
print(f"Standard Deviation Range = [{trip_duration_mean - 2*trip_duration_std}, {trip_duration_mean + 2*trip_duration_std}]")

# Learn here that Mean and Standard Deviation might not be the best approach
# Do a Describe on the Data
print("Data Description")
print(df["Trip Duration"].describe())

# Median here is a much better fit
print(f"Median Trip Length (Seconds): {df['Trip Duration'].median()}")
print(f"Median Trip Length (Minutes): {df['Trip Duration'].median()/60}")

# Let's go with data between 5th and 95th percentiles
duration_5th_percentile = np.percentile(df["Trip Duration"], 5)
duration_95th_percentile = np.percentile(df["Trip Duration"], 95)
print(f"5th Percentile Duration (Seconds): {duration_5th_percentile}")
print(f"5th Percentile Duration (Minutes): {duration_5th_percentile/60}")

print(f"95th Percentile Duration (Seconds): {duration_95th_percentile}")
print(f"95th Percentile Duration (Minutes): {duration_95th_percentile/60}")


# This is a good fit
# Both are within out SD range, but excessively long trips are not influencing our dataset
df_duration_5th_percentile = df[df["Trip Duration"] < duration_5th_percentile].index
df.drop(df_duration_5th_percentile, inplace=True)
print(f"Rows after removing short trips: {df.size/16}")

df_duration_95th_percentile = df[df["Trip Duration"] > duration_95th_percentile].index
df.drop(df_duration_95th_percentile, inplace=True)
print(f"Rows after removing long trips: {df.size/16}")
# Remove Rows < 5th Percentile Duration

print("\n\n\n")
# Repeat, but for Trip Distance Now
# Find Trip Distance Mean
trip_distance_mean = df["Trip Distance"].mean()
print(f"Trip Distance Mean: {trip_distance_mean}")

# Find Trip Distance Standard Deviation
trip_distance_std = df["Trip Distance"].std()
print(f"Trip Distance Standard Deviation: {trip_distance_std}")

# Find +/- 2 SD from Mean
print("Standard Deviation Range = +/-2 St. Dev. from Mean")
print(f"Standard Deviation Range = [{trip_distance_mean - 2*trip_distance_std}, {trip_distance_mean + 2*trip_distance_std}]")

# Learn here that Mean and Standard Deviation might not be the best approach
# Do a Describe on the Data
print("Data Description")
print(df["Trip Distance"].describe())

# Median here is a much better fit
print(f"Median Trip Length (Seconds): {df['Trip Distance'].median()}")
print(f"Median Trip Length (Minutes): {df['Trip Distance'].median()/60}")

# Let's go with data between 5th and 95th percentiles
distance_5th_percentile = np.percentile(df["Trip Distance"], 5)
distance_95th_percentile = np.percentile(df["Trip Distance"], 95)
print(f"5th Percentile Distance (Feet): {distance_5th_percentile}")
print(f"5th Percentile Distance (Miles): {distance_5th_percentile/5280}")

print(f"95th Percentile Distance (Feet): {distance_95th_percentile}")
print(f"95th Percentile Distance (Miles): {distance_95th_percentile/5280}")

# Not a Great Value at 5th Percentile - let's do 10 & 90
distance_10th_percentile = np.percentile(df["Trip Distance"], 10)
distance_90th_percentile = np.percentile(df["Trip Distance"], 90)
print(f"10th Percentile Distance (Feet): {distance_10th_percentile}")
print(f"10th Percentile Distance (Miles): {distance_10th_percentile/5280}")

print("hmm...lets see 10/90")
print(f"90th Percentile Distance (Feet): {distance_90th_percentile}")
print(f"90th Percentile Distance (Miles): {distance_90th_percentile/5280}")
print(f"this one is more realistic, so lets go with that")
"""