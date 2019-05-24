# 2.The dataset given, records data of city temperatures over the years’2014 and 2015. 
# Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.

import pandas as pd
import matplotlib.pyplot as plt

df_temp = pd.read_csv("CityTemps.csv")
print(df_temp)

x_mosco = df_temp["Moscow"]
x_san_Francisco = df_temp["San Francisco"]

plt.hist(x_mosco, len(x_mosco), facecolor='blue', alpha=0.5)
plt.hist(x_san_Francisco, len(x_san_Francisco), facecolor='red', alpha=0.5)

plt.xlabel("Temperature")
plt.ylabel("Frequency")
plt.title("Temperatures of Mosco and San Francisco")

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right') # Rotate Axis Labels

plt.show()