#importing xarray, pandas and matplotlib.pyplot
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

#loading data
ds = xr.open_dataset('C:/Users/suege/Desktop/P4/ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc')

da = ds['chlor_a']

variable_name = 'chlor_a'

#slicing data
sliced_data = da.sel(lat=slice(-21,-23), lon=slice(35, 37.5))

da_mean = sliced_data.mean(dim='time')

#selecting the point nearest to a specified location
lat = -22.2  # Latitude of the location
lon = 35.4  # Longitude of the location

#selecting the nearest grid point
nearest_point = sliced_data.sel(lat=-22.2, lon=35.4, method='nearest')

#calculating mean seasonal cycle for Bazaruto and the single point
mean_seasonal_cycle = sliced_data.groupby('time.month').mean(dim='time')
mean_seasonal_cycle_region = mean_seasonal_cycle.mean(dim=['lat','lon'])
bz = nearest_point.groupby('time.month').mean(dim='time',)


#plotting
plt.figure(figsize=(10, 6))
bz.plot(label='Single Point', color='blue')
mean_seasonal_cycle_region.plot(label='Mean Seasonal Cycle for Bazaruto', color='red', linewidth=2)
plt.title('Timeseries Plot')
plt.xlabel('Time')
plt.ylabel('Chlorophyll')
plt.legend()
plt.grid(True)
plt.show()
