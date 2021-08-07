import pandas as pd

df = pd.read_csv("~/Desktop/output.csv")
total_columns = len(df.columns)

print(f"\nMedian Trip Length (Seconds): {df['Trip Duration'].median()}")
print(f"Median Trip Length (Minutes): {df['Trip Duration'].median()/60}")


scooter_price = 449
median_minutes = df['Trip Duration'].median()/60

remaining_investment = scooter_price

total_trips_until_profit = 0
times_used_daily = 0
while remaining_investment > 0:
    total_trips_until_profit += 1
    if times_used_daily % 10 == 0:
        remaining_investment += 5
    remaining_investment -=  (1 + 0.39*median_minutes)
    times_used_daily += 1

print(f"Total Trips Until Profit: {total_trips_until_profit}")


