#importing xarray, matplotlib.pyplot and numpy
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

#reading data
data = xr.open_dataset('C:/Users/suege/Desktop/P4/ESACCI-OC-MAPPED-CLIMATOLOGY-1M_MONTHLY_4km_PML_CHL-fv5.0.nc')

da = data['chlor_a']

#slicing data
sliced_data = da.sel(lat=slice(-21,-23), lon=slice(35, 37.5))

da_mean = sliced_data.mean(dim='time')

print(da_mean)

time=sliced_data.time

time.dt.month

#monthly groups
sliced_data.groupby('time.month')

#computing a climatological monthly mean 
seasonal_mean = sliced_data.groupby('time.month').mean()
seasonal_mean

seasonal_mean = seasonal_mean.reindex(month=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
seasonal_mean.plot(col='month', col_wrap=3, cmap='viridis', vmin=0., vmax=5.)