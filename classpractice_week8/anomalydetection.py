import pandas as pd
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt
from datetime import datetime

# Seasonal-Trend Decomposition using LOESS (STL)
# Read the data
ice_cream_interest = pd.read_csv('ice_cream_interest.csv')
ice_cream_interest.set_index('month', inplace=True)


plt.figure(figsize=(10,4))
plt.plot(ice_cream_interest)
for year in range(2004,2021):
    plt.axvline(datetime(year,1,1), color='k', linestyle='--', alpha=0.5)
plt.show()