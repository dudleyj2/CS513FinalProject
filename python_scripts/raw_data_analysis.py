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

print(f"\nTrip Duration Statistics (Seconds)")
print(df["Trip Duration"].describe())

print(f"\nTrip Distance Statistics (Feet)")
print(df["Trip Distance"].describe())
