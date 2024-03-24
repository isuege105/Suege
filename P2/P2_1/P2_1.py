import pandas as pd
#load the data
df = pd.read_csv(r'C:\Users\suege\Desktop\SCDM\Assignments\P1\CTD_20081129_1.csv')

#import matplotlib
import matplotlib.pyplot as plt

#create the figure
fig, ax = plt.subplots(1, 2, figsize=(10, 8))

#plot temperature profile
ax[0].plot(df['Temperature'], df['Depth'], color='red')
ax[0].set_xlabel('Temperature (deg C)')
ax[0].set_ylabel('Depth (m)')
ax[0].set_title('Temperature Profile')
ax[0].invert_yaxis()

#plot salinity profile
ax[1].plot(df['Salinity'], df['Depth'], color='blue')
ax[1].set_xlabel('Salinity (psu)')
ax[1].set_ylabel('Depth (m)')
ax[1].set_title('Salinity Profile')
ax[1].invert_yaxis()
ax[1].yaxis.set_visible(False)

#plot
plt.show()