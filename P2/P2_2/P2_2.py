import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load data
df = pd.read_csv(r'C:\Users\suege\Desktop\SCDM\Assignments\P2\2\SAA2_WC_2017_metocean_10min_avg.csv', parse_dates=['TIME_SERVER'])

#check for missing values
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)

#data selection
from datetime import datetime
start_date = datetime(2017, 6, 28)
end_date = end_date = datetime(2017, 7, 4)
data1 = df.loc[(df['TIME_SERVER'] >= start_date) & (df['TIME_SERVER'] <= end_date)]

#temperature time series
plt.figure(figsize=(12, 8))
plt.plot(data1['TIME_SERVER'], data1['TSG_TEMP'])
plt.xlabel('Date')
plt.ylabel('Temperature (deg C)')
plt.title('Time Series of Temperature')
plt.style.use('grayscale')
plt.savefig('temperature_time_series.png')

#salinity histogram
plt.figure(figsize=(10, 8) )  
sns.histplot(data1['TSG_SALINITY'], bins=range(30, 36), kde=False)
plt.xlabel('Salinity (psu)')
plt.ylabel('Frequency')
plt.title('Histogram of Salinity')
plt.savefig('salinity_histogram.png')

#scatter plot of wind speed and air temperature
plt.figure(figsize=(12, 10))
sns.scatterplot(x=data1['WIND_SPEED_TRUE'], y=data1['AIR_TEMPERATURE'], hue=data1['LATITUDE'], palette='viridis')
plt.xlabel('Wind Speed (m/s)')
plt.ylabel('Air Temperature (deg C)')
plt.title('Scatter Plot of Wind Speed vs. Air Temperature')
plt.legend(title='Latitude')
plt.savefig('wind_speed_vs_air_temperature.png', dpi=200)
