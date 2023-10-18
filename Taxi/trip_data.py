# %%
min_datetime = df['pickup_datetime'].min()
max_datetime = df['pickup_datetime'].max()
total_rows = len(df)
print("Datetime Range: From", min_datetime, "to", max_datetime)
print("Total Rows:", total_rows)



# %%
field_names = df.columns
field_descriptions = {
    "medallion": "A unique identifier for the taxi",
    "hack_license": "A unique identifier for the taxi driver",
    "pickup_datetime": "Date and time of pickup",
    "dropoff_datetime": "Date and time of dropoff",
    
}
print("Field Names:")
print(field_names)
print("\nField Descriptions:")
for field, description in field_descriptions.items():
    print(field, ":", description)


# %%
sample_data = df.head()
print("Sample Data:")
print(sample_data)


# %%
data_types = df.dtypes
max_length = df.astype(str).apply(lambda x: x.str.len()).max()
print("MySQL Data Types:")
print(data_types)
print("\nMaximum String Lengths:")
print(max_length)


# %%
min_longitude = df['pickup_longitude'].min()
max_longitude = df['pickup_longitude'].max()
min_latitude = df['pickup_latitude'].min()
max_latitude = df['pickup_latitude'].max()
print("Geographic Range:")
print("Min Longitude:", min_longitude)
print("Max Longitude:", max_longitude)
print("Min Latitude:", min_latitude)
print("Max Latitude:", max_latitude)


# %%
import math

def haversine_distance(lat1, lon1, lat2, lon2):
  
    radius = 3959.0
    
    
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
   
    distance = radius * c
    return distance

average_trip_distance = df.apply(lambda row: haversine_distance(row['pickup_latitude'], row['pickup_longitude'], row['dropoff_latitude'], row['dropoff_longitude']), axis=1).mean()
print("Average Trip Distance (Haversine):", average_trip_distance, "miles")


# %%
plt.hist(df['trip_distance'], bins=20)
plt.xlabel("Trip Distance")
plt.ylabel("Frequency")
plt.title("Histogram of Trip Distances")
plt.show()


# %%
distinct_values = df.nunique()
print("Distinct Values for Each Field:")
print(distinct_values)



# %%
numeric_columns = df.select_dtypes(include=[np.number]).columns
min_max_values = df[numeric_columns].agg(['min', 'max'])
print("Minimum and Maximum Values for Numeric Fields (excluding lat and lon):")
print(min_max_values)


# %%
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour'] = df['pickup_datetime'].dt.hour
average_passengers_per_hour = df.groupby('hour')['passenger_count'].mean()
plt.plot(average_passengers_per_hour)
plt.xlabel("Hour of the Day")
plt.ylabel("Average Number of Passengers")
plt.title("Average Number of Passengers per Hour")
plt.show()


# %%
import pandas as pd


df = pd.read_csv("C:/Users/Tejashwini/Desktop/Taxi/trip_data_1.csv (1)/trip_data_1.csv")


# %%
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'])
df['hour'] = df['pickup_datetime'].dt.hour
average_passengers_per_hour = df.groupby('hour')['passenger_count'].mean()


# %%
import matplotlib.pyplot as plt


reduced_df = pd.read_csv("reduced_trip_data.csv")


reduced_df['pickup_datetime'] = pd.to_datetime(reduced_df['pickup_datetime'])
reduced_df['hour'] = reduced_df['pickup_datetime'].dt.hour
average_passengers_per_hour_reduced = reduced_df.groupby('hour')['passenger_count'].mean()


plt.figure(figsize=(10, 6))


plt.plot(average_passengers_per_hour, label="Original Data", marker='o', linestyle='-')


plt.plot(average_passengers_per_hour_reduced, label="Reduced Data", marker='o', linestyle='-')

plt.xlabel("Hour of the Day")
plt.ylabel("Average Number of Passengers")
plt.title("Average Number of Passengers per Hour (Original vs. Reduced Data)")
plt.xticks(range(24))
plt.grid(True)
plt.legend()
plt.show()



