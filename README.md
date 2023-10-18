
1. What datetime range does your data cover? How many rows are there total?

Datetime Range: From 2013-01-01 00:00:00 to 2013-01-31 23:59:59
Total Rows: 14776615

2. What are the field names? Give descriptions for each field.

Field Names:
Index(['medallion', 'hack_license', 'vendor_id', 'rate_code',
       'store_and_fwd_flag', 'pickup_datetime', 'dropoff_datetime',
       'passenger_count', 'trip_time_in_secs', 'trip_distance',
       'pickup_longitude', 'pickup_latitude', 'dropoff_longitude',
       'dropoff_latitude', 'hour'],
      dtype='object')

Field Descriptions:
medallion : A unique identifier for the taxi
hack_license : A unique identifier for the taxi driver
pickup_datetime : Date and time of pickup
dropoff_datetime : Date and time of dropoff

3. Give some sample data for each field.

Sample Data:
                          medallion                      hack_license  \
0  89D227B655E5C82AECF13C3F540D4CF4  BA96DE419E711691B9445D6A6307C170   
1  0BD7C8F5BA12B88E0B67BED28BEA73D8  9FD8F69F0804BDB5549F40E9DA1BE472   
2  0BD7C8F5BA12B88E0B67BED28BEA73D8  9FD8F69F0804BDB5549F40E9DA1BE472   
3  DFD2202EE08F7A8DC9A57B02ACB81FE2  51EE87E3205C985EF8431D850C786310   
4  DFD2202EE08F7A8DC9A57B02ACB81FE2  51EE87E3205C985EF8431D850C786310   

  vendor_id  rate_code store_and_fwd_flag     pickup_datetime  \
0       CMT          1                  N 2013-01-01 15:11:48   
1       CMT          1                  N 2013-01-06 00:18:35   
2       CMT          1                  N 2013-01-05 18:49:41   
3       CMT          1                  N 2013-01-07 23:54:15   
4       CMT          1                  N 2013-01-07 23:25:03   

      dropoff_datetime  passenger_count  trip_time_in_secs  trip_distance  \
0  2013-01-01 15:18:10                4                382            1.0   
1  2013-01-06 00:22:54                1                259            1.5   
2  2013-01-05 18:54:23                1                282            1.1   
3  2013-01-07 23:58:20                2                244            0.7   
4  2013-01-07 23:34:24                1                560            2.1   

   pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  \
0        -73.978165        40.757977         -73.989838         40.751171   
1        -74.006683        40.731781         -73.994499         40.750660   
...
1     0  
2    18  
3    23  
4    23  

4. What MySQL data types / len would you need to store each of the fields?

MySQL Data Types:
medallion                     object
hack_license                  object
vendor_id                     object
rate_code                      int64
store_and_fwd_flag            object
pickup_datetime       datetime64[ns]
dropoff_datetime              object
passenger_count                int64
trip_time_in_secs              int64
trip_distance                float64
pickup_longitude             float64
pickup_latitude              float64
dropoff_longitude            float64
dropoff_latitude             float64
hour                           int32
dtype: object

Maximum String Lengths:
medallion             32
hack_license          32
vendor_id              3
rate_code              3
store_and_fwd_flag     3
pickup_datetime       19
...
dropoff_longitude     14
dropoff_latitude      14
hour                   2
dtype: int64


5. What is the geographic range of your data (min/max - X/Y)?

Geographic Range:
Min Longitude: -2771.2854
Max Longitude: 112.40418
Min Latitude: -3547.9207
Max Latitude: 3310.3645

6. What is the average overall computed trip distance?

Average Trip Distance (Haversine): 12.178383325209287 miles

7. What are the distinct values for each field?

Distinct Values for Each Field:
medallion               13426
hack_license            32224
vendor_id                   2
rate_code                  14
store_and_fwd_flag          2
pickup_datetime       2303465
dropoff_datetime      2305816
passenger_count            10
trip_time_in_secs        6594
trip_distance            4368
pickup_longitude        40442
pickup_latitude         64511
dropoff_longitude       56249
dropoff_latitude        88766
hour                       24
dtype: int64

![image](https://github.com/tejashwini2000/trip_data/assets/94233281/c06f9e86-e2bc-403b-85b2-896ba7f2ef3c)

 
8. For other numeric types besides lat and lon, what are the min and max values?

Minimum and Maximum Values for Numeric Fields (excluding lat and lon):
     rate_code  passenger_count  trip_time_in_secs  trip_distance  \
min          0                0                  0            0.0   
max        210              255              10800          100.0   

     pickup_longitude  pickup_latitude  dropoff_longitude  dropoff_latitude  \
min       -2771.28540       -3547.9207         -2350.9556        -3547.9207   
max         112.40418        3310.3645          2228.7375         3477.1055   

     hour  
min     0  
max    23  

9. Create a chart that shows the average number of passengers each hour of the day.
![image](https://github.com/tejashwini2000/trip_data/assets/94233281/0f35d610-6fed-4065-9af7-2c86980a2b1d)

 
10. Repeat step 9 with the reduced dataset and compare the two charts.
![image](https://github.com/tejashwini2000/trip_data/assets/94233281/449bc9f6-1511-40b6-8e50-babbc43cfb4d)


 

