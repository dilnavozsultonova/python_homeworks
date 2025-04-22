import pandas as pd


# Load the dataset
flight_file = pd.read_parquet('lesson-17/data/flights')

# Convert DepDelay to numeric (force errors to NaN, then drop or fill)
flight_file ['DepDelay'] = pd.to_numeric(flight_file ['DepDelay'], errors='coerce')
flight_file ['FlightDate'] = pd.to_numeric(flight_file ['FlightDate'], errors='coerce')

# Now filter the delays
flights_pipeline = flight_file [flight_file ['DepDelay'] > 30].copy()

# Avoid divide-by-zero: filter out or handle missing/zero duration
flights_pipeline = flights_pipeline[flights_pipeline['FlightDate'] > 0]

# Add Delay_Per_Hour
flights_pipeline['Delay_Per_Hour'] = flights_pipeline['DepDelay'] / (flights_pipeline['FlightDate'] / 60)

# View result
print(flights_pipeline[['Reporting_Airline', 'DepDelay', 'FlightDate', 'Delay_Per_Hour']].head())
# print(flight_file.columns)