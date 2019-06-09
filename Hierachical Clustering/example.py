import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage


data = pd.read_csv("movie_metadata1.csv")
data.head()

f1 = data["budget"].values
f2 = data["gross"].values

fb = f1[0:10]
fg = f2[0:10]

X = np.array(list(zip(fb, fg)))

z = linkage(X, 'ward')
dn = dendrogram(z)
plt.show()
