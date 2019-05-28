import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals
df_cereal = pd.read_csv("cereal.csv")
print(df_cereal.head())

plt.hist([df_cereal["sugars"], df_cereal["vitamins"]], color=['orange', 'green'])
plt.title("Sugars and Vitamins")
plt.xlabel("Sugars and Vitamins")
plt.legend(["Sugars"," Vitamins"])
plt.show()


# 2. The names of the manufactures are coded using alphabets, create a new column with their fullname using the below mapping.
# 'N': 'Nabisco',
# 'Q': 'Quaker Oats',
# 'K': 'Kelloggs',
# 'R': 'Raslston Purina',
# 'G': 'General Mills' ,
# 'P' :'Post' ,
# 'A':'American Home Foods Products'
# Create a bar plot where each manufacturer is on the y axis and the 
# height of the bars depict the number of cereals manufactured by them.

dict_mfr = {'N': 'Nabisco',
'Q': 'Quaker Oats',
'K': 'Kelloggs',
'R': 'Raslston Purina',
'G': 'General Mills' ,
'P' :'Post' ,
'A':'American Home Foods Products'}

df_cereal["manufactures"] = [dict_mfr[mfr] for mfr in df_cereal["mfr"]]

grouped_mfr =  df_cereal.groupby(["manufactures"], as_index=False).count()
x = grouped_mfr["manufactures"]
y = grouped_mfr["mfr"]

plt.bar(x,y)

plt.setp(plt.gca().get_xticklabels(), rotation=90, horizontalalignment='right')
plt.xlabel("Manufactureres")
plt.ylabel("Count")
plt.title("number of cereals manufactured by Manufactures")
plt.show()