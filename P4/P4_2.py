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

#plotting
da_mean.plot.contourf(levels=np.arange(0.,30.,2.), figsize=(12,12), vmin=0, vmax=5, cmap='viridis')

