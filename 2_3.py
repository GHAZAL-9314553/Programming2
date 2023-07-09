import os
import dask.dataframe as dd

data_dir = "C:/code/data/nycflights"
file_pattern = os.path.join(data_dir, "*.csv")

ddf = dd.read_csv(
    file_pattern,
    parse_dates={"Date": ["Year", "Month", "DayofMonth"]},
    dtype={"TailNum": str, "CRSElapsedTime": float, "Cancelled": bool},
)

non_canceled_flights = ddf[ddf['Cancelled'] == False]

# Convert 'Date' column to datetime format
non_canceled_flights['Date'] = dd.to_datetime(non_canceled_flights['Date'])

airport_counts = non_canceled_flights.groupby('Origin')['Cancelled'].count().compute()
print(airport_counts)

average_delay = non_canceled_flights.groupby('Origin')['DepDelay'].mean().compute()
print(average_delay)

worst_delay_day = non_canceled_flights.groupby(['Origin', non_canceled_flights['Date'].dt.weekday])['DepDelay'].mean().idxmax().compute()
print(worst_delay_day)

# Convert 'DepTime' column to datetime format
ddf['DepTime'] = dd.to_datetime(ddf['DepTime'], format='%H%M', errors='coerce')

busiest_hours = ddf['DepTime'].dt.hour.value_counts().nlargest(5).compute()
print(busiest_hours)
